## Question

Quel écosystème Java est principalement destiné aux applications d'entreprise traditionnelles (serveurs, transactions, sécurité) ?<br><br>

A) Java SE<br>
B) Java ME<br>
C) Java EE<br>
D) Java Card

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>Java EE</strong> (désormais <strong>Jakarta EE</strong>) est conçu pour les applications d'entreprise, avec :<br>
- gestion des transactions<br>
- persistance<br>
- sécurité<br><br>

<strong>Java SE</strong> : base standard du langage.<br>
<strong>Java ME</strong> : systèmes embarqués.<br>
<strong>Java Card</strong> : cartes à puce.

## Question

Quelle affirmation décrit le mieux le principe "Write Once Run Anywhere" de Java ?<br><br>

A) Le code source Java peut s'exécuter directement sur n'importe quel processeur<br>
B) Le bytecode Java peut s'exécuter sur n'importe quelle machine disposant d'une JVM<br>
C) Le compilateur javac produit du code machine universel<br>
D) La JVM traduit le code Java en langage machine avant la compilation

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Le principe "Write Once Run Anywhere" signifie que le <strong>bytecode</strong> généré par la compilation peut s'exécuter sur n'importe quelle plateforme disposant d'une <strong>JVM</strong>.<br><br>

<strong>A) est incorrect :</strong> Le code source doit d'abord être compilé en bytecode.<br>
<strong>C) est incorrect :</strong> Le compilateur produit du bytecode, pas du code machine.<br>
<strong>D) est incorrect :</strong> C'est la JVM qui traduit le bytecode pendant l'exécution, pas avant la compilation.

## Question

Quelle est la différence entre une classe et un objet en Java ?<br><br>

A) Une classe est un objet compilé<br>
B) Une classe est un modèle, un objet est une instance créée en mémoire<br>
C) Un objet est une classe qui possède la méthode main()<br>
D) Il n'y a pas de différence, ce sont deux termes pour la même chose

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Une <strong>classe</strong> est un <strong>blueprint (modèle)</strong> qui définit des attributs et méthodes. Un <strong>objet</strong> est une <strong>instance</strong> de cette classe, créée en mémoire à runtime.<br><br>

Exemple :<br>
<strong>Class Car</strong> = le plan du jouet<br>
<strong>Car myCar = new Car()</strong> = le jouet réel en main<br><br>

<strong>A) est incorrect :</strong> La compilation produit du bytecode, pas des objets.<br>
<strong>C) est incorrect :</strong> La méthode main() n'a rien à voir avec la définition objet/classe.<br>
<strong>D) est incorrect :</strong> Ce sont deux concepts distincts et fondamentaux.

## Question

Que contient le JDK ? (Sélectionnez toutes les réponses correctes)<br><br>

A) Le compilateur javac<br>
B) La JVM<br>
C) Des outils de développement<br>
D) Un éditeur de code source

## Réponse

<strong>Réponse correcte :</strong> A), B), C)<br><br>

Le <strong>JDK (Java Development Kit)</strong> contient :<br>
- Le compilateur <strong>javac</strong><br>
- La <strong>JVM</strong><br>
- Des <strong>outils de développement</strong> (debugger, javadoc, etc.)<br><br>

<strong>D) est incorrect :</strong> Le JDK ne contient pas d'éditeur de code (IDE). Vous devez utiliser un outil externe comme IntelliJ, Eclipse, ou VS Code.

## Question

Que contient le JRE ?<br><br>

A) Uniquement la JVM<br>
B) La JVM et le compilateur javac<br>
C) La JVM et des bibliothèques Java compilées en bytecode<br>
D) Le code source des bibliothèques Java standard

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

Le <strong>JRE (Java Runtime Environment)</strong> contient :<br>
- La <strong>JVM</strong><br>
- Des <strong>bibliothèques Java déjà compilées en bytecode</strong> (System, String, Math, etc.)<br><br>

<strong>A) est incorrect :</strong> Le JRE contient aussi les bibliothèques standard.<br>
<strong>B) est incorrect :</strong> Le compilateur javac est dans le JDK, pas le JRE.<br>
<strong>D) est incorrect :</strong> Les bibliothèques sont en bytecode (.class), pas en code source.

## Question

Qu'est-ce que la JVM ?<br><br>

A) Un compilateur qui transforme Java en code machine<br>
B) Un programme logiciel qui exécute du bytecode Java<br>
C) Un langage de programmation<br>
D) Un processeur physique optimisé pour Java

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

La <strong>JVM (Java Virtual Machine)</strong> est un <strong>programme logiciel</strong> qui exécute du bytecode Java. C'est un programme comme Chrome, VS Code, ou Spotify.<br><br>

La JVM :<br>
- Lit le bytecode<br>
- Le traduit en instructions pour le processeur<br>
- Gère la mémoire<br><br>

<strong>A) est incorrect :</strong> C'est javac qui compile, la JVM exécute.<br>
<strong>C) est incorrect :</strong> Java est le langage, la JVM est l'environnement d'exécution.<br>
<strong>D) est incorrect :</strong> C'est du logiciel, pas du matériel.

