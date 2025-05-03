# TP0 — Super Calculatrice

## Présentation

Dans ce TP, j’ai mis en place une **super-calculatrice Python** capable de réaliser plusieurs opérations (addition, soustraction, multiplication, division).
L’objectif était également de concevoir et appliquer un **plan de tests unitaires** complet avec `pytest` et `unittest`, tout en respectant les bonnes pratiques de code (`flake8`).

---

## Organisation du projet

Voici la structure complète de mon projet :

```
TP 1/
└── TP0/
    ├── .pytest_cache/                  # Cache interne de pytest (à ignorer)
    ├── .venv/                          # Environnement virtuel Python (à ignorer dans un rendu)
    ├── calculate/                      # Dossier principal contenant les modules métier
    │   ├── __init__.py                 # Rend le dossier importable comme package Python
    │   ├── controller.py               # Gère la logique d’exécution de la calculatrice
    │   ├── operators.py                # Contient les fonctions des opérations (add, sub, mul, div)
    │   ├── view.py                     # Gère l'affichage et les entrées utilisateur
    │   └── __pycache__/                # Cache Python automatique (non nécessaire à versionner)
    │
    ├── tests/                          # Dossier contenant tous les fichiers de test
    │   ├── __init__.py                 # Fichier vide pour l'import
    │   ├── conftest.py                 # Ajoute calculate/ au PYTHONPATH pour les tests
    │   ├── plan_de_test.md             # Mon plan de test détaillé par module
    │   ├── test_operators.py           # Tests Pytest du module operators
    │   ├── test_view.py                # Tests Pytest du module view
    │   ├── test_controller_pytestmock.py # Tests Pytest du module controller
    │   ├── test_operators_unittest.py # Tests Unittest du module operators
    │   └── test_view_unittest.py      # Tests Unittest du module view
    │
    ├── main.py                         # Point d’entrée du programme (interface CLI)
    ├── requirements.txt                # Liste des dépendances (pytest, flake8, etc.)
    ├── __init__.py                     # Rend le dossier principal importable
    ├── README.md                       # Ce fichier
    └── TP0.pdf                         # Sujet du TP fourni
```

---

## Ce que j’ai fait

✅ J’ai implémenté un **plan de test** détaillé pour chaque fichier métier dans `calculate/`
✅ J’ai ajouté des **tests unitaires avec Pytest** pour les modules `operators`, `view`, et `controller`
✅ J’ai également ajouté les **tests avec Unittest** pour `operators` et `view`
✅ J’ai intégré `pytest-mock` pour tester le contrôleur de manière plus flexible
✅ J’ai corrigé tous les **warnings de style avec Flake8** pour garantir un code propre
✅ J’ai mis en place un fichier `conftest.py` pour assurer le bon import des modules lors des tests
✅ J’ai structuré tous les fichiers pour qu’ils puissent être exécutés et testés directement

---

## PRERECQUIS

> 📌 On s'assure d’être dans le bon dossier :

```bash
cd TP0
```

### Ensuite :

1. **On installe les dépendances** :

```bash
pip install -r requirements.txt
```

2. **On lance le programme interactif** :

```bash
python main.py
```

3. **On lance les tests Pytest** :

```bash
pytest tests/
```

4. **On lance les tests Unittest** :

```bash
python -m unittest discover -s tests/
```

5. **On vérifie le style du code** :

```bash
flake8 calculate/
```

---

## Conclusion

Ce TP m’a permis de mieux structurer un projet Python, de renforcer mes compétences en **tests unitaires**, et d’automatiser la vérification de la qualité du code.
Je suis maintenant capable de monter un projet modulaire, testable et maintenable, avec une base de tests propre et complète ✅


