"""
Configuration globale du projet d'analyse de Formule 1.

Ce fichier contient toutes les constantes et paramètres de configuration utilisés dans le projet :
- Chemins vers les dossiers de données
- Années et Grands Prix à analyser
- Pilotes et équipes d'intérêt
- Paramètres de visualisation
- Etc.
"""

import os                           # Gestion des chemins et variables d'environnement
import pathlib                      # Manipulation avancée des chemins de fichiers
import matplotlib.pyplot as plt     # Création de graphiques et visualisations
import seaborn as sns               # Extension de matplotlib pour de plus beaux graphiques

# --------------------------------------------------
# Chemins des dossiers (adaptés à la structure du projet)
# --------------------------------------------------

#Chemin du répertoire racine du projet
# Définit le chemin absolu vers le répertoire racine du projet
# __file__ : chemin du fichier actuel (config.py)
# .parent.parent : remonte de 2 niveaux (src -> racine)
# .absolute() : convertit en chemin absolu
ROOT_DIR = pathlib.Path(__file__).parent.parent.absolute()

#Chemin des sous-dossiers
DATA_DIR = os.path.join(ROOT_DIR, 'data')      # Dossier contenant toutes les données du projet
CACHE_DIR = os.path.join(DATA_DIR, 'cache')    # Dossier de cache pour les données FastF1
EXPORT_DIR = os.path.join(DATA_DIR, 'exports') # Dossier pour les données exportées (CSV, JSON...)
PLOTS_DIR = os.path.join(DATA_DIR, 'plots')    # Dossier pour sauvegarder les graphiques générés

#Chemins des dossiers s'ils n'existent pas
os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs(EXPORT_DIR, exist_ok=True)
os.makedirs(PLOTS_DIR, exist_ok=True)

# --------------------------------------------------
# Configuration FastF1
# --------------------------------------------------

#Niveau de log pour FastF1(DEBUG, INFO, WARNING, ERROR, CRITICAL)
FASTF1_LOG_LEVEL = 'INFO'

# --------------------------------------------------
# Périodes d'analyse
# --------------------------------------------------

#Années à analyser
YEARS = [2020, 2021, 2022, 2023, 2024]

