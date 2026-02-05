## Question

Quelle est la différence entre GMT et UTC ?<br><br>

A) GMT est une timezone, UTC est un standard de temps mondial<br>
B) GMT et UTC sont exactement identiques et interchangeables<br>
C) UTC est uniquement pour l'astronomie, GMT pour la coordination globale<br>
D) GMT s'ajuste avec le DST, UTC non

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>GMT (Greenwich Mean Time) :</strong><br>
- Une <strong>timezone</strong> (fuseau horaire)<br>
- Basée sur l'observatoire de Greenwich<br>
- Terme historique<br><br>

<strong>UTC (Coordinated Universal Time) :</strong><br>
- Un <strong>standard de temps</strong> utilisé mondialement<br>
- Basé sur des horloges atomiques<br>
- Plus précis que GMT<br>
- Référence internationale<br><br>

En pratique, GMT et UTC sont très proches mais <strong>techniquement différents</strong>.<br><br>

<strong>B) est incorrect :</strong> Pas exactement identiques techniquement.<br>
<strong>C) est incorrect :</strong> UTC est le standard mondial, pas seulement astronomique.<br>
<strong>D) est incorrect :</strong> Ni GMT ni UTC ne s'ajustent au DST.

## Question

Qu'est-ce que l'Unix Epoch ?<br><br>

A) Un format de calendrier utilisé uniquement dans les applications Java<br>
B) Un système de mesure du temps basé sur GMT<br>
C) Une classe Java pour travailler avec les timezones<br>
D) Le nombre de secondes écoulées depuis le 1er janvier 1970 UTC

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

L'<strong>Unix Epoch</strong> est le nombre de secondes (ou millisecondes) écoulées depuis :<br>
<strong>1er janvier 1970, 00:00:00 UTC</strong><br><br>

C'est le point de référence utilisé par :<br>
- Unix/Linux<br>
- Java (Instant)<br>
- La plupart des systèmes informatiques<br><br>

Exemple :<br>
- Epoch = 0 → 1970-01-01T00:00:00Z<br>
- 86400 secondes = +1 jour<br><br>

<strong>A), B), C) sont incorrects :</strong> Mauvaise définition.

## Question

Comment convertir une instance Calendar en objet Date en Java ?<br><br>

A) calendar.toDate();<br>
B) Date date = calendar.getTime();<br>
C) Date date = new Date(calendar);<br>
D) Date date = Calendar.toDate(calendar);

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

La méthode correcte est <strong>calendar.getTime()</strong>.<br><br>

Exemple :<br>
Calendar calendar = Calendar.getInstance();<br>
Date date = calendar.getTime();<br><br>

Note : C'est l'ancienne API (java.util). Dans le code moderne, utiliser java.time.<br><br>

<strong>A), C), D) sont incorrects :</strong> Méthodes inexistantes ou syntaxe incorrecte.

## Question

Comment parser correctement une date String avec SimpleDateFormat ?<br><br>

A) Date date = Date.parse("yyyy-MM-dd", "2023-10-15");<br>
B) Date date = SimpleDateFormat.parse("yyyy-MM-dd", "2023-10-15");<br>
C) Date date = new SimpleDateFormat("yyyy-MM-dd").parse("2023-10-15");<br>
D) Date date = new Date("2023-10-15").format("yyyy-MM-dd");

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

La syntaxe correcte est :<br>
<strong>Date date = new SimpleDateFormat("yyyy-MM-dd").parse("2023-10-15");</strong><br><br>

Étapes :<br>
1. Créer un SimpleDateFormat avec le pattern<br>
2. Appeler parse() avec le String<br><br>

Note :<br>
- C'est l'ancienne API<br>
- Dans le code moderne, utiliser DateTimeFormatter avec java.time<br><br>

<strong>A), B), D) sont incorrects :</strong> Syntaxe incorrecte.

## Question

Quelle est la différence entre LocalDateTime et ZonedDateTime ?<br><br>

A) LocalDateTime n'inclut pas de timezone, ZonedDateTime inclut une timezone spécifique<br>
B) LocalDateTime est toujours en UTC, ZonedDateTime s'ajuste au système<br>
C) ZonedDateTime peut stocker uniquement des dates, LocalDateTime date et heure<br>
D) LocalDateTime nécessite une conversion manuelle en timestamps avant comparaison

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>Différence clé :</strong><br><br>

<strong>LocalDateTime :</strong><br>
- Date + heure<br>
- ❌ <strong>Pas de timezone</strong><br>
- Représentation locale sans contexte géographique<br><br>

<strong>ZonedDateTime :</strong><br>
- Date + heure + <strong>timezone</strong><br>
- ✅ Inclut ZoneId<br>
- Gère automatiquement le DST<br>
- Représentation complète avec contexte<br><br>

<strong>B), C), D) sont incorrects :</strong> Fausses affirmations.

## Question

En quoi java.time.Period diffère-t-il de Duration ?<br><br>

A) Period ne peut être utilisé que pour convertir des timezones<br>
B) Period est toujours en UTC, Duration est local<br>
C) Duration peut stocker des timestamps futurs, Period non<br>
D) Period représente des différences date-based (années, mois, jours), Duration représente des différences time-based (heures, minutes, secondes)

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

<strong>Différence fondamentale :</strong><br><br>

<strong>Period :</strong><br>
- Human-scale<br>
- Basé sur : <strong>années, mois, jours</strong><br>
- Dépend du calendrier<br>
- Utilisé avec LocalDate<br><br>

<strong>Duration :</strong><br>
- Machine-scale<br>
- Basé sur : <strong>heures, minutes, secondes, nanosecondes</strong><br>
- Mesure exacte<br>
- Utilisé avec Instant, LocalTime<br><br>

<strong>A), B), C) sont incorrects :</strong> Mauvaise compréhension.

## Question

Que fournit java.time.Clock ?<br><br>

A) Une synchronisation automatique avec une horloge atomique<br>
B) Un timer haute précision pour mesurer la vitesse d'exécution<br>
C) Une abstraction sur le temps système, permettant un contrôle et des tests du temps<br>
D) Un timestamp fixe qui ne change jamais

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>java.time.Clock</strong> fournit une <strong>abstraction sur le temps système</strong>.<br><br>

Avantages :<br>
- Permet de <strong>contrôler le temps</strong> dans les tests<br>
- Rend le code <strong>testable</strong><br>
- Peut simuler différentes zones horaires<br>
- Peut figer le temps pour les tests<br><br>

Exemple d'usage :<br>
- Production : Clock.systemDefaultZone()<br>
- Tests : Clock.fixed() pour un temps constant<br><br>

<strong>A), B), D) sont incorrects :</strong> Pas le rôle principal.

## Question

Quel est le but principal du package java.time.temporal ?<br><br>

A) Définir les classes date-time de haut niveau comme LocalDateTime<br>
B) Fournir un support bas niveau pour la manipulation date-time (ajout/retrait d'unités)<br>
C) Gérer les horloges système dans les applications Java<br>
D) Remplacer SimpleDateFormat pour le formatage de dates

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>java.time.temporal</strong> fournit un <strong>support bas niveau</strong> pour la manipulation date-time.<br><br>

Contient :<br>
- <strong>Temporal</strong> : interface pour objets date-time<br>
- <strong>TemporalAmount</strong> : interface pour quantités de temps<br>
- <strong>TemporalUnit</strong> : unités de temps (ChronoUnit)<br>
- <strong>TemporalField</strong> : champs date-time<br>
- <strong>TemporalAdjuster</strong> : ajustements personnalisés<br><br>

Permet des opérations comme :<br>
- Ajout/retrait d'unités<br>
- Requêtes sur les champs<br>
- Ajustements complexes<br><br>

<strong>A) est incorrect :</strong> C'est java.time qui contient LocalDateTime.<br>
<strong>C) est incorrect :</strong> Les horloges sont dans Clock.<br>
<strong>D) est incorrect :</strong> Le formatage est dans java.time.format.

## Question

Dans l'ancienne API, pourquoi SimpleDateFormat n'est-il PAS thread-safe ?<br><br>

A) Parce qu'il utilise trop de mémoire<br>
B) Parce qu'il est mutable et peut être modifié pendant l'utilisation<br>
C) Parce qu'il ne supporte pas le multithreading<br>
D) Parce qu'il est trop lent

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>SimpleDateFormat n'est PAS thread-safe</strong> car il est <strong>mutable</strong>.<br><br>

Problème :<br>
- État interne modifiable<br>
- Partage entre threads → comportement imprévisible<br>
- Corruption de données possible<br><br>

Solutions avec l'ancienne API :<br>
- Créer une instance par thread<br>
- Synchroniser l'accès<br>
- Utiliser ThreadLocal<br><br>

<strong>Solution moderne :</strong><br>
Utiliser <strong>DateTimeFormatter</strong> (immutable et thread-safe).<br><br>

<strong>A), C), D) sont incorrects :</strong> Pas la vraie raison.

## Question

