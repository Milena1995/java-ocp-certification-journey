import requests
import re
from pathlib import Path
import base64

# ============================================================
# CONFIGURATION GÉNÉRALE
# ============================================================

# URL locale de l'API AnkiConnect
# (Anki doit être lancé avec l'extension AnkiConnect active)
ANKI_URL = "http://localhost:8765"

# Dossier racine du script
BASE_DIR = Path(__file__).resolve().parent

# Dossier contenant les fichiers Markdown à importer
MARKDOWN_DIR = BASE_DIR / "questions"


# ============================================================
# MAPPING (MODULE, SOUS-MODULE) -> DECK ANKI
# ============================================================
#
# - Clé : tuple (module, sous_module)
# - sous_module = None  → module mono-deck
# - sous_module = "01", "02", ... → sous-deck précis
#
# IMPORTANT :
# Le nom du fichier DOIT être :
#   module-01-02-xxxx.md
#           ^^ ^^
#        module sous-module
#

MODULE_TO_DECK = {
    # -----------------------
    # MODULE 01 (split)
    # -----------------------
    ("01", "01"): "Java::OCP SE 21::Module 01 — Date, Time & Types::Java Overview & JVM",
    ("01", "02"): "Java::OCP SE 21::Module 01 — Date, Time & Types::Primitives & Variables",
    ("01", "03"): "Java::OCP SE 21::Module 01 — Date, Time & Types::Operators & Precedence",
    ("01", "04"): "Java::OCP SE 21::Module 01 — Date, Time & Types::Wrapper Classes & Conversions",
    ("01", "05"): "Java::OCP SE 21::Module 01 — Date, Time & Types::Math API & Boolean Logic",
    ("01", "06"): "Java::OCP SE 21::Module 01 — Date, Time & Types::Strings & Text Manipulation",
    ("01", "07"): "Java::OCP SE 21::Module 01 — Date, Time & Types::Date & Time API",
    ("01", "08"): "Java::OCP SE 21::Module 01 — Date, Time & Types::Period, Duration & Formatting",
    ("01", "09"): "Java::OCP SE 21::Module 01 — Date, Time & Types::Time Zones & DST",

    # -----------------------
    # MODULES MONO-DECK
    # -----------------------
    ("00", None): "Java::OCP SE 21::Module 00 — Overview",
    ("02", None): "Java::OCP SE 21::Module 02 — Control Flow",
    ("03", None): "Java::OCP SE 21::Module 03 — Object-Oriented Concepts",
    ("04", None): "Java::OCP SE 21::Module 04 — Exceptions",
    ("05", None): "Java::OCP SE 21::Module 05 — Arrays & Collections",
    ("06", None): "Java::OCP SE 21::Module 06 — Streams & Lambdas",
    ("07", None): "Java::OCP SE 21::Module 07 — Packaging & Deployment",
    ("08", None): "Java::OCP SE 21::Module 08 — Concurrency",
    ("09", None): "Java::OCP SE 21::Module 09 — I/O API",
    ("10", None): "Java::OCP SE 21::Module 10 — Localization",
    ("11", None): "Java::OCP SE 21::Module 11 — Miscellaneous",
}


# ============================================================
# ANKICONNECT – FONCTIONS UTILITAIRES
# ============================================================

def appel_anki(action, params=None):
    """
    Envoie une requête à AnkiConnect.

    :param action: Nom de l'action AnkiConnect (ex: 'addNote')
    :param params: Dictionnaire de paramètres
    :return: (result, is_duplicate)
    """
    payload = {"action": action, "version": 6}
    if params:
        payload["params"] = params

    response = requests.post(ANKI_URL, json=payload, timeout=5)
    result = response.json()

    # Toute erreur autre qu'un doublon est bloquante
    if result.get("error") and "duplicate" not in result["error"].lower():
        raise Exception(result["error"])

    return result.get("result"), "duplicate" in str(result.get("error", "")).lower()


# ============================================================

def uploader_image(chemin_image: Path):
    """
    Upload une image locale dans Anki (media collection).
    """
    with open(chemin_image, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")

    appel_anki(
        "storeMediaFile",
        {"filename": chemin_image.name, "data": data},
    )

    return chemin_image.name


# ============================================================

def traiter_images(texte: str):
    """
    Remplace les images Markdown par <img src="..."> après upload.
    """
    pattern = re.compile(r"!\[[^\]]*\]\((images/[^)]+)\)")

    def remplacer(match):
        chemin = MARKDOWN_DIR / match.group(1)
        if not chemin.exists():
            print(f"⚠️ Image introuvable : {chemin}")
            return match.group(0)

        nom = uploader_image(chemin)
        return f'<img src="{nom}">'

    return pattern.sub(remplacer, texte)


# ============================================================

def parser_markdown(fichier: Path):
    """
    Extrait toutes les paires (Question, Réponse) du fichier Markdown.
    """
    contenu = fichier.read_text(encoding="utf-8")

    pattern = re.compile(
        r"## Question\s*(.*?)\s*## Réponse\s*(.*?)(?=\n## Question|\Z)",
        re.DOTALL,
    )

    return [
        (q.strip(), r.strip())
        for q, r in pattern.findall(contenu)
        if q.strip() and r.strip()
    ]


# ============================================================

def ajouter_carte(question, reponse, nom_modele, champs, deck_name):
    """
    Ajoute une carte Anki (Basic / Basique).
    """
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

    _, duplicate = appel_anki("addNote", payload)
    return not duplicate, duplicate


# ============================================================
# MAIN
# ============================================================

def main():
    # Vérification AnkiConnect
    version, _ = appel_anki("version")
    print(f"✅ Anki connecté (version {version})")

    # Choix du modèle
    modeles, _ = appel_anki("modelNames")
    nom_modele = "Basique" if "Basique" in modeles else "Basic"
    champs, _ = appel_anki("modelFieldNames", {"modelName": nom_modele})

    print(f"📝 Modèle : {nom_modele} | Champs : {champs}")

    # Parcours des fichiers Markdown
    for fichier_md in sorted(MARKDOWN_DIR.glob("module-*.md")):
        print(f"\n🔎 Fichier : {fichier_md.name}")

        # Format attendu :
        # module-01-02-xxxx.md
        match = re.match(r"module-(\d+)-(\d+)-", fichier_md.name, re.IGNORECASE)

        if match:
            module = match.group(1).zfill(2)
            submodule = match.group(2).zfill(2)
        else:
            # Cas mono-deck : module-02-xxxx.md
            match = re.match(r"module-(\d+)-", fichier_md.name, re.IGNORECASE)
            if not match:
                print("⏭️ Nom invalide, ignoré")
                continue
            module = match.group(1).zfill(2)
            submodule = None

        deck_name = MODULE_TO_DECK.get((module, submodule))
        if not deck_name:
            print(f"⚠️ Deck non défini pour module {module}, sous-module {submodule}")
            continue

        print(f"➡️ Deck cible : {deck_name}")

        cartes = parser_markdown(fichier_md)
        print(f"📚 {len(cartes)} cartes trouvées")

        ajout = doublon = 0
        for q, r in cartes:
            ok, dup = ajouter_carte(q, r, nom_modele, champs, deck_name)
            ajout += ok
            doublon += dup

        print(f"✅ {ajout} ajoutées | ⏭️ {doublon} doublons")


# ============================================================

if __name__ == "__main__":
    main()