#Format plus détaillé pour les années et les grands prix
#Liste des saisons pour l'analyse (à mettre à jour en fonction des besoins)
SEASON = {
    2020 : {
        'name' : 'Saison 2020',
        'race' : [
            'Austrian Grand Prix', 'Styrian Grand Prix', 'Hungarian Grand Prix', 'British Grand Prix', 'Spanish Grand Prix', 'Belgian Grand Prix', 'Italian Grand Prix', 'Tuscan Grand Prix', 'Russian Grand Prix', 'Eifel Grand Prix', 'Portuguese Grand Prix', 'Emilia Romagna Grand Prix', 'Turkish Grand Prix', 'Bahrain Grand Prix', 'Sakhir Grand Prix', 'Abu Dhabi Grand Prix'
        ]
    }, 
    
    2021 : {
        'name' : "Saison 2021",
        'race': [
            'Bahrain Grand Prix', 'Saudi Arabian Grand Prix', 'Australian Grand Prix',
            'Azerbaijan Grand Prix', 'Miami Grand Prix', 'Emilia Romagna Grand Prix',
            'Monaco Grand Prix', 'Spanish Grand Prix', 'Canadian Grand Prix',
            'Austrian Grand Prix', 'British Grand Prix', 'Hungarian Grand Prix',
            'Belgian Grand Prix', 'Dutch Grand Prix', 'Italian Grand Prix',
            'Singapore Grand Prix', 'Japanese Grand Prix', 'Qatar Grand Prix',
            'United States Grand Prix', 'Mexico City Grand Prix', 'São Paulo Grand Prix',
            'Las Vegas Grand Prix', 'Abu Dhabi Grand Prix'
        ]
    },
    
    2022 : {
        'name': 'Saison 2022',
        'races': [
            'Bahrain Grand Prix', 'Saudi Arabian Grand Prix', 'Australian Grand Prix',
            'Emilia Romagna Grand Prix', 'Miami Grand Prix', 'Spanish Grand Prix',
            'Monaco Grand Prix', 'Azerbaijan Grand Prix', 'Canadian Grand Prix',
            'British Grand Prix', 'Austrian Grand Prix', 'French Grand Prix',
            'Hungarian Grand Prix', 'Belgian Grand Prix', 'Dutch Grand Prix',
            'Italian Grand Prix', 'Singapore Grand Prix', 'Japanese Grand Prix',
            'United States Grand Prix', 'Mexico City Grand Prix', 'São Paulo Grand Prix',
            'Abu Dhabi Grand Prix'
        ]
    },
            
    2023 : {
        'name': 'Saison 2023',
        'races': [
            'Bahrain Grand Prix', 'Saudi Arabian Grand Prix', 'Australian Grand Prix',
            'Azerbaijan Grand Prix', 'Miami Grand Prix', 'Emilia Romagna Grand Prix',
            'Monaco Grand Prix', 'Spanish Grand Prix', 'Canadian Grand Prix',
            'Austrian Grand Prix', 'British Grand Prix', 'Hungarian Grand Prix',
            'Belgian Grand Prix', 'Dutch Grand Prix', 'Italian Grand Prix',
            'Singapore Grand Prix', 'Japanese Grand Prix', 'Qatar Grand Prix',
            'United States Grand Prix', 'Mexico City Grand Prix', 'São Paulo Grand Prix',
            'Las Vegas Grand Prix', 'Abu Dhabi Grand Prix'
        ]
    },
    
    2024 : {
      'name': 'Saison 2024',
        'races': [
            'Bahrain Grand Prix', 'Saudi Arabian Grand Prix', 'Australian Grand Prix',
            'Japanese Grand Prix', 'Chinese Grand Prix', 'Miami Grand Prix',
            'Emilia Romagna Grand Prix', 'Monaco Grand Prix', 'Canadian Grand Prix',
            'Spanish Grand Prix', 'Austrian Grand Prix', 'British Grand Prix',
            'Hungarian Grand Prix', 'Belgian Grand Prix', 'Dutch Grand Prix',
            'Italian Grand Prix', 'Azerbaijan Grand Prix', 'Singapore Grand Prix',
            'United States Grand Prix', 'Mexico City Grand Prix', 'São Paulo Grand Prix',
            'Las Vegas Grand Prix', 'Qatar Grand Prix', 'Abu Dhabi Grand Prix'
        ]
    }
}

# --------------------------------------------------
# Pilotes et équipes d'intérêt
# --------------------------------------------------