Quelle méthode permet d'ajouter une durée à un Instant ?<br><br>

A) instant.add(duration);<br>
B) instant.plus(duration);<br>
C) instant.plusDuration(duration);<br>
D) Duration.add(instant, duration);

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

La méthode correcte est <strong>instant.plus(duration)</strong>.<br><br>

Exemple :<br>
Instant instant = Instant.now();<br>
Duration duration = Duration.ofHours(2);<br>
Instant nouveau = instant.plus(duration);<br><br>

Autres méthodes similaires :<br>
- instant.plusSeconds(long)<br>
- instant.plusMillis(long)<br>
- instant.plusNanos(long)<br><br>

Rappel : Instant est immutable, donc retourne un nouvel objet.<br><br>

<strong>A), C), D) sont incorrects :</strong> Méthodes inexistantes ou syntaxe incorrecte.

## Question

Comment obtenir le nombre de jours entre deux LocalDate ?<br><br>

A) date1.minus(date2).getDays();<br>
B) ChronoUnit.DAYS.between(date1, date2);<br>
C) Period.between(date1, date2).getTotalDays();<br>
D) Duration.between(date1, date2).toDays();

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

La méthode correcte est <strong>ChronoUnit.DAYS.between(date1, date2)</strong>.<br><br>

Retourne un <strong>long</strong> représentant le nombre de jours.<br><br>

Exemple :<br>
LocalDate d1 = LocalDate.of(2024, 1, 1);<br>
LocalDate d2 = LocalDate.of(2024, 1, 15);<br>
long jours = ChronoUnit.DAYS.between(d1, d2); // 14<br><br>

<strong>A) est incorrect :</strong> minus() retourne un LocalDate, pas une durée.<br>
<strong>C) est incorrect :</strong> getTotalDays() n'existe pas (Period a getDays() mais pas le total).<br>
<strong>D) est incorrect :</strong> Duration.between() ne fonctionne pas avec LocalDate.

## Question

Que retourne Period.between(LocalDate.of(2024, 1, 15), LocalDate.of(2024, 3, 10)) ?<br><br>

A) P55D (55 jours)<br>
B) P1M25D (1 mois et 25 jours)<br>
C) P2M (2 mois)<br>
D) P1M26D (1 mois et 26 jours)

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Period.between()</strong> calcule la différence en <strong>années, mois et jours</strong>.<br><br>

Calcul :<br>
- Du 15 janvier au 15 février = 1 mois<br>
- Du 15 février au 10 mars = 25 jours<br>
- Total : <strong>P1M25D</strong> (1 mois, 25 jours)<br><br>

Format ISO : P[années]Y[mois]M[jours]D<br><br>

Important : Period utilise le calendrier, pas un nombre total de jours.<br><br>

<strong>A), C), D) sont incorrects :</strong> Mauvais calcul.

## Question

Quelle classe de l'ancienne API Date/Time doit absolument être évitée dans du code moderne ?<br><br>

A) java.time.LocalDate<br>
B) java.util.Date<br>
C) java.time.Instant<br>
D) java.time.ZonedDateTime

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>À ÉVITER absolument :</strong><br>
- java.util.Date<br>
- java.util.Calendar<br>
- java.text.SimpleDateFormat<br><br>

Raisons :<br>
- Mutable (pas thread-safe)<br>
- API confuse<br>
- Bugs historiques (mois à partir de 0)<br>
- Mélange date/heure/timezone<br><br>

<strong>À UTILISER :</strong><br>
- java.time.* (LocalDate, Instant, ZonedDateTime, etc.)<br><br>

<strong>A), C), D) sont incorrects :</strong> Ce sont les nouvelles classes recommandées.

## Question

Quelle est la meilleure pratique pour stocker un DateTimeFormatter réutilisable ?<br><br>

A) Le créer à chaque utilisation<br>
B) Le déclarer comme constante static final<br>
C) L'instancier dans un bloc synchronized<br>
D) Utiliser ThreadLocal

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Bonne pratique :</strong> Déclarer comme <strong>constante static final</strong>.<br><br>

Exemple :<br>
private static final DateTimeFormatter FORMATTER = <br>
    DateTimeFormatter.ofPattern("dd/MM/yyyy");<br><br>

Raisons :<br>
- DateTimeFormatter est <strong>immutable</strong><br>
- <strong>Thread-safe</strong><br>
- Peut être réutilisé partout<br>
- Performances optimales<br><br>

<strong>A) est incorrect :</strong> Gaspillage de ressources.<br>
<strong>C) et D) sont incorrects :</strong> Inutiles car déjà thread-safe.

## Question

Comment créer un Clock fixe pour les tests ?<br><br>

A) Clock.systemUTC()<br>
B) Clock.fixed(Instant, ZoneId)<br>
C) new Clock(Instant)<br>
D) Clock.freeze()

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Pour créer un <strong>Clock fixe pour les tests</strong> :<br>
<strong>Clock.fixed(Instant, ZoneId)</strong><br><br>

Exemple :<br>
Instant instant = Instant.parse("2024-01-15T10:00:00Z");<br>
Clock clock = Clock.fixed(instant, ZoneId.of("Europe/Paris"));<br>
LocalDateTime ldt = LocalDateTime.now(clock); // toujours 15 jan 2024 11:00<br><br>

Utile pour :<br>
- Tests unitaires<br>
- Comportement prévisible<br>
- Vérification de logique temporelle<br><br>

<strong>A) est incorrect :</strong> Retourne l'heure système actuelle.<br>
<strong>C) et D) sont incorrects :</strong> Méthodes inexistantes.

## Question

Quelle interface tous les types date-time principaux implémentent-ils ?<br><br>

A) DateTime<br>
B) Temporal<br>
C) TimeStamp<br>
D) Chronological

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Tous les types date-time principaux implémentent l'interface <strong>Temporal</strong>.<br><br>

Types qui implémentent Temporal :<br>
- LocalDate<br>
- LocalTime<br>
- LocalDateTime<br>
- ZonedDateTime<br>
- Instant<br>
- OffsetDateTime<br><br>

Cela permet :<br>
- Utilisation avec ChronoUnit.between()<br>
- Manipulation générique de date-time<br>
- Support des TemporalAdjuster<br><br>

<strong>A), C), D) sont incorrects :</strong> Interfaces inexistantes.

## Question

Quelle méthode permet de formater un LocalDate en String personnalisé ?<br><br>

A) localDate.toString("dd/MM/yyyy");<br>
B) localDate.format(DateTimeFormatter.ofPattern("dd/MM/yyyy"));<br>
C) DateTimeFormatter.format(localDate, "dd/MM/yyyy");<br>
D) String.format(localDate, "dd/MM/yyyy");

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

La méthode correcte est :<br>
<strong>localDate.format(DateTimeFormatter.ofPattern("dd/MM/yyyy"))</strong><br><br>

Exemple :<br>
LocalDate date = LocalDate.of(2024, 1, 15);<br>
String formatted = date.format(DateTimeFormatter.ofPattern("dd/MM/yyyy"));<br>
// Résultat : "15/01/2024"<br><br>

Ou avec un formatter réutilisable :<br>
private static final DateTimeFormatter FMT = DateTimeFormatter.ofPattern("dd/MM/yyyy");<br>
String formatted = date.format(FMT);<br><br>

<strong>A), C), D) sont incorrects :</strong> Syntaxe incorrecte.

## Question

Qu'est-ce qu'une API Java ?<br><br>

A) Un package Java<br>
B) Un ensemble de classes, interfaces, enums et méthodes fournies par le JDK<br>
C) Une application web<br>
D) Un protocole de communication

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Une <strong>API Java</strong> est un ensemble de classes, interfaces, enums et méthodes fournies par le JDK pour résoudre un problème donné.<br><br>

Exemples :<br>
- API Collections → List, Map<br>
- API Date & Time → LocalDate, Instant, ZonedDateTime<br><br>

<strong>Important :</strong> API ≠ package<br>
- API = fonctionnalité logique<br>
- package = organisation technique<br><br>

<strong>A) est incorrect :</strong> Un package est l'organisation, pas la fonctionnalité.<br>
<strong>C) et D) sont incorrects :</strong> Pas en contexte Java.

## Question

Pourquoi l'ancienne API Date (java.util.Date) était-elle problématique ?<br><br>

A) Elle était trop rapide<br>
B) Elle était mutable, pas thread-safe, et avait une API confuse<br>
C) Elle ne supportait pas les dates après 2000<br>
D) Elle était immutable

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Ancienne API (MAUVAISE CONCEPTION) :</strong><br>
- java.util.Date<br>
- java.util.Calendar<br><br>

<strong>Problèmes :</strong><br>
- ❌ Mutable<br>
- ❌ Pas thread-safe<br>
- ❌ Mois à partir de 0<br>
- ❌ API confuse<br>
- ❌ Mélange date / heure / timezone<br><br>

<strong>A), C), D) sont incorrects :</strong> Mauvaises raisons.

