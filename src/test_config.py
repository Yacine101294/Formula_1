"""
Script de test pour le fichier de configuration.
Vérifie que la configuration est correctement chargée et que les fonctions fonctionnent.
"""

import os
import sys
import matplotlib.pyplot as plt

# Importer le module config
import config

def test_paths():
    """Teste si les chemins sont correctement définis et si les dossiers existent."""
    print("=== Test des chemins ===")
    print(f"Répertoire racine : {config.ROOT_DIR}")
    print(f"Répertoire de données : {config.DATA_DIR}")
    print(f"Répertoire de cache : {config.CACHE_DIR}")
    print(f"Répertoire d'export : {config.EXPORT_DIR}")
    print(f"Répertoire de graphiques : {config.PLOTS_DIR}")
    
    # Vérifier que les dossiers existent
    for path in [config.DATA_DIR, config.CACHE_DIR, config.EXPORT_DIR, config.PLOTS_DIR]:
        exists = os.path.exists(path)
        print(f"  - {os.path.basename(path)} existe : {exists}")

def test_seasons():
    """Teste si les saisons sont correctement définies."""
    print("\n=== Test des saisons ===")
    for year in config.YEARS:
        try:
            season_name = config.SEASONS[year]['name']
            races_key = 'races' if 'races' in config.SEASONS[year] else 'race'
            races = config.SEASONS[year][races_key]
            print(f"{season_name} : {len(races)} courses")
        except Exception as e:
            print(f"Erreur pour l'année {year} : {e}")

def test_drivers():
    """Teste si les pilotes sont correctement définis."""
    print("\n=== Test des pilotes ===")
    for year in config.YEARS:
        try:
            drivers = config.DRIVERS[year]
            print(f"Année {year} : {len(drivers)} pilotes")
            # Afficher quelques exemples
            examples = list(drivers.items())[:3]
            for code, name in examples:
                print(f"  - {code} : {name}")
        except Exception as e:
            print(f"Erreur pour l'année {year} : {e}")

def test_teams():
    """Teste si les équipes sont correctement définies."""
    print("\n=== Test des équipes ===")
    for year in config.YEARS:
        try:
            teams = config.TEAMS[year]
            print(f"Année {year} : {len(teams)} équipes")
        except Exception as e:
            print(f"Erreur pour l'année {year} : {e}")

def test_functions():
    """Teste les fonctions d'aide."""
    print("\n=== Test des fonctions ===")
    try:
        # Tester find_race_by_name
        year = 2023
        partial_name = "monaco"
        race = config.find_race_by_name(year, partial_name)
        print(f"Recherche de '{partial_name}' en {year} : {race}")
        
        # Tester get_driver_color
        driver_code = "VER"
        color = config.get_driver_color(driver_code)
        print(f"Couleur pour {driver_code} : {color}")
        
        # Tester la configuration matplotlib
        try:
            config.configure_mpl_style()
            print("Configuration matplotlib réussie")
        except Exception as e:
            print(f"Erreur lors de la configuration matplotlib : {e}")
            
    except Exception as e:
        print(f"Erreur lors du test des fonctions : {e}")

def main():
    """Fonction principale de test."""
    print("Tests de la configuration du projet F1\n")
    
    test_paths()
    test_seasons()
    test_drivers()
    test_teams()
    test_functions()
    
    print("\nTests terminés.")

if __name__ == "__main__":
    main() 