## Question

Quand dit-on qu'un programme est à "runtime" ?<br><br>

A) Pendant la compilation du code source<br>
B) Pendant l'écriture du code dans l'IDE<br>
C) Pendant l'exécution du programme par la JVM<br>
D) Pendant la création du fichier .class

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

Le <strong>runtime</strong> est la phase d'<strong>exécution</strong> du programme, après le démarrage. À runtime :<br>
- Les objets sont créés en mémoire<br>
- Les méthodes sont appelées<br>
- Les erreurs <strong>RuntimeException</strong> peuvent apparaître<br><br>

Opposé à <strong>compile-time</strong> (moment de la compilation).<br><br>

<strong>A) et D) sont incorrects :</strong> C'est le compile-time.<br>
<strong>B) est incorrect :</strong> L'écriture du code précède la compilation et l'exécution.

## Question

Quelle affirmation est correcte concernant les erreurs en Java ?<br><br>

A) Les NullPointerException surviennent au compile-time<br>
B) Les erreurs de syntaxe surviennent au runtime<br>
C) Les erreurs de types sont détectées au compile-time<br>
D) Toutes les erreurs sont détectées avant l'exécution

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

Au <strong>compile-time</strong> :<br>
- Erreurs de syntaxe<br>
- Vérification des types<br>
- Pas d'objets en mémoire<br><br>

Au <strong>runtime</strong> :<br>
- <strong>NullPointerException</strong><br>
- Objets en mémoire<br>
- Valeurs réelles<br><br>

<strong>A) est incorrect :</strong> NullPointerException est une erreur runtime.<br>
<strong>B) est incorrect :</strong> Les erreurs de syntaxe sont détectées au compile-time.<br>
<strong>D) est incorrect :</strong> De nombreuses erreurs n'apparaissent qu'au runtime.

## Question

Que sont les bibliothèques Java incluses dans le JRE ?<br><br>

A) Du code source Java écrit par l'utilisateur<br>
B) Des classes Java déjà compilées en bytecode, fournies par Java<br>
C) Des fichiers exécutables .exe<br>
D) Du code machine spécifique à chaque processeur

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Les <strong>bibliothèques Java standard</strong> sont :<br>
- Des classes déjà écrites par les développeurs Java<br>
- Déjà compilées en <strong>bytecode</strong> (.class)<br>
- Exemples : System, String, Math, List<br><br>

Quand vous écrivez <strong>System.out.println()</strong>, vous utilisez une bibliothèque standard fournie par Java.<br><br>

<strong>A) est incorrect :</strong> Ce n'est pas votre code.<br>
<strong>C) est incorrect :</strong> C'est du bytecode, pas des exécutables.<br>
<strong>D) est incorrect :</strong> C'est du bytecode portable, pas du code machine.

## Question

À quel moment le processeur intervient-il dans l'exécution d'un programme Java ?<br><br>

A) Pendant l'écriture du code source<br>
B) Pendant la compilation Java vers bytecode<br>
C) Uniquement quand la JVM exécute le bytecode<br>
D) Le processeur exécute directement le bytecode Java

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

Le processeur intervient <strong>uniquement quand la JVM est en train d'exécuter le programme</strong>.<br><br>

Flux complet :<br>
- Écriture du code → <strong>pas de processeur</strong><br>
- Compilation (javac) → processeur exécute javac, <strong>pas votre programme</strong><br>
- Exécution (java) → <strong>la JVM démarre</strong> → <strong>la JVM donne du travail au processeur</strong><br><br>

Image mentale :<br>
Ton programme Java → JVM → Processeur<br><br>

<strong>D) est incorrect :</strong> Le processeur n'exécute jamais directement le bytecode, il exécute la JVM.

## Question

Quelle est la structure organisationnelle de Java du plus petit au plus grand ?<br><br>

A) Module → Package → Classe<br>
B) Classe → Package → Module<br>
C) Package → Classe → Module<br>
D) Classe → Module → Package

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Structure hiérarchique de Java :<br>
- <strong>Classe</strong> : unité de base (blueprint)<br>
- <strong>Package</strong> : groupe de classes<br>
- <strong>Module</strong> : groupe de packages<br><br>

Analogie :<br>
Classe = fichier<br>
Package = dossier<br>
Module = projet<br><br>

<strong>A), C), D) sont incorrects :</strong> L'ordre est inversé ou mélangé.

## Question

Pourquoi Eclipse Temurin est-il recommandé pour apprendre Java 21 ?<br><br>

A) C'est le seul JDK compatible avec Java 21<br>
B) C'est un OpenJDK avec support long terme, stable et gratuit<br>
C) Il contient des fonctionnalités exclusives absentes des autres JDK<br>
D) Il permet la compilation native contrairement aux autres

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Eclipse Temurin</strong> est recommandé car :<br>
- Basé sur <strong>OpenJDK</strong><br>
- <strong>Support long terme</strong><br>
- Très utilisé en entreprise<br>
- <strong>Stable et gratuit</strong><br>
- Choix par défaut pour l'apprentissage<br><br>