## Question

Quand la nouvelle API Date & Time (JSR-310) a-t-elle été introduite ?<br><br>

A) Java 5<br>
B) Java 6<br>
C) Java 8<br>
D) Java 11

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

La <strong>nouvelle API (JSR-310)</strong> a été introduite en <strong>Java 8</strong>.<br><br>

Implémentée via :<br>
- java.time<br>
- java.time.temporal<br>
- java.time.format<br>
- java.time.zone<br><br>

Avantages :<br>
- ✅ Immutable<br>
- ✅ Thread-safe<br>
- ✅ Claire<br>
- ✅ ISO-8601<br><br>

<strong>A), B), D) sont incorrects :</strong> Mauvaise version.

## Question

Que signifie qu'un objet est "immutable" dans java.time ?<br><br>

A) Il peut être modifié mais lentement<br>
B) Il ne change jamais après sa création<br>
C) Il est stocké en mémoire permanente<br>
D) Il ne peut pas être copié

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Un objet <strong>immutable</strong> ne change jamais après sa création.<br><br>

<strong>Conséquence (PIÈGE MAJEUR OCP) :</strong><br>
date.plusDays(1); // ❌ ne modifie PAS date<br>
date = date.plusDays(1); // ✅ assigne le nouvel objet<br><br>

Toutes les méthodes retournent un <strong>NOUVEL objet</strong>.<br><br>

Pourquoi c'est bien :<br>
- Thread-safe<br>
- Pas de bugs concurrents<br>
- Comportement prévisible<br><br>

<strong>A), C), D) sont incorrects :</strong> Mauvaise définition.

## Question

Quel code modifie correctement la date ?<br><br>

A) date.plusDays(1);<br>
B) date = date.plusDays(1);<br>
C) date.setDays(date.getDays() + 1);<br>
D) date.modify(1)

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Avec les objets <strong>immutables</strong>, il faut <strong>réassigner</strong> :<br>
date = date.plusDays(1);<br><br>

<strong>A) est incorrect :</strong> Ne modifie pas date, retourne un nouvel objet perdu.<br>
<strong>C) est incorrect :</strong> Pas de setters dans java.time (immutable).<br>
<strong>D) est incorrect :</strong> Méthode inexistante.<br><br>

<strong>Piège OCP majeur :</strong> date.plusDays(1) ne modifie PAS date.

## Question

Que représente LocalDate ?<br><br>

A) Une date avec heure et timezone<br>
B) Une date sans heure ni timezone<br>
C) Un timestamp UTC<br>
D) Une durée en jours

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>LocalDate</strong> représente :<br>
- Date <strong>sans heure</strong><br>
- <strong>Pas de timezone</strong><br><br>

Exemples d'usage :<br>
- Date de naissance<br>
- Date de facture<br>
- Dates anniversaires<br><br>

Format ISO : yyyy-MM-dd<br>
Exemple : 2024-01-15<br><br>

<strong>A) est incorrect :</strong> C'est ZonedDateTime.<br>
<strong>C) est incorrect :</strong> C'est Instant.<br>
<strong>D) est incorrect :</strong> C'est Period ou Duration.

## Question

Que représente LocalTime ?<br><br>

A) Une heure avec date<br>
B) Une heure sans date ni timezone<br>
C) Un timestamp<br>
D) Une durée

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>LocalTime</strong> représente :<br>
- Heure <strong>sans date</strong><br>
- <strong>Pas de timezone</strong><br><br>

Exemples d'usage :<br>
- Heure d'ouverture d'un magasin<br>
- Heure d'alarme<br>
- Horaires récurrents<br><br>

Format ISO : HH:mm:ss<br>
Exemple : 14:30:00<br><br>

<strong>A) est incorrect :</strong> C'est LocalDateTime.<br>
<strong>C) et D) sont incorrects :</strong> Mauvaise catégorie.

## Question

Que représente LocalDateTime ?<br><br>

A) Date + heure + timezone<br>
B) Date + heure sans timezone<br>
C) Un point absolu dans le temps<br>
D) Une durée

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>LocalDateTime</strong> représente :<br>
- <strong>Date + heure</strong><br>
- ❌ <strong>Pas de timezone</strong><br>
- Temps humain local<br><br>

Important : sans timezone, c'est ambigu pour des événements mondiaux.<br><br>

Format : yyyy-MM-ddTHH:mm:ss<br>
Exemple : 2024-01-15T14:30:00<br><br>

<strong>Piège OCP :</strong> LocalDateTime ne gère PAS la timezone.<br><br>

<strong>A) est incorrect :</strong> C'est ZonedDateTime.<br>
<strong>C) est incorrect :</strong> C'est Instant.

## Question

Quelle méthode est la plus sûre pour créer une date ?<br><br>

A) LocalDate.now()<br>
B) LocalDate.of(2024, 1, 15)<br>
C) LocalDate.parse("2024-01-15")<br>
D) new LocalDate(2024, 1, 15)

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>of()</strong> est LA PLUS SÛRE car :<br>
- Valeurs numériques<br>
- Aucune ambiguïté<br>
- Vérification à la compilation<br>
- Pas d'exception de parsing<br><br>

<strong>A)</strong> dépend de l'horloge système (peut varier).<br>
<strong>C)</strong> strict ISO, erreurs à l'exécution possibles.<br>
<strong>D)</strong> pas de constructeur public.<br><br>

LocalDate.of(2024, 1, 15); // ✅ SÛRE

## Question

Que se passe-t-il avec LocalDate.parse("2024-1-15") ?<br><br>

A) Crée la date 15 janvier 2024<br>
B) DateTimeParseException à l'exécution<br>
C) Erreur de compilation<br>
D) Conversion automatique au format correct

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>parse()</strong> est <strong>STRICT</strong> :<br>
- ISO strict par défaut<br>
- Pas de correction<br>
- Pas d'approximation<br><br>

Format attendu : yyyy-MM-dd (avec zéros)<br>
Format fourni : yyyy-M-d (sans zéros)<br><br>

Résultat : <strong>DateTimeParseException</strong> à l'exécution.<br><br>

Java ne devine jamais, ne corrige jamais.<br><br>

<strong>A), C), D) sont incorrects :</strong> Exception à l'exécution.

## Question

Quelle est la différence entre plusDays() et withDayOfMonth() ?<br><br>

A) Aucune différence<br>
B) plus = relatif (ajout), with = absolu (remplacement)<br>
C) with = relatif, plus = absolu<br>
D) Les deux font la même chose différemment

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Différence CLÉ :</strong><br><br>

<strong>plusDays()</strong> :<br>
- Opération <strong>relative</strong><br>
- Ajoute des jours<br>
- date.plusDays(5) → +5 jours<br><br>

<strong>withDayOfMonth()</strong> :<br>
- Opération <strong>absolue</strong><br>
- Remplace directement<br>
- date.withDayOfMonth(15) → jour = 15<br><br>

<strong>Règle :</strong> plus/minus = relatif, with = absolu<br><br>

<strong>A), C), D) sont incorrects :</strong> Il y a une différence importante.

## Question

Qu'est-ce que "machine-scale" vs "human-scale" ?<br><br>

A) Des échelles de performance<br>
B) Machine = temps absolu UTC, Human = calendrier avec règles humaines<br>
C) Des versions de Java différentes<br>
D) Des formats de date différents

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Machine-scale :</strong><br>
- Temps absolu<br>
- UTC<br>
- Indépendant des humains<br>
- Classes : Instant, Duration<br><br>

<strong>Human-scale :</strong><br>
- Calendrier<br>
- Règles humaines (mois, années, DST)<br>
- Classes : LocalDate, LocalDateTime, Period, ZonedDateTime<br><br>

<strong>A), C), D) sont incorrects :</strong> Mauvaise catégorie.

## Question

Qu'est-ce que l'epoch en Java ?<br><br>

A) 1er janvier 2000 à minuit<br>
B) 1er janvier 1970 00:00:00 UTC<br>
C) Le moment de création de la JVM<br>
D) 1er janvier 1900 à minuit

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

L'<strong>epoch</strong> est le point de référence :<br>
<strong>1970-01-01T00:00:00Z (UTC)</strong><br><br>

Instant est basé sur l'epoch :<br>
- Instant.ofEpochSecond(0) → epoch<br>
- Instant.ofEpochMilli(1000) → +1 seconde<br><br>

Les timestamps sont souvent exprimés en millisecondes depuis l'epoch.<br><br>

<strong>A), C), D) sont incorrects :</strong> Mauvaise date.

## Question

Que fait Instant.toEpochMilli() ?<br><br>

A) Convertit en LocalDateTime<br>
B) Retourne le nombre de millisecondes depuis l'epoch (1970)<br>
C) Convertit en format ISO<br>
D) Retourne l'année actuelle

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>toEpochMilli()</strong> retourne un <strong>long</strong> représentant le nombre de millisecondes depuis l'epoch (1970-01-01T00:00:00Z).<br><br>

