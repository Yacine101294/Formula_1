"""
Module d'analyse des temps au tour.

Ce module permet d'analyser les temps au tour des pilotes, notamment :
- Comparaison des temps au tour entre pilotes
- Analyse de l'évolution des temps au tour pendant une course
- Identification des tours les plus rapides
- Analyse des secteurs et mini-secteurs
- Calcul des statistiques (moyenne, médiane, écart-type, etc.)
"""

import os
import json
import pickle
from datetime import datetime, timedelta
from typing import Any, Dict, Optional, Union
import fastf1
from pathlib import Path

class CacheManager :
    """Gestionnaire de cache pour les données FastF1."""
    
    def __init__(self, cache_dir: str = 'cache')
        """
        Initilise le gestionnaire de cache
        
        Args:
            cache_dir (str): Chemin du répertoire de cach
        """
        self.cache_dir = Path(cache_dir)                          # Convertit le chemin en objet Path pour une meilleure manipulation
        self.cache_dir.mkdir(parents=True, exist_ok=True)         # Crée le répertoire de cache s'il n'existe pas, avec les parents si nécessaire
        self.metadata_file = self.cache_dir / 'metadata.json'     # Définit le chemin du fichier metadata.json dans le cache
        self.metadata = self._load_metadata()                     # Charge les métadonnées du cache depuis le fichier

    def _load_metadata(self) -> Dict:
        """charge les métadonnées du cache."""
        if self.metadata_file.exists():
            with open(self.metadata_file, 'r') as f:
                return json.load(f)
        return {}
    
    def _save_metadata(self):
        """Sauvegarde les métadonnées du cache."""
        with open(self.metadata_file, 'w') as f:
            json.dump(self.metadata, f)
            
    def _get_cache_path(self, key: str) -> Path:
        """Génère le chemin du fichier de cache pour une clé donnée."""
        return self.cache_dir / f"{key}.pkl"
    
    def get(self, key: str, max_age: Optional[timedelta] = None) -> Optional[Any]:
        """
        Récupère une donnée du cache.
        
        Args:
            key (str): Clé de la donnée
            max_age (timedelta, optional): Âge maximum autorisé pour la donnée
            
        Returns:
            Any: Donnée en cache ou None si non trouvée ou expirée
        """
        if key not in self.metadata:
            return None
            
        cache_path = self._get_cache_path(key)
        if not cache_path.exists():
            return None
            
        # Vérification de l'âge du cache
        if max_age is not None:
            cache_time = datetime.fromisoformat(self.metadata[key]['timestamp'])
            if datetime.now() - cache_time > max_age:
                return None
                
        try:
            with open(cache_path, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
            
    def set(self, key: str, value: Any):
        """
        Stocke une donnée dans le cache.
        
        Args:
            key (str): Clé de la donnée
            value (Any): Valeur à stocker
        """
        cache_path = self._get_cache_path(key)
        
        # Sauvegarde de la donnée
        with open(cache_path, 'wb') as f:
            pickle.dump(value, f)
            
        # Mise à jour des métadonnées
        self.metadata[key] = {
            'timestamp': datetime.now().isoformat(),
            'size': os.path.getsize(cache_path)
        }
        self._save_metadata()
        
    def clear(self, key: Optional[str] = None):
        """
        Efface le cache.
        
        Args:
            key (str, optional): Clé spécifique à effacer. Si None, efface tout le cache.
        """
        if key is None:
            # Effacement complet
            for file in self.cache_dir.glob("*.pkl"):
                file.unlink()
            self.metadata = {}
        else:
            # Effacement d'une clé spécifique
            cache_path = self._get_cache_path(key)
            if cache_path.exists():
                cache_path.unlink()
            if key in self.metadata:
                del self.metadata[key]
                
        self._save_metadata()
        
    def get_cache_size(self) -> int:
        """
        Retourne la taille totale du cache en octets.
        
        Returns:
            int: Taille du cache en octets
        """
        return sum(meta['size'] for meta in self.metadata.values())
        
    def get_cache_info(self) -> Dict:
        """
        Retourne des informations sur le cache.
        
        Returns:
            Dict: Informations sur le cache
        """
        return {
            'total_size': self.get_cache_size(),
            'entry_count': len(self.metadata),
            'entries': self.metadata
        }