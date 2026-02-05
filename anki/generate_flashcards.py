import requests
import re
from pathlib import Path
import base64


# URL locale de l'API AnkiConnect (Anki doit être lancé avec l'extension AnkiConnect active)
ANKI_URL = "http://localhost:8765"


# Chemin du script actuel (on remonte d'un niveau : parent.parent)
BASE_DIR = Path(__file__).resolve().parent.parent

# Dossier contenant les fichiers Markdown à importer
MARKDOWN_DIR = BASE_DIR / "questions"

# Mapping entre le numéro de module dans le nom de fichier et le nom du deck Anki
MODULE_TO_DECK = {
    "00": "Java :: OCP SE 21 :: Module 00 — Overview",
    "01": "Java :: OCP SE 21 :: Module 01 — Date, Time & Types",
    "02": "Java :: OCP SE 21 :: Module 02 — Control Flow",
    "03": "Java :: OCP SE 21 :: Module 03 — Object-Oriented Concepts",
    "04": "Java :: OCP SE 21 :: Module 04 — Exceptions",
    "05": "Java :: OCP SE 21 :: Module 05 — Arrays & Collections",
    "06": "Java :: OCP SE 21 :: Module 06 — Streams & Lambdas",
    "07": "Java :: OCP SE 21 :: Module 07 — Packaging & Deployment",
    "08": "Java :: OCP SE 21 :: Module 08 — Concurrency",
    "09": "Java :: OCP SE 21 :: Module 09 — I/O API",
    "10": "Java :: OCP SE 21 :: Module 10 — Localization",
    "11": "Java :: OCP SE 21 :: Module 11 — Miscellaneous",
}


# ------------------------------------------------------------------
# Fonctions utilitaires Anki / AnkiConnect
# ------------------------------------------------------------------


def appel_anki(action, params=None):
    """
    Envoie une requête à l'API AnkiConnect avec l'action donnée.

    :param action: Nom de l'action AnkiConnect (ex: 'addNote', 'storeMediaFile').
    :param params: Paramètres à envoyer pour cette action (dict) ou None.
    :return: Un tuple (result, is_duplicate)
             - result : contenu du champ 'result' renvoyé par AnkiConnect
             - is_duplicate : booléen indiquant si l'erreur mentionne un doublon
    """
    payload = {"action": action, "version": 6}
    if params:
        payload["params"] = params

    response = requests.post(ANKI_URL, json=payload, timeout=5)
    result = response.json()

    # Si Anki renvoie une erreur qui n'est pas liée à un doublon, on remonte l'exception
    if result.get("error") and "duplicate" not in result["error"].lower():
        raise Exception(result["error"])

    # On renvoie le résultat ainsi qu'un flag indiquant si l'erreur contenait "duplicate"
    return result.get("result"), "duplicate" in str(result.get("error", "")).lower()


# ------------------------------------------------------------------