Exemple :<br>
Instant instant = Instant.now();<br>
long millis = instant.toEpochMilli();<br><br>

Utile pour :<br>
- Interopérabilité avec anciennes APIs<br>
- Stockage en base de données<br>
- Comparaisons numériques<br><br>

<strong>A), C), D) sont incorrects :</strong> Mauvaise fonction.

## Question

Comment convertir un Instant en représentation humaine ?<br><br>

A) instant.toLocalDateTime()<br>
B) instant.atZone(ZoneId)<br>
C) instant.format()<br>
D) new ZonedDateTime(instant)

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Pour convertir <strong>Instant → représentation humaine</strong> :<br>
<strong>instant.atZone(ZoneId)</strong><br><br>

Exemple :<br>
Instant instant = Instant.now();<br>
ZonedDateTime zdt = instant.atZone(ZoneId.of("Europe/Paris"));<br><br>

Cette méthode ajoute le contexte timezone nécessaire pour affichage humain.<br><br>

<strong>A) est incorrect :</strong> Il faut spécifier une zone.<br>
<strong>C) et D) sont incorrects :</strong> Syntaxe incorrecte.

## Question

Qu'est-ce que ChronoUnit ?<br><br>

A) Une classe pour créer des dates<br>
B) Un enum représentant des unités de temps<br>
C) Une interface pour les durées<br>
D) Un formatter de dates

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>ChronoUnit</strong> est un <strong>enum</strong> représentant des unités de temps.<br><br>

Exemples :<br>
- ChronoUnit.DAYS<br>
- ChronoUnit.HOURS<br>
- ChronoUnit.MONTHS<br>
- ChronoUnit.YEARS<br><br>

Utilisé principalement avec <strong>between()</strong> pour calculer des différences.<br><br>

<strong>A), C), D) sont incorrects :</strong> Mauvaise catégorie.

## Question

Quelle affirmation sur ChronoUnit.between() est correcte ?<br><br>

A) Retourne toujours un nombre positif<br>
B) Retourne un long qui peut être négatif<br>
C) Retourne une Duration<br>
D) Lève une exception si le résultat est négatif

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>ChronoUnit.between(a, b)</strong> :<br>
- Retourne un <strong>long</strong><br>
- Peut être <strong>positif, zéro ou négatif</strong><br><br>

Calcul : <strong>b - a</strong> sur la ligne du temps<br><br>

Négatif signifie : date2 avant date1<br><br>

Exemple :<br>
ChronoUnit.DAYS.between(date1, date2);<br>
// Si résultat = -5 → date2 est 5 jours avant date1<br><br>

<strong>Piège OCP :</strong> Négatif = normal, pas un bug.<br><br>

<strong>A), C), D) sont incorrects :</strong> Mauvaise compréhension.

## Question

Pourquoi l'ancienne API Calendar utilisait-elle les mois à partir de 0 ?<br><br>

A) Pour optimiser la mémoire<br>
B) Héritage de conception C/Unix (erreur historique)<br>
C) Pour faciliter les calculs<br>
D) C'est plus logique

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

L'ancienne API Calendar utilisait les mois à partir de 0 par <strong>héritage de conception C/Unix</strong>.<br><br>

Problème :<br>
- Janvier = 0<br>
- Février = 1<br>
- ...<br>
- Décembre = 11<br><br>

C'était source de <strong>bugs constants</strong>.<br><br>

La nouvelle API (java.time) corrige ce problème :<br>
- Janvier = 1<br>
- Décembre = 12<br><br>

<strong>A), C), D) sont incorrects :</strong> C'était une erreur de conception.

## Question

Quelle API doit-on éviter dans le code moderne Java ?<br><br>

A) java.time<br>
B) java.util.Date et java.util.Calendar<br>
C) java.time.temporal<br>
D) java.time.format

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>À ÉVITER :</strong><br>
- java.util.Date<br>
- java.util.Calendar<br><br>

Raisons :<br>
- Mutable<br>
- Pas thread-safe<br>
- API confuse<br>
- Mois à partir de 0<br><br>

<strong>À UTILISER :</strong><br>
- java.time (LocalDate, ZonedDateTime, Instant, etc.)<br><br>

<strong>A), C), D) sont incorrects :</strong> Ce sont les nouvelles APIs recommandées.

## Question

Quel code est INCORRECT à cause de l'immutabilité ? (Piège OCP)<br><br>

A) date = date.plusDays(1);<br>
B) date.plusDays(1);<br>
C) LocalDate newDate = date.plusDays(1);<br>
D) date = date.withYear(2025);

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>INCORRECT :</strong> date.plusDays(1);<br><br>

Problème :<br>
- plusDays() retourne un <strong>nouvel objet</strong><br>
- Le résultat est <strong>perdu</strong> (non assigné)<br>
- date reste <strong>inchangée</strong><br><br>

<strong>Piège OCP majeur :</strong> Oublier d'assigner le résultat.<br><br>

<strong>A), C), D) sont corrects :</strong> Ils assignent le résultat.

## Question

Dans java.time, toutes les classes sont-elles immutables et thread-safe ?<br><br>

A) Oui, toutes sans exception<br>
B) Oui, les principales classes (LocalDate, Instant, ZonedDateTime, etc.)<br>
C) Non, aucune n'est thread-safe<br>
D) Seulement Instant est immutable

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Oui</strong>, les principales classes de java.time sont <strong>immutables</strong> et <strong>thread-safe</strong> :<br>
- LocalDate<br>
- LocalTime<br>
- LocalDateTime<br>
- ZonedDateTime<br>
- Instant<br>
- Duration<br>
- Period<br>
- DateTimeFormatter<br><br>

C'est un avantage majeur par rapport à l'ancienne API.<br><br>

<strong>A) est presque correct :</strong> Quelques rares exceptions existent.<br>
<strong>C) et D) sont incorrects :</strong> Faux.

## Question

Quel piège OCP concernant LocalDateTime est vrai ?<br><br>

A) LocalDateTime gère automatiquement les timezones<br>
B) LocalDateTime ne gère PAS les timezones<br>
C) LocalDateTime est mutable<br>
D) LocalDateTime peut être null par défaut

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Piège OCP majeur :</strong><br>
LocalDateTime ne gère PAS les timezones.<br><br>

Pour avoir une timezone, il faut utiliser <strong>ZonedDateTime</strong>.<br><br>

LocalDateTime représente une date-heure <strong>locale</strong> sans contexte géographique.<br><br>

<strong>A) est incorrect :</strong> C'est le piège classique.<br>
<strong>C) est incorrect :</strong> LocalDateTime est immutable.<br>
<strong>D) est incorrect :</strong> Pas de valeur par défaut null automatique.

## Question

Quelle méthode permet d'obtenir l'Instant correspondant au 1er janvier 1970 00:00:00 UTC ?<br><br>

A) Instant.epoch()<br>
B) Instant.ofEpochSecond(0)<br>
C) Instant.zero()<br>
D) new Instant(0)

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

La méthode correcte est <strong>Instant.ofEpochSecond(0)</strong>.<br><br>

Cela retourne le point de référence (epoch) :<br>
1970-01-01T00:00:00Z<br><br>

Autres exemples :<br>
- Instant.ofEpochMilli(1000) → +1 seconde<br>
- Instant.ofEpochSecond(86400) → +1 jour<br><br>

<strong>A), C), D) sont incorrects :</strong> Méthodes inexistantes.

## Question

Que représente Duration en Java ?<br><br>

A) Une quantité de temps basée sur années, mois et jours<br>
B) Une quantité de temps machine-scale basée sur secondes et nanosecondes<br>
C) Un intervalle de dates humaines<br>
D) Une timezone avec offset

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Duration</strong> représente une quantité de temps <strong>machine-scale</strong>.<br><br>

Basée sur :<br>
- <strong>Secondes</strong><br>
- <strong>Nanosecondes</strong><br><br>

Caractéristiques :<br>
- <strong>Exacte</strong><br>
- 1 jour = <strong>toujours 24h</strong><br>
- DST <strong>ignoré</strong><br><br>

Utilisée avec : Instant, calculs exacts, logs, systèmes, délais techniques.<br><br>

<strong>A) est incorrect :</strong> C'est Period.<br>
<strong>C) et D) sont incorrects :</strong> Mauvaise définition.

## Question

Que représente Period en Java ?<br><br>

A) Une durée exacte en secondes<br>
B) Une quantité de temps human-scale basée sur années, mois et jours<br>
C) Un intervalle de temps pour les systèmes<br>
D) Une période de 24 heures exactes

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Period</strong> représente une quantité de temps <strong>human-scale</strong>.<br><br>

Basée sur :<br>
- <strong>Années</strong><br>
- <strong>Mois</strong><br>
- <strong>Jours</strong><br><br>

Caractéristiques :<br>
- Dépend du <strong>calendrier</strong><br>
- DST <strong>pris en compte</strong><br>
- 1 jour peut ≠ 24h (à cause du DST)<br><br>