#Pilotes et leurs abréviation par année
DRIVERS = {
    2020 : {
        'HAM': 'Lewis Hamilton',
        'BOT': 'Valtteri Bottas',
        'VER': 'Max Verstappen',
        'ALB': 'Alexander Albon',
        'LEC': 'Charles Leclerc',
        'VET': 'Sebastian Vettel',
        'PER': 'Sergio Perez',
        'STR': 'Lance Stroll',
        'RIC': 'Daniel Ricciardo',
        'OCO': 'Esteban Ocon',
        'SAI': 'Carlos Sainz',
        'NOR': 'Lando Norris',
        'KVY': 'Daniil Kvyat',
        'GAS': 'Pierre Gasly',
        'RAI': 'Kimi Räikkönen',
        'GIO': 'Antonio Giovinazzi',
        'GRO': 'Romain Grosjean',
        'MAG': 'Kevin Magnussen',
        'RUS': 'George Russell',
        'LAT': 'Nicholas Latifi',
        'HUL': 'Nico Hulkenberg',
        'FIT': 'Pietro Fittipaldi',
        'AIT': 'Jack Aitken'
    },
    
    2021 : {
    'HAM': 'Lewis Hamilton',
    'BOT': 'Valtteri Bottas',
    'VER': 'Max Verstappen',
    'PER': 'Sergio Perez',
    'LEC': 'Charles Leclerc',
    'SAI': 'Carlos Sainz',
    'RIC': 'Daniel Ricciardo',
    'NOR': 'Lando Norris',
    'ALO': 'Fernando Alonso',
    'OCO': 'Esteban Ocon',
    'VET': 'Sebastian Vettel',
    'STR': 'Lance Stroll',
    'GAS': 'Pierre Gasly',
    'TSU': 'Yuki Tsunoda',
    'RAI': 'Kimi Räikkönen',
    'GIO': 'Antonio Giovinazzi',
    'MSC': 'Mick Schumacher',
    'MAZ': 'Nikita Mazepin',
    'RUS': 'George Russell',
    'LAT': 'Nicholas Latifi',
    'HUL': 'Nico Hulkenberg'  # Remplaçant COVID (non titulaire)
    },
    
    2022 : {
    'VER': 'Max Verstappen',
    'PER': 'Sergio Perez',
    'LEC': 'Charles Leclerc',
    'SAI': 'Carlos Sainz',
    'HAM': 'Lewis Hamilton',
    'RUS': 'George Russell',
    'NOR': 'Lando Norris',
    'RIC': 'Daniel Ricciardo',
    'ALO': 'Fernando Alonso',
    'OCO': 'Esteban Ocon',
    'VET': 'Sebastian Vettel',
    'STR': 'Lance Stroll',
    'GAS': 'Pierre Gasly',
    'TSU': 'Yuki Tsunoda',
    'BOT': 'Valtteri Bottas',
    'ZHO': 'Zhou Guanyu',
    'MSC': 'Mick Schumacher',
    'MAG': 'Kevin Magnussen',
    'ALB': 'Alexander Albon',
    'LAT': 'Nicholas Latifi',
    'DEV': 'Nyck de Vries'  # Remplaçant (1 GP pour Albon)
    },
    
    2023 : {
    'VER': 'Max Verstappen',
    'PER': 'Sergio Perez',
    'LEC': 'Charles Leclerc',
    'SAI': 'Carlos Sainz',
    'HAM': 'Lewis Hamilton',
    'RUS': 'George Russell',
    'NOR': 'Lando Norris',
    'PIA': 'Oscar Piastri',
    'ALO': 'Fernando Alonso',
    'STR': 'Lance Stroll',
    'OCO': 'Esteban Ocon',
    'GAS': 'Pierre Gasly',
    'BOT': 'Valtteri Bottas',
    'ZHO': 'Zhou Guanyu',
    'MAG': 'Kevin Magnussen',
    'HUL': 'Nico Hulkenberg',
    'ALB': 'Alexander Albon',
    'SAR': 'Logan Sargeant',
    'DEV': 'Nyck de Vries',
    'RIC': 'Daniel Ricciardo',  # À partir de mi-saison
    'TSU': 'Yuki Tsunoda',
    'LAW': 'Liam Lawson'  # Remplaçant Ricciardo blessé
    },
    
    2024 : {
        'VER': 'Max Verstappen',
        'PER': 'Sergio Perez',
        'LEC': 'Charles Leclerc',
        'SAI': 'Carlos Sainz',
        'HAM': 'Lewis Hamilton',
        'RUS': 'George Russell',
        'NOR': 'Lando Norris',
        'PIA': 'Oscar Piastri',
        'ALO': 'Fernando Alonso',
        'STR': 'Lance Stroll',
        'OCO': 'Esteban Ocon',
        'GAS': 'Pierre Gasly',
        'ALB': 'Alexander Albon',
        'SAR': 'Logan Sargeant',
        'TSU': 'Yuki Tsunoda',
        'RIC': 'Daniel Ricciardo',
        'HUL': 'Nico Hulkenberg',
        'MAG': 'Kevin Magnussen',
        'BOT': 'Valtteri Bottas',
        'ZHO': 'Guanyu Zhou',
        'LAW': 'Liam Lawson',
        'BEA': 'Franco Colapinto'
    }
}

