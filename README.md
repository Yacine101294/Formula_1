# Analyse de données de Formule 1

Ce projet utilise FastF1 et d'autres bibliothèques Python pour analyser les données de Formule 1 de 2020 à 2025, notamment :
- Les temps au tour
- L'usure des pneus
- Les données de télémétrie
- Les trajectoires des pilotes
- Les stratégies de course

## Structure du projet

```
Formula_1_v2/
├── data/                  # Dossier pour les données
│   └── cache/             # Cache FastF1
├── src/                   # Code source
│   ├── config.py          # Configuration
│   ├── data_fetcher.py    # Récupération des données
│   ├── analysis/          # Modules d'analyse
│   └── visualization/     # Modules de visualisation
├── notebooks/             # Notebooks Jupyter
└── requirements.txt       # Dépendances
```

## Installation

1. Clonez ce dépôt
2. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```

## Utilisation

1. Explorez les notebooks dans le dossier `notebooks/`
2. Utilisez les modules dans `src/` pour créer vos propres analyses

## Ressources utiles

- [Documentation FastF1](https://theoehrly.github.io/FastF1/)
- [API Ergast](https://ergast.com/mrd/)
- [Kaggle F1 Datasets](https://www.kaggle.com/search?q=formula+1)

## Licence

Ce projet est sous licence MIT. 