Utilisée avec : LocalDate, règles métier, dates humaines.<br><br>

<strong>A) et C) sont incorrects :</strong> C'est Duration.<br>
<strong>D) est incorrect :</strong> Period ne garantit pas 24h exactes.

## Question

Quelle est la différence principale entre Duration et Period ?<br><br>

A) Duration pour les dates, Period pour les heures<br>
B) Duration est machine-scale (secondes), Period est human-scale (années/mois/jours)<br>
C) Period est plus précis que Duration<br>
D) Il n'y a aucune différence

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Différence CLÉ (piège examen) :</strong><br><br>

<strong>Duration :</strong><br>
- Type : machine-scale<br>
- Unités : secondes, nanosecondes<br>
- DST : ❌ ignoré<br>
- 1 jour : toujours 24h<br><br>

<strong>Period :</strong><br>
- Type : human-scale<br>
- Unités : années, mois, jours<br>
- DST : ✅ pris en compte<br>
- 1 jour : peut ≠ 24h<br><br>

<strong>A), C), D) sont incorrects :</strong> Mauvaise compréhension de la différence.

## Question

Quel type doit-on utiliser pour calculer un timeout serveur de 30 secondes ?<br><br>

A) Period.ofSeconds(30)<br>
B) Duration.ofSeconds(30)<br>
C) LocalDateTime.plusSeconds(30)<br>
D) ChronoUnit.SECONDS

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Pour un <strong>calcul exact</strong> (timeout serveur), on utilise <strong>Duration</strong>.<br><br>

Exemple : Duration.ofSeconds(30)<br><br>

Raisons :<br>
- Mesure <strong>machine-scale</strong><br>
- Précision exacte en secondes/nanosecondes<br>
- Indépendant du calendrier et du DST<br><br>

<strong>A) est incorrect :</strong> Period n'a pas de méthode ofSeconds().<br>
<strong>C) est incorrect :</strong> LocalDateTime n'est pas une durée.<br>
<strong>D) est incorrect :</strong> ChronoUnit est une unité, pas une durée.

## Question

Quel type doit-on utiliser pour ajouter 1 mois à un abonnement client ?<br><br>

A) Duration.ofDays(30)<br>
B) Period.ofMonths(1)<br>
C) LocalDate.plusDays(30)<br>
D) ChronoUnit.MONTHS

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Pour une <strong>règle métier</strong> (abonnement + 1 mois), on utilise <strong>Period</strong>.<br><br>

Exemple : Period.ofMonths(1)<br><br>

Raisons :<br>
- Mesure <strong>human-scale</strong><br>
- Respecte le calendrier (mois de différentes longueurs)<br>
- Gère correctement les années bissextiles<br><br>

<strong>A) est incorrect :</strong> 1 mois ≠ 30 jours (février = 28/29 jours).<br>
<strong>C) est incorrect :</strong> Ajoute directement, ne représente pas une durée réutilisable.<br>
<strong>D) est incorrect :</strong> C'est une unité, pas une période.

## Question

Que signifie Duration.ofDays(1) ?<br><br>

A) Un jour calendaire humain<br>
B) Exactement 24 heures (86400 secondes)<br>
C) Un jour qui s'adapte au DST<br>
D) Un jour dans le fuseau horaire local

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Duration.ofDays(1)</strong> signifie <strong>exactement 24 heures</strong> (86400 secondes).<br><br>

Important :<br>
- <strong>Pas un jour humain</strong><br>
- <strong>Pas affecté par le DST</strong><br>
- Machine-scale, mesure exacte<br><br>

<strong>Piège OCP :</strong> Duration.ofDays(1) ≠ jour calendaire<br><br>

<strong>A) est incorrect :</strong> Pour un jour calendaire, utiliser Period.ofDays(1).<br>
<strong>C) et D) sont incorrects :</strong> Duration ignore le DST et les timezones.

## Question

Que retourne ChronoUnit.DAYS.between(date1, date2) ?<br><br>

A) Toujours un nombre positif<br>
B) Un long qui peut être positif, zéro ou négatif<br>
C) Une Duration<br>
D) Une Period

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>ChronoUnit.DAYS.between(a, b)</strong> retourne un <strong>long</strong> qui peut être :<br>
- Positif<br>
- Zéro<br>
- <strong>Négatif</strong><br><br>

Pourquoi ?<br>
between() calcule : <strong>b - a</strong> sur la ligne du temps<br><br>

<strong>Résultat négatif :</strong> le deuxième temporal est <strong>avant</strong> le premier.<br><br>

<strong>Piège OCP :</strong> résultat négatif = normal, pas un bug.<br><br>

<strong>A), C), D) sont incorrects :</strong> Retourne un long, pas toujours positif.

## Question

Pourquoi between() fonctionne-t-il avec LocalDate, LocalDateTime et Instant ?<br><br>

A) Ce sont tous des sous-classes de Date<br>
B) Ils implémentent tous l'interface Temporal<br>
C) Ils utilisent tous le même format<br>
D) Ils sont tous basés sur milliseconde

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>between()</strong> fonctionne car ces types implémentent l'interface <strong>Temporal</strong>.<br><br>

Types compatibles :<br>
- LocalDate<br>
- LocalDateTime<br>
- LocalTime<br>
- ZonedDateTime<br>
- Instant<br><br>

Tous peuvent être utilisés avec ChronoUnit.between().<br><br>

<strong>A) est incorrect :</strong> Ce ne sont pas des sous-classes de java.util.Date.<br>
<strong>C) et D) sont incorrects :</strong> Pas la raison de compatibilité.

## Question

Quel format de date est valide en ISO-8601 par défaut en Java ?<br><br>

A) 15/01/2024<br>
B) 2024-01-15<br>
C) 2024/01/15<br>
D) 2024-1-5

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Java utilise <strong>ISO-8601 strict</strong> par défaut.<br><br>

<strong>Exemples valides :</strong><br>
- 2024-01-15<br>
- 2024-01-15T14:30<br>
- 2024-01-15T14:30Z<br><br>

<strong>Exemples invalides :</strong><br>
- ❌ 2024-1-5 (zéros manquants)<br>
- ❌ 15/01/2024 (slashes)<br>
- ❌ 2024/01/15 (slashes)<br><br>

Java ne devine jamais, ne corrige jamais.<br><br>

<strong>A), C), D) sont incorrects :</strong> Formats non-ISO.

## Question

Que se passe-t-il à la compilation avec LocalDate.parse("15/01/2024") ?<br><br>

A) Erreur de compilation<br>
B) Compilation OK, exception à l'exécution<br>
C) Conversion automatique au format ISO<br>
D) Warning mais compilation OK

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Règle fondamentale de parse() :</strong><br>
- ✔️ Compilation → OK (String valide syntaxiquement)<br>
- ❌ Exécution → exception si format invalide<br><br>

Le compilateur ne vérifie PAS les valeurs des String.<br><br>

Pour "15/01/2024", il faudrait utiliser un DateTimeFormatter approprié.<br><br>

<strong>A) est incorrect :</strong> La compilation réussit.<br>
<strong>C) est incorrect :</strong> Java ne convertit jamais automatiquement.<br>
<strong>D) est incorrect :</strong> Pas de warning à la compilation.

## Question

Quel est le rôle de DateTimeFormatter ?<br><br>

A) Valider uniquement les dates<br>
B) Convertir objet ↔ String avec formats personnalisés<br>
C) Créer des objets date/time<br>
D) Calculer des durées

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>DateTimeFormatter</strong> permet de convertir :<br>
- Objet → String (<strong>format</strong>)<br>
- String → Objet (<strong>parse</strong>)<br><br>

Avantages :<br>
- Permet formats non ISO<br>
- <strong>Immutable</strong><br>
- <strong>Thread-safe</strong><br>
- Peut être réutilisé partout<br><br>

Bonne pratique OCP : un formatter = constante partagée.<br><br>

<strong>A), C), D) sont incorrects :</strong> Pas le rôle principal.

## Question

Quelle est la différence entre "MM" et "mm" dans un DateTimeFormatter ?<br><br>

A) Aucune différence<br>
B) MM = mois, mm = minutes<br>
C) MM = minutes, mm = mois<br>
D) Les deux représentent le mois

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>PIÈGE CLASSIQUE OCP :</strong><br><br>

<strong>MM</strong> = <strong>mois</strong> (Month)<br>
<strong>mm</strong> = <strong>minutes</strong> ❌ (attention au piège)<br><br>

Java est <strong>strictement sensible à la casse</strong>.<br><br>

Exemple :<br>
"yyyy-MM-dd" → année-mois-jour ✅<br>
"yyyy-mm-dd" → année-minutes-jour ❌ (erreur)<br><br>

<strong>A), C), D) sont incorrects :</strong> MM et mm sont différents.

## Question

Quelle est la différence entre "yyyy" et "YYYY" dans un DateTimeFormatter ?<br><br>

