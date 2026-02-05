# 📚 Ressources d'apprentissage

## 🧠 Notion Workspace

Mon workspace Notion centralise toute l'organisation de mon apprentissage Java SE 21.

### 📄 Study Tracker — Learning Stories
Suivi détaillé de chaque session d'apprentissage avec statut et progression.  
🔗 [Accéder au tracker](lien-study-tracker)

### 📊 Base de données Learning Stories
Database Notion avec toutes mes Learning Stories organisées par :
- **Module** : 0 à 11
- **Phase** : Fondations, Java SE 21, Exam Prep
- **Status** : Not Started, In Progress, Completed
- **Ressource principale** : Oracle / Udemy
- **Compréhension** : Pas clair, Fragile, OK, Très clair

🔗 [Voir la database complète](lien-database)

### 📅 Plan global & calendrier
Timeline détaillée des 3 phases :
- **Phase 1** : Fondations (jan-fév 2026)
- **Phase 2** : Java SE 21 (fév-avr 2026)
- **Phase 3** : Exam Prep (avr-mai 2026)

🔗 [Voir le planning](lien-planning)

### 📖 Ressources & Exam Prep
Liens vers cours, documentation officielle Oracle, outils et stratégies d'examen.  
🔗 [Voir les ressources](lien-ressources)

---

## 📖 Qu'est-ce qu'une Learning Story (LS) ?

### Format
**LS-MX-XX** (exemple : LS-M1-03)
- **M** = Module
- **X** = Numéro du module (0-11)
- **XX** = Numéro de la story

### Structure de chaque LS

Chaque Learning Story suit un template rigoureux :

**🎯 Objectif d'apprentissage**  
Test mental : "Je peux [compétence mesurable]"

**📦 Ce que je dois maîtriser**  
Liste des concepts, méthodes, APIs à connaître

**🧠 Ce que je dois être capable d'expliquer**  
Points clés à verbaliser (style "expliquer à quelqu'un")

**⚠️ Pièges & points d'attention (examen)**  
Pièges classiques OCP, erreurs fréquentes, edge cases

**☑️ Validation (auto-check)**  
Checklist de validation avant de passer à la suite

**📝 Notes personnelles**  
Notes détaillées prises pendant l'apprentissage

---

## 🎓 Cours suivis

### Oracle Java Foundations
- **Format** : Learning Path officiel Oracle
- **Modules** : 14 modules
- **Durée** : ~8-10h
- **Certifications** : Badges Oracle (Explorer)
- **Focus** : Fondamentaux solides Java

**Lien** : [Oracle MyLearn](https://mylearn.oracle.com/ou/learning-path/oracle-java-foundations/79726)

---

### Udemy Oracle Java SE 21 Developer
- **Format** : Cours vidéo complet
- **Sections** : 36 sections
- **Durée** : ~60h de contenu
- **Focus** : Préparation intensive examen + pratique

**Lien** : [Udemy Course](lien-udemy)

**Projets inclus** :
- Section 15 : E-commerce Console Application
- Section 35 : Online Store (exam prep)

---

### Enthuware (Phase 3)
- **Type** : Mock exams
- **Format** : Questions type Oracle
- **Usage** : Phase 3 uniquement (révisions finales)

---

## 🧠 Méthodologie : Anki + Spaced Repetition

### Pourquoi Anki ?

**Spaced repetition** = technique scientifiquement prouvée pour mémoriser à long terme.

- Les flashcards sont revues à des intervalles optimaux
- Les concepts difficiles reviennent plus souvent
- Garantit la rétention jusqu'à l'examen

### Automatisation

Au lieu de créer manuellement chaque flashcard, j'utilise un **script Python** qui :
1. Parse des fichiers Markdown structurés
2. Génère automatiquement les cartes Anki
3. Les importe directement via AnkiConnect

📂 [Voir le système complet](../anki/)

### Organisation des questions

Les questions sont organisées par module dans `anki/questions/` :
- `module-01-date-time.md`
- `module-02-program-flow.md`
- `module-03-oop.md`
- etc.

**Format** : Questions style examen Oracle avec explications détaillées

---

## 🔗 Liens utiles

### Documentation officielle
- [Java SE 21 API Documentation](https://docs.oracle.com/en/java/javase/21/docs/api/)
- [Oracle Java Tutorials](https://docs.oracle.com/javase/tutorial/)

### Conventions Java
- [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html)
- [Oracle Code Conventions](https://www.oracle.com/java/technologies/javase/codeconventions-contents.html)