def uploader_image(chemin_image: Path):
    """
    Envoie une image à AnkiConnect via l'action 'storeMediaFile'.

    :param chemin_image: Chemin vers le fichier image (Path).
    :return: Le nom de fichier tel qu'il sera référencé dans Anki.
    """
    with open(chemin_image, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")

    # Envoi du fichier encodé en base64 à Anki
    appel_anki(
        "storeMediaFile",
        {
            "filename": chemin_image.name,
            "data": data,
        },
    )

    return chemin_image.name


# ------------------------------------------------------------------


def traiter_images(texte: str):
    """
    Parcourt le texte Markdown et remplace les images de la forme
    ![alt](images/xxx.png)
    par des balises HTML <img src="..."> dont la source est un fichier
    déjà uploadé dans Anki.

    :param texte: Contenu (question/réponse) en Markdown.
    :return: Texte avec les liens d'images remplacés.
    """
    pattern = re.compile(r"!\[[^\]]*\]\((images/[^)]+)\)")

    def remplacer(match):
        # Chemin local vers le fichier image
        chemin = MARKDOWN_DIR / match.group(1)
        if not chemin.exists():
            # Image introuvable localement : on logge et on laisse le Markdown tel quel
            print(f"  ⚠️  Image introuvable : {chemin}")
            return match.group(0)

        # Upload de l'image dans Anki et récupération du nom de fichier
        nom = uploader_image(chemin)
        print(f"  📷 Image uploadée : {nom}")
        # Dans Anki, on réfère l'image par <img src="nom_fichier">
        return f'<img src="{nom}">'

    return pattern.sub(remplacer, texte)


# ------------------------------------------------------------------


def parser_markdown(fichier: Path):
    """
    Analyse un fichier Markdown pour en extraire les paires (Question, Réponse).

    Le format attendu est répété dans le fichier :
        ## Question
        ...
        ## Réponse
        ...
    Les blocs sont extraits jusqu'au prochain '## Question' ou la fin du fichier.

    :param fichier: Chemin du fichier Markdown (Path).
    :return: Liste de tuples [(question, reponse), ...] propres (strip).
    """
    with fichier.open("r", encoding="utf-8") as f:
        contenu = f.read()

    # Regex pour capturer chaque bloc "Question ... Réponse ..."
    pattern = re.compile(
        r"## Question\s*(.*?)\s*## Réponse\s*(.*?)(?=\n## Question|\Z)",
        re.DOTALL,
    )

    # On nettoie les espaces superflus et on ne garde que les blocs non vides
    return [
        (q.strip(), r.strip())
        for q, r in pattern.findall(contenu)
        if q.strip() and r.strip()
    ]


# ------------------------------------------------------------------


def ajouter_carte(question, reponse, nom_modele, champs, deck_name):
    """
    Crée une note Anki à partir d'une question/réponse en utilisant le modèle donné.

    :param question: Texte de la question (front).
    :param reponse: Texte de la réponse (back).
    :param nom_modele: Nom du modèle Anki (ex: 'Basique' / 'Basic').
    :param champs: Liste des noms de champs du modèle.
    :param deck_name: Nom du deck cible.
    :return: Tuple (ajoutee, doublon) :
             - ajoutee : True si la carte a été ajoutée
             - doublon : True si une carte identique existait déjà
    """
    # Remplacement/Upload des images éventuelles dans la question et la réponse
    question = traiter_images(question)
    reponse = traiter_images(reponse)

    payload = {
        "note": {
            "deckName": deck_name,
            "modelName": nom_modele,
            "fields": {
                champs[0]: question,
                champs[1]: reponse,
            },
            "tags": ["java", "ocp", "se21"],
            "options": {"allowDuplicate": False},
        }
    }

    result, duplicate = appel_anki("addNote", payload)
    # On renvoie un double booléen pour faciliter les stats (ajout vs doublon)
    return not duplicate, duplicate


# ------------------------------------------------------------------


def main():
    """
    Point d'entrée principal :
    - Vérifie la connexion à AnkiConnect.
    - Détermine le modèle de carte ('Basique' ou 'Basic').
    - Parcourt les fichiers Markdown module-*.md.
    - Pour chaque fichier, importe toutes les cartes dans le deck correspondant.
    """
    # Vérification que l'API AnkiConnect est accessible
    version, _ = appel_anki("version")
    print(f"✅ Anki connecté (version {version})")

    # Récupération des modèles disponibles et choix Basique/Basic
    modeles, _ = appel_anki("modelNames")
    nom_modele = "Basique" if "Basique" in modeles else "Basic"

    # Récupération des noms de champs du modèle choisi
    champs, _ = appel_anki("modelFieldNames", {"modelName": nom_modele})
    print(f"📝 Modèle '{nom_modele}' | Champs : {' / '.join(champs)}")

    # Parcours des fichiers Markdown dans le dossier 'questions'
    for fichier_md in sorted(MARKDOWN_DIR.glob("module-*.md")):
        # On attend un nom de fichier du type 'module-01-...' pour extraire le numéro de module
        match = re.match(r"module-(\d+)-", fichier_md.name)
        if not match:
            print(f"⏭️  Ignoré : {fichier_md.name}")
            continue

        module_num = match.group(1)
        deck_name = MODULE_TO_DECK.get(module_num)

        if not deck_name:
            # Si le module n'a pas de mapping défini, on le signale et on passe au suivant
            print(f"⚠️  Module inconnu : {module_num}")
            continue

        print(f"\n📦 Import depuis {fichier_md.name}")
        print(f"➡️  Deck : {deck_name}")

        # Extraction des cartes (question/réponse) depuis le Markdown
        cartes = parser_markdown(fichier_md)
        print(f"📚 {len(cartes)} carte(s) trouvée(s)")

        ajout, doublon = 0, 0
        # Ajout de chaque carte dans Anki
        for q, r in cartes:
            ok, dup = ajouter_carte(q, r, nom_modele, champs, deck_name)
            if ok:
                ajout += 1
            elif dup:
                doublon += 1

        print(f"✅ {ajout} ajoutée(s) | ⏭️  {doublon} ignorée(s)")


# ------------------------------------------------------------------


if __name__ == "__main__":
    main()