A) Aucune différence<br>
B) yyyy = année civile, YYYY = année de semaine<br>
C) YYYY = année civile, yyyy = année de semaine<br>
D) Les deux sont identiques en Java

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>PIÈGE TRÈS DANGEREUX OCP :</strong><br><br>

<strong>yyyy</strong> = <strong>année civile</strong> ✅ (2024, 2025...)<br>
<strong>YYYY</strong> = <strong>année de semaine</strong> ❌ (week year)<br><br>

<strong>Année de semaine :</strong> peut différer de l'année civile en début/fin d'année.<br><br>

Toujours utiliser <strong>yyyy</strong> pour les dates normales.<br><br>

<strong>A), C), D) sont incorrects :</strong> yyyy et YYYY sont très différents.

## Question

Quelle est la différence entre "dd" et "DD" dans un DateTimeFormatter ?<br><br>

A) dd = jour du mois, DD = jour de l'année<br>
B) DD = jour du mois, dd = jour de l'année<br>
C) Aucune différence<br>
D) Les deux sont invalides

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>Différence :</strong><br><br>

<strong>dd</strong> = <strong>jour du mois</strong> (01-31)<br>
<strong>DD</strong> = <strong>jour de l'année</strong> (001-365/366)<br><br>

Exemple :<br>
15 janvier 2024 :<br>
- dd = 15<br>
- DD = 015 (15ème jour de l'année)<br><br>

<strong>B), C), D) sont incorrects :</strong> Case sensitive est critique.

## Question

Quelle est la différence entre "HH" et "hh" dans un DateTimeFormatter ?<br><br>

A) HH = heure 1-12, hh = heure 0-23<br>
B) HH = heure 0-23, hh = heure 1-12 (AM/PM)<br>
C) Aucune différence<br>
D) Les deux sont pour les minutes

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Différence :</strong><br><br>

<strong>HH</strong> = heure <strong>0-23</strong> (format 24h)<br>
<strong>hh</strong> = heure <strong>1-12</strong> (format AM/PM)<br><br>

Pour utiliser hh, il faut aussi spécifier AM/PM avec le pattern 'a'.<br><br>

Exemple :<br>
"HH:mm" → 14:30<br>
"hh:mm a" → 02:30 PM<br><br>

<strong>A), C), D) sont incorrects :</strong> Mauvaise définition.

## Question

DateTimeFormatter est-il thread-safe ?<br><br>

A) Non, il faut le synchroniser<br>
B) Oui, car il est immutable<br>
C) Seulement si déclaré final<br>
D) Ça dépend du format utilisé

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>DateTimeFormatter</strong> est :<br>
- <strong>Immutable</strong><br>
- <strong>Thread-safe</strong><br><br>

Conséquences :<br>
- Peut être réutilisé partout<br>
- Peut être partagé entre threads<br>
- Pas besoin de synchronisation<br><br>

<strong>Bonne pratique :</strong> Déclarer comme constante static final.<br><br>

<strong>A), C), D) sont incorrects :</strong> Thread-safe par nature.

## Question

Quel format par défaut utilise LocalDate ?<br><br>

A) dd/MM/yyyy<br>
B) MM/dd/yyyy<br>
C) yyyy-MM-dd (ISO-8601)<br>
D) dd-MM-yyyy

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>LocalDate</strong> utilise par défaut le format <strong>ISO-8601</strong> :<br>
<strong>yyyy-MM-dd</strong><br><br>

Caractéristiques :<br>
- Date sans heure<br>
- Pas de fuseau horaire<br>
- Format standard international<br><br>

Exemple : 2024-02-04<br><br>

<strong>A), B), D) sont incorrects :</strong> Formats non-ISO.

## Question

Quelle méthode est plus sûre pour créer une date ?<br><br>

A) LocalDate.parse("2024-02-04")<br>
B) LocalDate.of(2024, 2, 4)<br>
C) Les deux sont équivalentes<br>
D) new LocalDate(2024, 2, 4)

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>À l'examen :</strong> of() est toujours plus sûre que parse().<br><br>

<strong>Différence :</strong><br><br>

<strong>of() :</strong><br>
- Données : nombres<br>
- Risque : ❌ aucun (vérifié à la compilation)<br><br>

<strong>parse() :</strong><br>
- Données : String<br>
- Risque : ⚠️ exception à l'exécution si format invalide<br><br>

<strong>A) et C) sont incorrects :</strong> parse() a plus de risques.<br>
<strong>D) est incorrect :</strong> Pas de constructeur public.

## Question

Que se passe-t-il avec ce code : LocalDate.parse("2024-1-5") ?<br><br>

A) Compilation OK, crée la date 5 janvier 2024<br>
B) Compilation OK, DateTimeParseException à l'exécution<br>
C) Erreur de compilation<br>
D) Warning mais fonctionne

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Le code compile mais lève <strong>DateTimeParseException</strong> à l'exécution.<br><br>

Raison :<br>
- Format attendu : yyyy-MM-dd (avec zéros)<br>
- Format fourni : yyyy-M-d (sans zéros)<br>
- Java ne devine pas, ne corrige pas<br><br>

<strong>Piège OCP :</strong> parse() accepte formats approximatifs → <strong>FAUX</strong><br><br>

<strong>A), C), D) sont incorrects :</strong> Exception à l'exécution.

## Question

Pour parser "15/01/2024", quel code est correct ?<br><br>

A) LocalDate.parse("15/01/2024")<br>
B) LocalDate.parse("15/01/2024", DateTimeFormatter.ofPattern("dd/MM/yyyy"))<br>
C) LocalDate.of(15, 1, 2024)<br>
D) new LocalDate("15/01/2024")

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Pour un format non-ISO, il faut <strong>créer un DateTimeFormatter</strong> :<br><br>

LocalDate.parse("15/01/2024", DateTimeFormatter.ofPattern("dd/MM/yyyy"))<br><br>

<strong>A) est incorrect :</strong> Format ISO attendu par défaut.<br>
<strong>C) est incorrect :</strong> Ordre des paramètres : of(année, mois, jour).<br>
<strong>D) est incorrect :</strong> Pas de constructeur String.

## Question

Lequel de ces énoncés est FAUX ? (Piège OCP)<br><br>

A) Duration.ofDays(1) représente un jour humain qui s'adapte au DST<br>
B) Period.ofMonths(1) représente 1 mois calendaire<br>
C) ChronoUnit.between() peut retourner un nombre négatif<br>
D) DateTimeFormatter est thread-safe

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>FAUX :</strong> Duration.ofDays(1) = jour humain → <strong>FAUX</strong><br><br>

<strong>Vérité :</strong><br>
Duration.ofDays(1) = <strong>exactement 24 heures</strong><br>
- Pas affecté par le DST<br>
- Machine-scale, pas human-scale<br><br>

<strong>Pièges OCP à retenir :</strong><br>
- ❌ Duration.ofDays(1) = jour humain<br>
- ❌ Period = secondes<br>
- ❌ MM = minutes<br>
- ❌ YYYY = année civile<br><br>

<strong>B), C), D) sont vrais.</strong>

## Question

Quel est le bon usage pour mesurer le temps d'exécution d'un processus système ?<br><br>

A) Period entre deux LocalDate<br>
B) Duration entre deux Instant<br>
C) ChronoUnit.DAYS.between() avec LocalDateTime<br>
D) Difference entre deux ZonedDateTime

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Pour mesurer le <strong>temps d'exécution</strong> d'un processus système :<br>
<strong>Duration entre deux Instant</strong><br><br>

Raisons :<br>
- Mesure <strong>exacte</strong> en nanosecondes<br>
- Machine-scale<br>
- Indépendant du calendrier et DST<br><br>

Exemple :<br>
Instant debut = Instant.now();<br>
// processus<br>
Instant fin = Instant.now();<br>
Duration duree = Duration.between(debut, fin);<br><br>

<strong>A), C), D) sont incorrects :</strong> Pas adaptés pour mesures exactes système.

## Question

Si ChronoUnit.DAYS.between(date2, date1) retourne -5, que signifie-t-il ?<br><br>

A) Il y a une erreur dans le code<br>
B) date1 est 5 jours après date2<br>
C) date1 est 5 jours avant date2<br>
D) Les dates sont invalides

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>between(a, b)</strong> calcule : <strong>b - a</strong><br><br>

Si between(date2, date1) = -5 :<br>
- date1 - date2 = -5<br>
- Donc date1 est <strong>5 jours avant</strong> date2<br>
- Ou : date2 est <strong>5 jours après</strong> date1<br><br>

<strong>Résultat négatif = normal</strong>, indique l'ordre temporel.<br><br>

<strong>Piège OCP :</strong> résultat négatif ≠ bug<br><br>

<strong>A), C), D) sont incorrects :</strong> Mauvaise interprétation du signe.

## Question

Qu'est-ce qu'une timezone en Java ?<br><br>

