"""
Module de chargement et gestion des données FastF1.

Ce module gère :
- Le chargement des données depuis FastF1
- La gestion du cache
- Les fonctions d'accès aux données
- La validation des données chargées
"""

import fastf1
import fastf1.core
import fastf1.plotting
import pandas as pd
from typing import Optional, Dict, Any
from pathlib import Path

class DataLoader:
    def __init__(self, cache_dir: Optional[str] = None):
        """
        Initialise le chargeur de données FastF1.

        Args:
            cache_dir (str, optional): Chemin vers le répertoire de cache.
                                     Si None, utilise le répertoire par défaut.
        """
        # Configuration du cache
        if cache_dir:
            fastf1.Cache.enable_cache(cache_dir)  # Active le cache avec le répertoire spécifié
        else:
            fastf1.Cache.enable_cache(cache_dir)  # Active le cache avec le répertoire par défaut
            
        #Confirmation du stype de plot par défaut
        fastf1.plotting.setup_mpl()
    
    def load_sessions(self, year : int, gp: str, session: str) -> fastf1.core.Session:
        """
        Cahrge une session spécifique.
        
        Args:
            year (int): Année de la course
            gp (str): Nom du Grand Prix
            session (str): Type de session ('Q' pour qualification, 'R' pour course)

        Returns:
            fastf1.core.Session: Session FastF1
        """
        # get_session() est une fonction FastF1 qui charge les données d'une session de course
        # Elle télécharge les données depuis l'API F1 et les met en cache pour les utilisations futures
        # Les paramètres sont:
        # - year: l'année de la course (ex: 2023)
        # - gp: le nom du Grand Prix (ex: 'Monaco', 'Spa')  
        # - session: le type de session ('FP1','FP2','FP3','Q','R' pour les essais, qualifs ou course)
        return fastf1.get_session(year, gp, session)
    
    def load_telemetry(self, session: fastf1.core.Session, driver: str) -> pd.DataFrame:
        """
        Charge les données de télémétrie pour un pilote donné.

        Args:
            session (fastf1.core.Session): Session FastF1
            driver (str): Code du pilote (ex: 'HAM', 'VER')

        Returns:
            pd.DataFrame: DataFrame contenant les données de télémétrie
        """
        session.load()
        return session.laps.pick_driver(driver).get_telemetry()
    
    def load_lap_times(self, session: fastf1.core.Session) -> pd.DataFrame:
        """
        Charge les temps au tour pour une session donnée.
        
        Args:
            session (fastf1.core.Session): Session FastF1
            
        Returns:
            pd.DataFrame: DataFrame pandas contenant les temps au tour.
                        Un DataFrame est une structure de données tabulaire 2D
                        (similaire à une feuille Excel) fournie par la librairie pandas,
                        permettant de stocker et manipuler facilement des données.
        """
        session.load()
        return session.laps
    
    def load_weather_data(self, session: fastf1.core.Session) -> pd.DataFrame:
        """
        Charge les temps au tour pour tous les pilotes.

        Args:
            session (fastf1.core.Session): Session FastF1

        Returns:
            pd.DataFrame: DataFrame contenant les temps au tour
        """
        # session.load() est une méthode FastF1 qui charge les données de la session en mémoire
        # Elle doit être appelée avant d'accéder aux données de la session
        # Les données sont chargées depuis le cache si disponible, sinon téléchargées depuis l'API F1
        session.load()
        return session.laps
    
    def load_weather_data(self, session: fastf1.core.Session) -> pd.DataFrame:
        """
        charge les données météorologiques de la session.
        
        Args:
            session (fastf1.core.Session): Session FastF1

        Returns:
            pd.DataFrame: DataFrame contenant les données météorologique
        """
        session.load()
        return session.drivers
    
    def get_track_info(self, session: fastf1.core.Session) -> Dict[str, Any]:
        """
        Récupère les informations sur le circuit.
        
        Args:
            sessions (fastf1.core.Session): Session FastF1
            
        Returns:
            Dict[str, Any]: Dictionnaire contenant les informations sur le circuit
        """
        session.load()
        return session.track