<strong>A) est incorrect :</strong> Plusieurs JDK sont compatibles avec Java 21.<br>
<strong>C) est incorrect :</strong> Tous les JDK respectent la même spécification Java.<br>
<strong>D) est incorrect :</strong> C'est GraalVM qui offre la compilation native.

## Question

Qu'est-ce que JAVA_HOME ?<br><br>

A) Le répertoire d'installation de tous les programmes Java<br>
B) Une variable d'environnement contenant le chemin vers le JDK actif<br>
C) Un fichier de configuration du PATH système<br>
D) Le dossier de stockage des fichiers .class compilés

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>JAVA_HOME</strong> est une <strong>variable d'environnement</strong> qui contient le chemin vers le JDK actif.<br><br>

Exemple :<br>
/Library/Java/JavaVirtualMachines/temurin-21.jdk/Contents/Home<br><br>

Importance :<br>
- Maven, Gradle, IDE l'utilisent<br>
- Source de vérité pour les outils<br>
- Évite les conflits de versions<br><br>

<strong>A) est incorrect :</strong> C'est le chemin vers UN JDK spécifique.<br>
<strong>C) est incorrect :</strong> C'est une variable, pas un fichier.<br>
<strong>D) est incorrect :</strong> Ce n'est pas un dossier de sortie de compilation.

## Question

Pourquoi est-il important de définir JAVA_HOME ?<br><br>

A) Pour que Java puisse compiler le code<br>
B) Pour que les outils (Maven, Gradle, IDE) sachent quel JDK utiliser<br>
C) Pour accélérer la compilation du bytecode<br>
D) C'est optionnel, le PATH suffit toujours

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>JAVA_HOME est crucial</strong> car de nombreux outils en dépendent :<br>
- Maven<br>
- Gradle<br>
- IntelliJ<br>
- Serveurs (Tomcat, Spring Boot)<br><br>

Sans JAVA_HOME :<br>
- Conflits de versions<br>
- Outils qui ne trouvent pas le bon JDK<br>
- Erreurs imprévisibles<br><br>

Règle d'or : <strong>JAVA_HOME = la source de vérité</strong><br><br>

<strong>A) est incorrect :</strong> Le compilateur peut fonctionner sans, mais les outils ont besoin de JAVA_HOME.<br>
<strong>C) est incorrect :</strong> Ça n'affecte pas les performances.<br>
<strong>D) est incorrect :</strong> JAVA_HOME est indispensable pour les outils professionnels.

## Question

Que fait la commande `/usr/libexec/java_home -v 21` sur macOS ?<br><br>

A) Elle installe Java 21<br>
B) Elle trouve et retourne le chemin exact du JDK 21 installé<br>
C) Elle compile un programme Java avec la version 21<br>
D) Elle supprime toutes les versions de Java sauf la 21

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Cette commande :<br>
- <strong>Trouve</strong> le JDK 21 parmi les JDK installés<br>
- <strong>Retourne le chemin exact</strong> du JDK<br>
- Évite les erreurs manuelles<br>
- C'est la méthode <strong>officielle Apple</strong><br><br>

Utilisation typique :<br>
export JAVA_HOME=$(/usr/libexec/java_home -v 21)<br><br>

<strong>A) est incorrect :</strong> Elle ne fait que trouver, pas installer.<br>
<strong>C) est incorrect :</strong> Ce n'est pas une commande de compilation.<br>
<strong>D) est incorrect :</strong> Elle ne modifie pas les installations.

## Question

Pourquoi modifie-t-on le PATH avec `export PATH=$JAVA_HOME/bin:$PATH` ?<br><br>

A) Pour installer Java dans un nouveau répertoire<br>
B) Pour que les commandes java et javac utilisent le Java du JAVA_HOME<br>
C) Pour compiler plus rapidement<br>
D) Pour permettre l'exécution de programmes sans JVM

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Modifier le PATH avec <strong>$JAVA_HOME/bin</strong> permet de s'assurer que :<br>
- Les commandes <strong>java</strong> et <strong>javac</strong> utilisent le Java du JAVA_HOME<br>
- Pas un autre Java installé ailleurs<br>
- Cohérence totale<br><br>

Structure :<br>
JDK → JAVA_HOME (vérité centrale) → PATH → java/javac<br><br>

<strong>A) est incorrect :</strong> Le PATH ne modifie pas l'installation.<br>
<strong>C) est incorrect :</strong> Ça n'affecte pas les performances.<br>
<strong>D) est incorrect :</strong> La JVM reste nécessaire pour exécuter Java.

## Question

Quelle affirmation est vraie concernant les différentes distributions de JDK ?<br><br>

A) Chaque JDK implémente un dialecte différent de Java<br>
B) Tous les JDK respectent la même spécification Java standard<br>
C) Oracle JDK est le seul JDK certifié pour la production<br>
D) GraalVM est recommandé pour débuter avec Java

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Java est un <strong>langage standardisé</strong>. Tous les JDK doivent respecter la <strong>spec Java</strong>, donc :<br>
- Même comportement<br>
- Même API<br>
- Compatibilité garantie<br><br>