A) Un décalage horaire fixe par rapport à UTC<br>
B) Une définition qui inclut un offset UTC, des règles DST et un historique<br>
C) Une heure locale sans contexte géographique<br>
D) Un format d'affichage de l'heure

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Une <strong>timezone</strong> définit comment un Instant (UTC) est affiché localement.<br><br>

Elle inclut :<br>
• Un <strong>offset UTC</strong> (décalage)<br>
• Des <strong>règles de changement d'heure (DST)</strong><br>
• Un <strong>historique</strong> des changements<br><br>

Une timezone est intelligente et gère les variations automatiquement.<br><br>

<strong>A) est incorrect :</strong> Ça c'est un offset, pas une timezone complète.<br>
<strong>C) est incorrect :</strong> C'est LocalDateTime.<br>
<strong>D) est incorrect :</strong> C'est plus qu'un format d'affichage.

## Question

Que représente ZoneId en Java ?<br><br>

A) Un décalage horaire fixe comme +02:00<br>
B) Une timezone réelle géographique qui gère automatiquement le DST<br>
C) Un format de date et heure<br>
D) Une classe pour gérer uniquement UTC

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>ZoneId</strong> représente une timezone réelle (géographique).<br><br>

Exemples :<br>
• Europe/Paris<br>
• America/New_York<br><br>

Gère automatiquement :<br>
• Heure d'été / hiver (DST)<br>
• Changements historiques<br><br>

<strong>Différent d'un offset fixe</strong> (+02:00).<br><br>

<strong>A) est incorrect :</strong> Un offset fixe ne gère pas le DST.<br>
<strong>C) et D) sont incorrects :</strong> Mauvaise définition.

## Question

Que représente ZonedDateTime ?<br><br>

A) Une date sans heure<br>
B) Une date + heure + ZoneId (représentation humaine complète)<br>
C) Un point absolu dans le temps UTC<br>
D) Une heure locale sans timezone

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>ZonedDateTime</strong> représente :<br>
<strong>date + heure + ZoneId</strong><br><br>

Caractéristiques :<br>
• C'est la <strong>représentation humaine complète</strong> du temps<br>
• Basée sur le calendrier <strong>ISO-8601</strong><br>
• <strong>Immutable</strong> et <strong>thread-safe</strong><br><br>

Exemple : 2025-02-04T15:30:00+01:00[Europe/Paris]<br><br>

<strong>A) est incorrect :</strong> Contient date ET heure.<br>
<strong>C) est incorrect :</strong> C'est Instant.<br>
<strong>D) est incorrect :</strong> C'est LocalDateTime.

## Question

Qu'est-ce qu'Instant en Java ?<br><br>

A) Une heure locale avec timezone<br>
B) Un point absolu dans le temps (UTC), indépendant des fuseaux<br>
C) Une date sans heure<br>
D) Un offset horaire

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Instant</strong> représente un <strong>point absolu dans le temps (UTC)</strong>.<br><br>

Indépendant :<br>
• Des pays<br>
• Des fuseaux horaires<br>
• Du DST<br><br>

Sert de <strong>référence universelle</strong>.<br><br>

Exemple : nombre de secondes depuis le 1er janvier 1970 00:00:00 UTC (epoch).<br><br>

<strong>A) est incorrect :</strong> Instant n'a pas de timezone.<br>
<strong>C) et D) sont incorrects :</strong> Mauvaise définition.

## Question

Qu'est-ce que le DST (Daylight Saving Time) ?<br><br>

A) Un format de date standardisé<br>
B) Le passage entre heure d'été et heure d'hiver<br>
C) Un algorithme de cryptage temporel<br>
D) Une base de données de fuseaux horaires

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>DST (Daylight Saving Time)</strong> :<br>
• Passage heure d'été / heure d'hiver<br>
• Géré automatiquement par <strong>ZoneId</strong><br><br>

Important :<br>
• Les offsets fixes ne gèrent PAS le DST<br>
• Les ZoneId gèrent automatiquement le DST<br><br>

<strong>A), C), D) sont incorrects :</strong> Pas la bonne définition.

## Question

Quelle est la différence principale entre LocalDateTime et ZonedDateTime ?<br><br>

A) LocalDateTime est plus rapide<br>
B) LocalDateTime n'a pas de timezone ni DST, ZonedDateTime a les deux<br>
C) ZonedDateTime ne peut pas représenter de dates futures<br>
D) Il n'y a aucune différence

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Différence :</strong><br><br>

<strong>LocalDateTime :</strong><br>
• ❌ Pas de time zone<br>
• ❌ Pas de DST<br>
• = heure locale sans contexte<br><br>

<strong>ZonedDateTime :</strong><br>
• ✅ Time zone (ZoneId)<br>
• ✅ DST géré automatiquement<br>
• = heure humaine contextualisée<br><br>

<strong>A) est incorrect :</strong> La performance n'est pas la différence clé.<br>
<strong>C) est incorrect :</strong> ZonedDateTime peut représenter n'importe quelle date.<br>
<strong>D) est incorrect :</strong> Ce sont des types très différents.

## Question

Quelle est la différence entre un offset et un ZoneId ?<br><br>

A) Un offset gère le DST, un ZoneId non<br>
B) Un offset est figé, un ZoneId est intelligent et gère le DST<br>
C) Ce sont deux termes pour la même chose<br>
D) Un ZoneId est toujours en UTC

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Différence (piège majeur) :</strong><br><br>

<strong>Offset :</strong><br>
• Exemple : +02:00<br>
• ❌ Ne gère PAS le DST<br>
• Figé, statique<br><br>

<strong>ZoneId :</strong><br>
• Exemple : Europe/Paris<br>
• ✅ Gère le DST automatiquement<br>
• Intelligent, dynamique<br><br>

Un offset est figé, une zone est intelligente.<br><br>

<strong>A) est incorrect :</strong> C'est l'inverse.<br>
<strong>C) et D) sont incorrects :</strong> Concepts différents.

## Question

Quelle relation existe entre Instant et ZonedDateTime ?<br><br>

A) Ce sont deux types incompatibles<br>
B) Un ZonedDateTime = un Instant + un ZoneId<br>
C) Instant est obsolète, on utilise ZonedDateTime<br>
D) ZonedDateTime ne peut pas être converti en Instant

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Lien fondamental :</strong><br>
<strong>Un ZonedDateTime = un Instant + un ZoneId</strong><br><br>

Conséquences :<br>
• Même instant → affichages différents selon la zone<br>
• Conversion possible dans les deux sens<br><br>

Exemple :<br>
Instant : 2025-02-04T14:30:00Z<br>
+ Europe/Paris → 2025-02-04T15:30:00+01:00[Europe/Paris]<br>
+ America/New_York → 2025-02-04T09:30:00-05:00[America/New_York]<br><br>

<strong>A), C), D) sont incorrects :</strong> Fausse compréhension de la relation.

## Question

Qu'est-ce que le "Gap DST" (heure inexistante) ?<br><br>

A) Une erreur de programmation<br>
B) Une heure qui n'existe pas lors du passage à l'heure d'été<br>
C) Un bug dans ZoneId<br>
D) Une heure qui existe deux fois

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Gap DST (heure inexistante)</strong> se produit lors du passage à l'heure d'été.<br><br>

Exemple (Europe/Paris) :<br>
01:59 → 03:00<br><br>

Une heure comme <strong>02:30 n'existe pas</strong>.<br><br>

Java ajuste automatiquement vers une heure valide.<br><br>

C'est un problème critique à comprendre pour l'examen.<br><br>

<strong>A) et C) sont incorrects :</strong> C'est un comportement normal du DST.<br>
<strong>D) est incorrect :</strong> C'est l'ambiguïté DST, pas le gap.

## Question

Qu'est-ce que l'"Ambiguïté DST" (heure répétée) ?<br><br>

A) Deux fuseaux horaires identiques<br>
B) Une même heure locale qui existe deux fois lors du passage à l'heure d'hiver<br>
C) Une erreur de calcul de Java<br>
D) Un format de date ambigu

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Ambiguïté DST (heure répétée)</strong> se produit lors du passage à l'heure d'hiver.<br><br>

Problème :<br>
• Une même heure locale <strong>existe deux fois</strong><br>
• Java doit choisir un offset<br>
• <strong>Piège classique à l'examen</strong><br><br>

Exemple :<br>
À 3h du matin, on recule à 2h.<br>
Donc 2h30 existe deux fois cette nuit-là.<br><br>

<strong>A), C), D) sont incorrects :</strong> Mauvaise définition.

## Question

Quelle est la conversion correcte entre time zones ?<br><br>

A) Garder l'heure locale mais changer la zone<br>
B) Changer la zone sans changer l'instant (résultat : heure différente, instant identique)<br>
C) Ajouter l'offset manuellement<br>
D) Convertir d'abord en String puis parser

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Conversion correcte (même instant) :</strong><br>
• Changer la zone <strong>sans changer l'instant</strong><br>
• Résultat : heure différente, instant identique<br><br>

