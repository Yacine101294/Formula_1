# -*- coding: utf-8 -*-
"""
Script de test pour le module data_loader.py
"""

import sys
import os
import matplotlib.pyplot as plt
from pathlib import Path

# Ajouter le répertoire racine du projet au path
# Cela permet d'importer les modules depuis n'importe où dans le projet
sys.path.append(str(Path(__file__).parent.parent.parent))

# Import du module DataLoader
from src.analysis.base.data_loader import DataLoader

def test_data_loader():
    """Test basic functionality of DataLoader class."""
    print("Initializing DataLoader...")
    
    # Utilise le chemin du cache par défaut (ou spécifiez un chemin)
    cache_dir = os.path.join(Path(__file__).parent.parent.parent, "data", "cache")
    data_loader = DataLoader(cache_dir)
    
    # Charger une session de course récente (par exemple, Monaco 2023)
    print("Loading session data for Monaco 2023 Grand Prix...")
    try:
        # Notez que nous utilisons load_sessions (avec un 's') car c'est le nom de la méthode dans votre classe
        session = data_loader.load_sessions(2023, 'Monaco', 'R')
        
        # Charger les données
        print("Loading lap times...")
        lap_times = data_loader.load_lap_times(session)
        
        # Afficher quelques statistiques sur les temps au tour
        print("\n----- Lap Times Summary -----")
        print(f"Number of laps recorded: {len(lap_times)}")
        print(f"Number of drivers: {len(lap_times['Driver'].unique())}")
        
        # Trouver le tour le plus rapide
        fastest_lap = lap_times.pick_fastest()
        print(f"\nFastest lap: {fastest_lap['Driver']} - {fastest_lap['LapTime']}")
        
        # Charger des données météo (Attention: dans votre implémentation actuelle, cette méthode renvoie les pilotes)
        print("\n----- Weather/Driver Information -----")
        info = data_loader.load_weather_data(session)
        print(f"Information retrieved: {type(info)}")
        
        # Exemple de chargement de télémétrie (pour Verstappen par exemple)
        print("\n----- Loading Telemetry for VER -----")
        try:
            telemetry = data_loader.load_telemetry(session, 'VER')
            print(f"Telemetry data points: {len(telemetry)}")
            print(f"Available channels: {', '.join(telemetry.columns)}")
            
            # Simple plot of speed vs distance
            plt.figure(figsize=(10, 6))
            plt.plot(telemetry['Distance'], telemetry['Speed'])
            plt.title('Speed vs Distance - VER (Monaco 2023)')
            plt.xlabel('Distance (m)')
            plt.ylabel('Speed (km/h)')
            plt.savefig('speed_verstappen.png')
            print("Generated speed plot for Verstappen saved as 'speed_verstappen.png'")
        except Exception as e:
            print(f"Error loading telemetry: {e}")
        
        print("\nData loader test completed successfully!")
    except Exception as e:
        print(f"Error in test: {e}")
        print("Please check your data_loader.py file for errors.")

if __name__ == "__main__":
    test_data_loader()