Distributions courantes :<br>
- Eclipse Temurin (recommandé)<br>
- Oracle JDK<br>
- Amazon Corretto<br>
- Azul Zulu<br><br>

<strong>A) est incorrect :</strong> Tous implémentent le même Java.<br>
<strong>C) est incorrect :</strong> Plusieurs JDK sont certifiés.<br>
<strong>D) est incorrect :</strong> GraalVM n'est pas pour débuter.

## Question

Quel est le point d'entrée d'un programme Java exécutable ?<br><br>

A) La première classe du fichier<br>
B) Le constructeur de la classe principale<br>
C) La méthode public static void main(String[] args)<br>
D) La méthode public void run()

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

Le point d'entrée d'un programme Java est la méthode :<br>
<strong>public static void main(String[] args)</strong><br><br>

Caractéristiques obligatoires :<br>
- <strong>public</strong> : accessible de partout<br>
- <strong>static</strong> : pas besoin d'instancier la classe<br>
- <strong>void</strong> : ne retourne rien<br>
- <strong>main</strong> : nom exact requis<br>
- <strong>String[] args</strong> : paramètres ligne de commande<br><br>

<strong>A) est incorrect :</strong> L'ordre des classes n'importe pas.<br>
<strong>B) est incorrect :</strong> Le constructeur n'est pas le point d'entrée.<br>
<strong>D) est incorrect :</strong> C'est pour les Runnable/Thread, pas le point d'entrée principal.

## Question

Quelle extension de fichier est produite par le compilateur javac ?<br><br>

A) .java<br>
B) .class<br>
C) .jar<br>
D) .exe

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Le compilateur <strong>javac</strong> compile le code source (.java) en <strong>bytecode</strong> (.class).<br><br>

Flux de compilation :<br>
Main.java → javac → Main.class<br><br>

Le fichier <strong>.class</strong> contient le bytecode Java qui peut être exécuté par n'importe quelle JVM.<br><br>

<strong>A) est incorrect :</strong> .java est le fichier source, pas la sortie de compilation.<br>
<strong>C) est incorrect :</strong> .jar est une archive contenant plusieurs .class, créée avec jar.<br>
<strong>D) est incorrect :</strong> Java ne produit pas de fichiers .exe natifs.

## Question

Pourquoi met-on la configuration de JAVA_HOME dans le fichier .zshrc (ou .bashrc) ?<br><br>

A) Pour compiler le code Java automatiquement<br>
B) Pour que JAVA_HOME soit défini automatiquement à chaque ouverture de terminal<br>
C) Pour installer Java au démarrage du système<br>
D) Pour partager JAVA_HOME avec d'autres utilisateurs

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Mettre la configuration dans <strong>.zshrc</strong> (ou .bashrc) permet :<br>
- Le shell lit ce fichier au démarrage<br>
- <strong>JAVA_HOME</strong> est défini automatiquement<br>
- Configuration <strong>persistante</strong> à chaque terminal<br>
- Pas besoin de redéfinir manuellement<br><br>

Exemple :<br>
export JAVA_HOME=$(/usr/libexec/java_home -v 21)<br>
export PATH=$JAVA_HOME/bin:$PATH<br><br>

<strong>A) est incorrect :</strong> Ce n'est pas pour la compilation automatique.<br>
<strong>C) est incorrect :</strong> Ça ne fait pas d'installation.<br>
<strong>D) est incorrect :</strong> C'est spécifique à l'utilisateur, pas partagé.

## Question

Quand une classe Java déclare un package, d'où doit-on lancer les commandes javac et java ?<br><br>

A) Depuis n'importe quel dossier du projet<br>
B) Depuis le dossier qui contient directement le fichier .java<br>
C) Depuis la racine du classpath, le dossier qui contient les packages<br>
D) Depuis le dossier parent du package déclaré

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>Règle fondamentale :</strong> Avec des packages, on compile et on exécute <strong>toujours depuis le dossier qui représente la racine du classpath</strong>, c'est-à-dire le dossier qui contient les packages.<br><br>

Jamais depuis un sous-dossier de package.<br><br>

<strong>A) est incorrect :</strong> La position doit être précisément la racine du classpath.<br>
<strong>B) est incorrect :</strong> Se placer dans le package lui-même cause des erreurs de résolution.<br>
<strong>D) est incorrect :</strong> C'est trop vague, il faut être exactement à la racine.

## Question

Soit la déclaration : `package primitive_types.foundation_ex_4_1;`<br>
Quel chemin de fichier Java attend-il pour trouver la classe compilée ?<br><br>

A) primitive_types/Classe.class<br>
B) foundation_ex_4_1/Classe.class<br>
C) primitive_types/foundation_ex_4_1/Classe.class<br>
D) Classe.class

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

Le <strong>package est un chemin logique</strong>. La déclaration :<br>
package primitive_types.foundation_ex_4_1;<br><br>

Signifie que Java s'attend à trouver la classe dans :<br>
<strong>primitive_types/foundation_ex_4_1/Classe.class</strong><br><br>

