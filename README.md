# Farm Simulator

Farm Simulator est une application web de gestion agricole. Elle permet d’afficher l’état de différents champs et de les filtrer selon leur statut : vide, semé ou récolté.

L'application utilise Flask (Python) pour le backend et HTML/CSS/JavaScript pour le frontend.

---

## Objectif

Ce projet a pour but de :

- Visualiser les champs agricoles.
- Consulter les informations de chaque champ (nom, culture, état, date de dernière action).
- Filtrer dynamiquement les champs selon leur état.

---

## Fonctionnalités

- Affichage des champs depuis une base SQLite.
- Filtrage dynamique côté client (JavaScript).
- API REST disponible à l’URL `/fields`.
- Structure de code organisée :
  - `models.py` : modèles de données
  - `fields.py` : routes pour les champs
  - `run.py` : point d’entrée de l’application
  - `templates/` : fichiers HTML
  - `static/` : CSS et JavaScript


---


## Lancement de l'application

Voici les étapes pour exécuter l'application en local :

```
python3 -m venv venv
source venv/bin/activate
```
```
pip install flask flask_sqlalchemy flask_cors
```

```
python run.py
```
```
http://localhost:5000
```