#Equipes et leurs codes couleur
TEAMS = {
    2024: {
        'Red Bull Racing': '#0600EF',
        'Ferrari': '#DC0000',
        'Mercedes': '#00D2BE',
        'McLaren': '#FF8700',
        'Aston Martin': '#006F62',
        'Alpine': '#0090FF',
        'Williams': '#005AFF',
        'Racing Bulls': '#1E41FF',
        'Kick Sauber': '#900000',
        'Haas F1 Team': '#FFFFFF'
    },
    2023: {
        'Red Bull Racing': '#1E41FF',
        'Ferrari': '#DC0000',
        'Mercedes': '#00D2BE',
        'McLaren': '#FF8700',
        'Aston Martin': '#006F62',
        'Alpine': '#0090FF',
        'Williams': '#005AFF',
        'AlphaTauri': '#2B4562',
        'Alfa Romeo': '#900000',
        'Haas F1 Team': '#FFFFFF'
    },
    2022: {
        'Red Bull Racing': '#1E41FF',
        'Ferrari': '#DC0000',
        'Mercedes': '#00D2BE',
        'McLaren': '#FF8700',
        'Aston Martin': '#006F62',
        'Alpine': '#0090FF',
        'Williams': '#005AFF',
        'AlphaTauri': '#2B4562',
        'Alfa Romeo': '#900000',
        'Haas F1 Team': '#FFFFFF'
    },
    2021: {
        'Red Bull Racing': '#1E41FF',
        'Ferrari': '#DC0000',
        'Mercedes': '#00D2BE',
        'McLaren': '#FF8700',
        'Aston Martin': '#006F62',
        'Alpine': '#0090FF',
        'Williams': '#005AFF',
        'AlphaTauri': '#2B4562',
        'Alfa Romeo': '#900000',
        'Haas F1 Team': '#FFFFFF'
    },
    2020: {
        'Red Bull Racing': '#1E41FF',
        'Ferrari': '#DC0000',
        'Mercedes': '#00D2BE',
        'McLaren': '#FF8700',
        'Racing Point': '#F596C8',
        'Renault': '#FFF500',
        'Williams': '#005AFF',
        'AlphaTauri': '#2B4562',
        'Alfa Romeo': '#900000',
        'Haas F1 Team': '#FFFFFF'
    }
}


# --------------------------------------------------
# Configuration des visualisations
# --------------------------------------------------

# Configuration de style pour matplotlib
def configure_mpl_style ():
    """Configure le style matplotilib pour les visualisations."""
    plt.style.use('dark_background')                                                     # Utilise un thème sombre
    plt.rcParams['figyre.figsize'] = (12, 7)                                             # Définit la taille par défaut des figures
    plt.rcParams['figure.dpi'] = 100                                                     # Définit la résolution des figures
    plt.rcParams['axes.grid'] = True                                                     # Active la grille sur les axes
    plt.rcParams['grid.alpha'] = 0.3                                                     # Définit la transparence de la grille
    
    # Configuration des polices
    plt.rcParams['font.family'] = 'sans-serif'                                          # Utilise une police sans-serif
    plt.rcParams['font.sans-serif'] = ['Arial', "DejaVu Sans", 'Liberation Sans', 'sans-serif']  # Définit l'ordre de préférence des polices

    # Configuration de seaborn
    sns.set_context("talk")                                                             # Utilise le contexte "talk" pour des graphiques plus grands
    
#Palettes de couleurs pour les visualisations
COLOR_PALETTES = {
    'teams' : {team : color for team, color in TEAMS[2024].item()}
}