Le package n'est pas juste un nom, c'est une <strong>structure de répertoires obligatoire</strong>.<br><br>

<strong>A) et B) sont incorrects :</strong> Le chemin complet doit correspondre exactement au package.<br>
<strong>D) est incorrect :</strong> Sans package, la classe serait dans le package par défaut.

## Question

Qu'est-ce que le classpath ?<br><br>

A) Le chemin absolu vers le JDK installé<br>
B) Le point de départ à partir duquel Java cherche les classes<br>
C) Le dossier contenant les fichiers .java source<br>
D) Une variable d'environnement obligatoire pour compiler

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Le <strong>classpath</strong> est le <strong>point de départ</strong> à partir duquel Java cherche les classes.<br><br>

Par défaut :<br>
- javac et java utilisent le dossier courant (.) comme classpath<br>
- Le dossier courant DOIT être la racine des packages<br><br>

<strong>A) est incorrect :</strong> Ça c'est JAVA_HOME.<br>
<strong>C) est incorrect :</strong> Le classpath peut contenir des .class, pas seulement des .java.<br>
<strong>D) est incorrect :</strong> C'est optionnel, il y a une valeur par défaut (.).

## Question

Soit la structure suivante :<br>
```
src/
└── primitive_types/
    └── foundation_ex_4_1/
        ├── Customer.java
        └── ShopApp.java
```
<br>
Depuis quel dossier faut-il compiler ?<br><br>

A) Depuis primitive_types/<br>
B) Depuis foundation_ex_4_1/<br>
C) Depuis src/<br>
D) Depuis n'importe où si on spécifie le chemin complet

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

Il faut compiler <strong>depuis src/</strong> qui est la <strong>racine du classpath</strong>, le dossier qui contient les packages.<br><br>