Exemple :<br>
15:00 Europe/Paris → 09:00 America/New_York<br>
(même moment, affichage différent)<br><br>

<strong>Erreur classique :</strong><br>
• Garder l'heure locale mais changer la zone<br>
• Cela change l'instant (souvent faux en métier)<br><br>

<strong>A) est incorrect :</strong> C'est l'erreur classique.<br>
<strong>C) et D) sont incorrects :</strong> Pas la bonne approche.

## Question

Que se passe-t-il si on crée un ZonedDateTime avec une heure dans le gap DST ?<br><br>

A) Une exception est levée<br>
B) Java ajuste automatiquement vers une heure valide<br>
C) La création échoue silencieusement<br>
D) L'heure reste exactement comme demandée

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Lors d'un <strong>gap DST</strong> (heure inexistante) :<br>
Java <strong>ajuste automatiquement</strong> vers une heure valide.<br><br>

Exemple :<br>
Si vous essayez de créer 02:30 lors du passage à l'heure d'été,<br>
Java va créer 03:30 à la place.<br><br>

Pas d'exception, <strong>ajustement automatique</strong>.<br><br>

<strong>A) est incorrect :</strong> Pas d'exception levée.<br>
<strong>C) et D) sont incorrects :</strong> L'heure est ajustée.

## Question

Quel type doit-on utiliser pour représenter un rendez-vous à Paris le 15 mars 2025 à 14h30 ?<br><br>

A) LocalDateTime<br>
B) Instant<br>
C) ZonedDateTime avec Europe/Paris<br>
D) OffsetDateTime avec +01:00

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

Pour un <strong>rendez-vous géographique</strong>, il faut <strong>ZonedDateTime</strong> avec la zone appropriée.<br><br>

Raisons :<br>
• Le rendez-vous a un <strong>contexte géographique</strong> (Paris)<br>
• Il faut gérer le <strong>DST</strong> automatiquement<br>
• Europe/Paris s'ajustera si le DST change<br><br>

<strong>A) est incorrect :</strong> Pas de timezone = ambigu.<br>
<strong>B) est incorrect :</strong> Instant est pour les points absolus, pas les rendez-vous humains.<br>
<strong>D) est incorrect :</strong> Un offset fixe ne gère pas le DST.

## Question

Quel type doit-on utiliser pour enregistrer le moment exact d'un événement système (log) ?<br><br>

A) LocalDateTime<br>
B) Instant<br>
C) ZonedDateTime<br>
D) LocalTime

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Pour un <strong>événement système</strong> (log, timestamp), il faut <strong>Instant</strong>.<br><br>

Raisons :<br>
• Point absolu dans le temps<br>
• Indépendant des fuseaux horaires<br>
• Référence universelle<br>
• Pas d'ambiguïté avec DST<br><br>

<strong>A) et C) sont incorrects :</strong> Dépendent d'une timezone ou localité.<br>
<strong>D) est incorrect :</strong> Pas de date, seulement l'heure.

## Question

Comment convertir correctement un ZonedDateTime de Paris vers New York ?<br><br>

A) zdtParis.withZoneSameLocal(ZoneId.of("America/New_York"))<br>
B) zdtParis.withZoneSameInstant(ZoneId.of("America/New_York"))<br>
C) zdtParis.plusHours(-6)<br>
D) Créer un nouveau ZonedDateTime avec les mêmes valeurs

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

La méthode correcte est <strong>withZoneSameInstant()</strong>.<br><br>

Cette méthode :<br>
• Garde le <strong>même instant</strong><br>
• Change l'affichage selon la nouvelle zone<br>
• Résultat : heure différente, instant identique<br><br>

<strong>A) est incorrect :</strong> withZoneSameLocal() garde l'heure locale mais change l'instant (erreur classique).<br>
<strong>C) est incorrect :</strong> Calcul manuel imprécis (et le décalage n'est pas toujours -6).<br>
<strong>D) est incorrect :</strong> Trop complexe et source d'erreurs.

## Question

Que représente ISO-8601 ?<br><br>

A) Un algorithme de cryptage<br>
B) Un standard international de représentation des dates et heures<br>
C) Une bibliothèque Java pour les dates<br>
D) Un fuseau horaire particulier

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>ISO-8601</strong> est un <strong>standard international</strong> de représentation des dates et heures.<br><br>

Format typique :<br>
2025-02-04T15:30:00+01:00[Europe/Paris]<br><br>

Java utilise ce standard pour :<br>
• ZonedDateTime<br>
• LocalDateTime<br>
• Instant<br>
• Tous les types temporels modernes<br><br>

<strong>A), C), D) sont incorrects :</strong> Pas la bonne définition.

## Question

Que signifie "immutable" pour ZonedDateTime et Instant ?<br><br>

A) Ces objets peuvent être modifiés à tout moment<br>
B) Une fois créés, ces objets ne peuvent pas être modifiés<br>
C) Ils sont stockés en mémoire permanente<br>
D) Ils ne peuvent pas être copiés

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Immutable</strong> signifie : une fois créés, ces objets <strong>ne peuvent pas être modifiés</strong>.<br><br>

Conséquences :<br>
• Toute opération retourne un <strong>nouvel objet</strong><br>
• L'objet original reste inchangé<br>
• <strong>Thread-safe</strong> par nature<br><br>

Exemple :<br>
ZonedDateTime zdt = ...<br>
ZonedDateTime nouveau = zdt.plusHours(2); // nouveau objet<br>
// zdt reste inchangé<br><br>

<strong>A), C), D) sont incorrects :</strong> Mauvaise définition d'immutable.

## Question

Pourquoi dit-on que ZonedDateTime et Instant sont "thread-safe" ?<br><br>

A) Parce qu'ils utilisent des locks internes<br>
B) Parce qu'ils sont immutables, donc plusieurs threads peuvent les lire sans risque<br>
C) Parce qu'ils sont synchronisés automatiquement<br>
D) Ils ne sont pas thread-safe

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Ces classes sont <strong>thread-safe</strong> car elles sont <strong>immutables</strong>.<br><br>

Explication :<br>
• Aucune modification possible<br>
• Plusieurs threads peuvent lire <strong>sans risque</strong><br>
• Pas besoin de synchronisation<br>
• Pas de locks nécessaires<br><br>

L'immutabilité garantit naturellement la thread-safety.<br><br>

<strong>A) et C) sont incorrects :</strong> Pas besoin de locks ou synchronisation.<br>
<strong>D) est incorrect :</strong> Ils sont bien thread-safe.

## Question

Quelle méthode permet d'obtenir l'Instant actuel ?<br><br>

A) Instant.getCurrentInstant()<br>
B) Instant.now()<br>
C) ZonedDateTime.toInstant()<br>
D) System.currentTimeMillis()

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

La méthode pour obtenir l'instant actuel est <strong>Instant.now()</strong>.<br><br>

Cette méthode retourne le point actuel dans le temps (UTC).<br><br>

Exemple :<br>
Instant maintenant = Instant.now();<br><br>

<strong>A) est incorrect :</strong> Cette méthode n'existe pas.<br>
<strong>C) est incorrect :</strong> C'est pour convertir un ZonedDateTime existant.<br>
<strong>D) est incorrect :</strong> Retourne un long, pas un Instant (ancienne API).

## Question

Comment créer un ZonedDateTime pour "maintenant" à Paris ?<br><br>

A) new ZonedDateTime("Europe/Paris")<br>
B) ZonedDateTime.now(ZoneId.of("Europe/Paris"))<br>
C) ZonedDateTime.of("Europe/Paris")<br>
D) Instant.now().atZone("Europe/Paris")

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

La méthode correcte est <strong>ZonedDateTime.now(ZoneId.of("Europe/Paris"))</strong>.<br><br>

Cette méthode :<br>
• Obtient l'instant actuel<br>
• L'affiche dans la zone spécifiée<br><br>

<strong>A) est incorrect :</strong> Pas de constructeur public.<br>
<strong>C) est incorrect :</strong> of() nécessite date et heure complètes.<br>
<strong>D) est incorrect :</strong> Syntaxe incorrecte (atZone prend un ZoneId, pas un String).

## Question

Que se passe-t-il lors d'une conversion de ZonedDateTime vers Instant ?<br><br>

A) On perd l'information de timezone mais on garde le point exact dans le temps<br>
B) On perd le point exact dans le temps<br>
C) Rien ne change, ce sont des types équivalents<br>
D) La conversion est impossible

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

Lors de la conversion <strong>ZonedDateTime → Instant</strong> :<br>
• On <strong>perd l'information de timezone</strong><br>
• On <strong>garde le point exact dans le temps</strong><br><br>

Exemple :<br>
ZonedDateTime zdt = ... // 15:00+01:00[Europe/Paris]<br>
Instant instant = zdt.toInstant(); // 14:00:00Z (UTC)<br><br>

Le moment est identique, mais la représentation est en UTC sans timezone.<br><br>

<strong>B), C), D) sont incorrects :</strong> Mauvaise compréhension de la conversion.