Commande correcte :<br>
javac primitive_types/foundation_ex_4_1/*.java<br><br>

Ou :<br>
javac primitive_types/foundation_ex_4_1/ShopApp.java<br><br>

<strong>A) et B) sont incorrects :</strong> Se placer dans un sous-package cause des erreurs de résolution de classes.<br>
<strong>D) est incorrect :</strong> Le classpath doit être correctement positionné.

## Question

Avec la même structure, quelle commande exécute correctement ShopApp depuis src/ ?<br><br>

A) java ShopApp<br>
B) java primitive_types/foundation_ex_4_1/ShopApp<br>
C) java primitive_types.foundation_ex_4_1.ShopApp<br>
D) java foundation_ex_4_1.ShopApp

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

Pour exécuter, on utilise le <strong>nom qualifié complet</strong> (Fully Qualified Name) avec des <strong>points</strong> :<br>
java primitive_types.foundation_ex_4_1.ShopApp<br><br>

Toujours depuis <strong>src/</strong> (racine du classpath).<br><br>

<strong>A) est incorrect :</strong> Java ne trouve pas la classe sans le package complet.<br>
<strong>B) est incorrect :</strong> On utilise des points (.), pas des slashes (/).<br>
<strong>D) est incorrect :</strong> Le package complet est nécessaire.

## Question

Que se passe-t-il si on se place dans `foundation_ex_4_1/` et qu'on compile avec `javac ShopApp.java` ?<br><br>

A) La compilation réussit normalement<br>
B) Erreur : cannot find symbol class Customer<br>
C) La compilation réussit mais l'exécution échoue<br>
D) Java corrige automatiquement le classpath

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Erreur :</strong> cannot find symbol class Customer<br><br>

<strong>Pourquoi ?</strong><br>
Parce que Java pense que le classpath = foundation_ex_4_1<br><br>

Il cherche alors :<br>
foundation_ex_4_1/primitive_types/foundation_ex_4_1/ShopApp.class<br><br>

Ce chemin n'existe pas, donc Java ne trouve pas Customer.<br><br>

<strong>A) et C) sont incorrects :</strong> La compilation échoue immédiatement.<br>
<strong>D) est incorrect :</strong> Java ne devine ni ne corrige le classpath.

## Question

Comment Java cherche-t-il les classes dans les packages ?<br><br>

A) Il parcourt récursivement tous les dossiers du projet<br>
B) Il remonte automatiquement dans l'arborescence si nécessaire<br>
C) Il part uniquement du classpath et suit exactement le package déclaré<br>
D) Il utilise l'intelligence artificielle pour deviner l'emplacement

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>Point clé Oracle :</strong><br>
Java ne "remonte" ni ne "descend" dans les packages automatiquement.<br>
Il part <strong>uniquement du classpath</strong>.<br><br>

- Java ne devine pas<br>
- Java ne corrige pas<br>
- Java ne parcourt pas l'arborescence librement<br><br>

Il suit <strong>exactement</strong> le chemin indiqué par le package.<br><br>

<strong>A), B), D) sont incorrects :</strong> Java suit une règle stricte et prévisible.

## Question

Quelle est la différence principale entre un IDE et l'examen Oracle concernant le classpath ?<br><br>

A) Les IDE n'utilisent pas de classpath<br>
B) L'IDE gère le classpath automatiquement, l'examen demande un raisonnement manuel<br>
C) L'examen interdit l'utilisation du classpath<br>
D) Il n'y a aucune différence

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>IntelliJ / IDE :</strong><br>
- Gère le classpath automatiquement<br>
- Masque la complexité<br>
- Peut donner l'illusion que "tout marche"<br><br>

<strong>Examen Oracle :</strong><br>
- Raisonnement manuel obligatoire<br>
- Tu dois savoir où tu te places<br>
- Tu dois connaître le classpath<br>
- Tu dois comprendre comment Java cherche les classes<br><br>

<strong>A), C), D) sont incorrects :</strong> Les deux utilisent le classpath différemment.

## Question

Quelle commande compile correctement tous les fichiers Java dans un package depuis la racine ?<br><br>

A) javac *.java<br>
B) javac primitive_types/*.java<br>
C) javac primitive_types/foundation_ex_4_1/*.java<br>
D) javac -r primitive_types/

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

Depuis la racine (src/), la commande correcte est :<br>
<strong>javac primitive_types/foundation_ex_4_1/*.java</strong><br><br>

Cela compile tous les fichiers .java dans ce package spécifique.<br><br>

<strong>A) est incorrect :</strong> Ne compile que les fichiers dans le dossier courant, pas dans les packages.<br>
<strong>B) est incorrect :</strong> Ne descend pas dans les sous-packages.<br>
<strong>D) est incorrect :</strong> L'option -r n'existe pas pour javac.

## Question

Si ShopApp.java utilise la classe Customer.java du même package, faut-il spécifier Customer dans la commande javac ?<br><br>

A) Oui, il faut toujours compiler toutes les dépendances manuellement<br>
B) Non, javac trouve automatiquement Customer si on compile depuis la racine<br>
C) Seulement si Customer est dans un autre package<br>
D) Ça dépend de la version de Java utilisée

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Si on compile correctement depuis la racine :<br>
javac primitive_types/foundation_ex_4_1/ShopApp.java<br><br>

<strong>Java trouve automatiquement Customer</strong> car :<br>
- Même package<br>
- Classpath correctement positionné<br>
- javac résout automatiquement les dépendances dans le même package<br><br>

<strong>A) est incorrect :</strong> javac est intelligent pour les dépendances locales.<br>
<strong>C) est incorrect :</strong> C'est vrai dans le même package aussi.<br>
<strong>D) est incorrect :</strong> Ce comportement est standard depuis Java 1.0.

## Question

Que signifie "la racine du classpath" ?<br><br>

A) Le dossier d'installation du JDK<br>
B) Le dossier qui contient les packages, point de départ de Java pour chercher les classes<br>
C) Le dossier contenant le fichier Main.java<br>
D) Le dossier système /usr/bin/

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>La racine du classpath</strong> est le dossier qui contient les packages, et qui sert de <strong>point de départ</strong> pour que Java cherche les classes.<br><br>

Exemple :<br>
Si vous avez src/com/exemple/Main.java<br>
La racine du classpath est <strong>src/</strong><br><br>

C'est depuis ce dossier que vous devez compiler et exécuter.<br><br>

<strong>A) est incorrect :</strong> Ça c'est JAVA_HOME.<br>
<strong>C) est incorrect :</strong> C'est souvent dans un sous-package.<br>
<strong>D) est incorrect :</strong> Ça n'a rien à voir avec le classpath Java.

## Question

Quel symbole utilise-t-on pour séparer les packages lors de l'exécution d'une classe ?<br><br>

A) Le slash (/) comme dans les chemins de fichiers<br>
B) Le backslash (\) comme sous Windows<br>
C) Le point (.) comme dans le nom qualifié complet<br>
D) Le tiret (-) comme séparateur logique

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

Pour exécuter une classe, on utilise le <strong>nom qualifié complet (Fully Qualified Name)</strong> avec des <strong>points (.)</strong> :<br><br>

java com.exemple.Main<br><br>

<strong>Attention au piège :</strong><br>
- Compilation : javac com/exemple/Main.java (slash)<br>
- Exécution : java com.exemple.Main (points)<br><br>

<strong>A) est incorrect :</strong> Les slashes sont pour javac, pas java.<br>
<strong>B) et D) sont incorrects :</strong> Ces symboles ne sont jamais utilisés pour les packages.

## Question

Que se passe-t-il si le dossier physique ne correspond pas exactement au package déclaré ?<br><br>

A) Java corrige automatiquement le chemin<br>
B) La compilation échoue avec une erreur de package<br>
C) L'IDE affiche un warning mais ça compile<br>
D) Ça fonctionne si on spécifie l'option -classpath

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Si la structure de dossiers ne correspond pas <strong>exactement</strong> au package déclaré, la compilation échoue.<br><br>

Exemple d'erreur :<br>
<strong>class X is public, should be declared in a file named X.java</strong><br>
ou<br>
<strong>package declaration does not match directory structure</strong><br><br>

Java exige une <strong>correspondance stricte</strong> entre :<br>
- La déclaration package<br>
- La structure de répertoires<br><br>

<strong>A), C), D) sont incorrects :</strong> Aucune correction ou contournement possible.

## Question

Si on a : `package com.oracle.exam;` et qu'on compile depuis le dossier parent de com/, que cherche Java ?<br><br>

A) exam/Classe.class<br>
B) oracle/exam/Classe.class<br>
C) com/oracle/exam/Classe.class<br>
D) ../com/oracle/exam/Classe.class

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

Java cherche <strong>toujours</strong> le chemin complet correspondant au package depuis le classpath.<br><br>

Avec package com.oracle.exam;<br>
Java cherche : <strong>com/oracle/exam/Classe.class</strong><br><br>

Si vous êtes dans le bon dossier (celui qui contient com/), ça fonctionne.<br>
Sinon, erreur de résolution.<br><br>

<strong>A) et B) sont incorrects :</strong> Le package complet doit être respecté.<br>
<strong>D) est incorrect :</strong> Java n'utilise pas de chemins relatifs comme ../

## Question

Pourquoi l'erreur "cannot find symbol" apparaît-elle souvent avec les packages ?<br><br>

A) Le fichier .java n'existe pas<br>
B) On compile depuis un mauvais dossier, Java ne trouve pas la classe dans le classpath<br>
C) La classe n'a pas de méthode main()<br>
D) Le JDK n'est pas installé correctement

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>cannot find symbol</strong> avec les packages indique généralement qu'on compile depuis un <strong>mauvais dossier</strong>.<br><br>

Java cherche la classe en partant du classpath, mais :<br>
- Le classpath est mal positionné<br>
- La structure de packages ne correspond pas<br>
- On n'est pas à la racine des packages<br><br>

<strong>Solution :</strong> Se placer à la racine du classpath et recompiler.<br><br>

<strong>A), C), D) sont incorrects :</strong> Ces erreurs donnent des messages différents.

## Question

Quelle affirmation sur le package par défaut est correcte ?<br><br>

A) Toutes les classes doivent déclarer un package<br>
B) Les classes sans déclaration de package appartiennent au package par défaut<br>
C) Le package par défaut s'appelle "default"<br>
D) On ne peut pas compiler une classe sans package

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Les classes <strong>sans déclaration de package</strong> appartiennent au <strong>package par défaut (unnamed package)</strong>.<br><br>

Caractéristiques :<br>
- Pas de nom de package<br>
- Les classes sont directement à la racine<br>
- Limité : on ne peut pas importer ces classes dans d'autres packages<br>
- <strong>Déconseillé en production</strong><br><br>

<strong>A) et D) sont incorrects :</strong> Le package est optionnel.<br>
<strong>C) est incorrect :</strong> Il n'a pas de nom, c'est pour ça qu'on l'appelle "unnamed".

## Question

Soit deux classes : com.app.Main et com.util.Helper.<br>
Main peut-il utiliser Helper sans import ?<br><br>

A) Oui, car elles commencent toutes les deux par com<br>
B) Oui, si elles sont dans le même fichier<br>
C) Non, car elles sont dans des packages différents<br>
D) Oui, si Helper est public

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>Non</strong>, Main doit importer Helper car elles sont dans des <strong>packages différents</strong> :<br>
- com.app ≠ com.util<br><br>

Il faut ajouter :<br>
import com.util.Helper;<br><br>

<strong>Les packages doivent correspondre exactement.</strong> Partager un préfixe commun (com) ne suffit pas.<br><br>

<strong>A) est incorrect :</strong> Le package complet doit correspondre.<br>
<strong>B) est incorrect :</strong> On ne peut pas avoir deux classes publiques dans le même fichier.<br>
<strong>D) est incorrect :</strong> Public ne dispense pas de l'import.

## Question

Quelle commande spécifie explicitement le classpath à un dossier nommé "bin" ?<br><br>

A) javac -classpath bin Main.java<br>
B) javac -cp bin Main.java<br>
C) Les deux réponses A et B sont correctes<br>
D) javac -path bin Main.java

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

Les deux formes sont correctes et équivalentes :<br>
- <strong>javac -classpath bin Main.java</strong><br>
- <strong>javac -cp bin Main.java</strong><br><br>

<strong>-cp</strong> est juste une abréviation de <strong>-classpath</strong>.<br><br>

Cela indique à javac que le classpath est le dossier "bin" au lieu du dossier courant (.).<br><br>

<strong>D) est incorrect :</strong> L'option -path n'existe pas.

## Question

Si on a cette structure :<br>
```
project/
├── src/
│   └── com/app/Main.java
└── bin/
```
<br>
Comment compiler Main.java pour que le .class aille dans bin/ ?<br><br>

A) javac src/com/app/Main.java -d bin<br>
B) javac -d bin src/com/app/Main.java<br>
C) javac src/com/app/Main.java > bin<br>
D) A et B sont correctes

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

Les deux commandes sont correctes :<br>
- javac src/com/app/Main.java -d bin<br>
- javac -d bin src/com/app/Main.java<br><br>

L'option <strong>-d</strong> spécifie le <strong>dossier de destination</strong> pour les fichiers .class.<br><br>

Java créera automatiquement : bin/com/app/Main.class<br><br>

<strong>C) est incorrect :</strong> Le symbole > ne fonctionne pas pour javac.

## Question

What is the difference between the Interpreter and the JIT (Just-In-Time) compiler?

Please select 1 option

A) The Interpreter compiles the whole program before starting; the JIT does it during execution
B) The Interpreter reads bytecode line-by-line; the JIT compiles frequently used code into machine language
C) The Interpreter is used for .java files; the JIT is used for .class files
D) There is no difference; they are two names for the same process

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

The <strong>Interpreter</strong> starts immediately by reading and executing bytecode instruction by instruction (fast startup, slow execution). The <strong>JIT</strong> identifies "hot" code (frequently executed) and compiles it into <strong>native machine code</strong> for maximum performance.<br><br>

<strong>A) is incorrect:</strong> Java doesn't compile the whole program to machine code before starting.<br>
<strong>C) is incorrect:</strong> Both work on bytecode (.class) during execution.<br>
<strong>D) is incorrect:</strong> They are distinct mechanisms working together in the JVM.



## Question

In Object-Oriented Programming (OOP), what is the primary purpose of Encapsulation?

Please select 1 option

A) To make the code run on any operating system
B) To protect data and ensure consistency by controlling access through rules
C) To allow objects to inherit methods from a parent class
D) To transform a class into an object in memory

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Encapsulation</strong> is about <strong>protecting data</strong> and controlling modifications. Instead of allowing direct access to variables, we use methods (like getters/setters) to apply business rules.<br><br>

<strong>A) is incorrect:</strong> That's the "Write Once Run Anywhere" principle.<br>
<strong>C) is incorrect:</strong> That is the definition of Inheritance.<br>
<strong>D) is incorrect:</strong> That is called Instantiation.

## Question

Which concept allows a single method call to have different behaviors depending on the actual object being used at runtime?

Please select 1 option

A) Encapsulation
B) Compilation
C) Polymorphism
D) Build process

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>Polymorphism</strong> allows objects of different types to be treated as a common parent type, but execute their own specific behavior at <strong>runtime</strong>.<br><br>

Example: A <strong>Dog</strong> and a <strong>Cat</strong> both have a <code>makeSound()</code> method, but the result (Bark vs Meow) depends on the <strong>real object</strong>.<br><br>

<strong>A) is incorrect:</strong> Encapsulation is about data protection.<br>
<strong>B) and D) are incorrect:</strong> These are technical processes, not OOP principles.

## Question

What is the difference between "Compiling" and "Building" in Java?

Please select 1 option

A) Compiling is the overall process; Building is just javac
B) Compiling is the .java to .class transformation; Building is the complete process including packaging
C) They are exactly the same thing
D) Compiling creates a JAR; Building creates a .class file

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Compiling</strong> is the specific task of <strong>javac</strong> (.java → .class).<br>
<strong>Building</strong> is the <strong>global process</strong> (often managed by Maven, Gradle, or an IDE) that includes compiling, running tests, organizing files, and creating a JAR.<br><br>

<strong>A) and D) are reversed:</strong> javac is a part of the build, and the build produces the final JAR.

## Question

What does a JAR file typically contain?

Please select 1 option

A) The original .java source code files
B) The javac compiler and the JRE
C) Compiled .class files, resources, and a MANIFEST file
D) The installation files for the JDK

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

A <strong>JAR (Java ARchive)</strong> is a package used to distribute applications. It contains <strong>bytecode</strong> (.class), not source code, along with images, configuration files, and metadata (MANIFEST.MF).<br><br>

<strong>A) is incorrect:</strong> We deliver bytecode, not source code.<br>
<strong>B) and D) are incorrect:</strong> Tools like javac or the JDK are installed on the machine, not inside the application's JAR.

## Question

Which environment is specifically dedicated to "functional validation" where business rules are verified before going live?

Please select 1 option

A) DEV (Development)
B) REC (Recette / UAT)
C) PROD (Production)
D) JVM (Virtual Machine)

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

The <strong>REC (Recette)</strong> or <strong>UAT (User Acceptance Testing)</strong> environment is used to verify that the application meets the functional requirements before it reaches the end users.<br><br>

<strong>A) is incorrect:</strong> DEV is for writing and testing code by developers.<br>
<strong>C) is incorrect:</strong> PROD is for real users with real data.<br>
<strong>D) is incorrect:</strong> JVM is the technical execution environment, not a deployment stage.

## Question

What are "Program Arguments" in a Java application?

Please select 1 option

A) Configuration settings for the JVM memory (e.g., -Xmx)
B) The source code written inside the main method
C) Values passed by the user to the application at launch (String[] args)
D) The list of libraries imported in the class

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>Program arguments</strong> are the values you provide when launching the program (e.g., <code>java Main value1 value2</code>). They are stored in the <strong>String[] args</strong> array of the <code>main</code> method.<br><br>

<strong>A) is incorrect:</strong> Those are <strong>JVM Arguments</strong> (used to configure the machine, not the program logic).