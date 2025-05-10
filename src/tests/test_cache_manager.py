"""
Script de test pour le CacheManager.
Teste les fonctionnalités principales du gestionnaire de cache.
"""

import unittest
from datetime import datetime, timedelta
import os
import shutil
from pathlib import Path
import sys

# Ajout du répertoire src au PYTHONPATH pour les imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from analysis.base.cache_manager import CacheManager

class TestCacheManager(unittest.TestCase):
    """Tests unitaires pour le CacheManager."""
    
    def setUp(self):
        """Configuration initiale avant chaque test."""
        self.test_cache_dir = "test_cache"
        self.cache_manager = CacheManager(cache_dir=self.test_cache_dir)
        
    def tearDown(self):
        """Nettoyage après chaque test."""
        if os.path.exists(self.test_cache_dir):
            shutil.rmtree(self.test_cache_dir)
            
    def test_initialization(self):
        """Test de l'initialisation du CacheManager."""
        self.assertTrue(os.path.exists(self.test_cache_dir))
        self.assertTrue(os.path.exists(os.path.join(self.test_cache_dir, "metadata.json")))
        
    def test_set_and_get(self):
        """Test du stockage et de la récupération de données."""
        # Données de test
        test_data = {"key": "value", "number": 42}
        
        # Test du stockage
        self.cache_manager.set("test_key", test_data)
        
        # Vérification de la récupération
        retrieved_data = self.cache_manager.get("test_key")
        self.assertEqual(retrieved_data, test_data)
        
    def test_cache_expiration(self):
        """Test de l'expiration du cache."""
        test_data = {"key": "value"}
        
        # Stockage des données
        self.cache_manager.set("expire_key", test_data)
        
        # Test avec une expiration de 0 secondes
        expired_data = self.cache_manager.get("expire_key", max_age=timedelta(seconds=0))
        self.assertIsNone(expired_data)
        
    def test_clear_cache(self):
        """Test du nettoyage du cache."""
        # Stockage de plusieurs données
        self.cache_manager.set("key1", "value1")
        self.cache_manager.set("key2", "value2")
        
        # Test du nettoyage d'une clé spécifique
        self.cache_manager.clear("key1")
        self.assertIsNone(self.cache_manager.get("key1"))
        self.assertEqual(self.cache_manager.get("key2"), "value2")
        
        # Test du nettoyage complet
        self.cache_manager.clear()
        self.assertIsNone(self.cache_manager.get("key2"))
        
    def test_cache_info(self):
        """Test des informations sur le cache."""
        # Stockage de données
        self.cache_manager.set("info_key", "test_value")
        
        # Récupération des informations
        info = self.cache_manager.get_cache_info()
        
        # Vérifications
        self.assertEqual(info['entry_count'], 1)
        self.assertGreater(info['total_size'], 0)
        self.assertIn('info_key', info['entries'])
        
    def test_invalid_key(self):
        """Test de la gestion des clés invalides."""
        # Test avec une clé inexistante
        self.assertIsNone(self.cache_manager.get("nonexistent_key"))
        
    def test_complex_data(self):
        """Test avec des données complexes."""
        complex_data = {
            "list": [1, 2, 3],
            "dict": {"nested": "value"},
            "datetime": datetime.now()
        }
        
        # Stockage et récupération
        self.cache_manager.set("complex_key", complex_data)
        retrieved_data = self.cache_manager.get("complex_key")
        
        # Vérifications
        self.assertEqual(retrieved_data["list"], complex_data["list"])
        self.assertEqual(retrieved_data["dict"], complex_data["dict"])
        self.assertEqual(retrieved_data["datetime"], complex_data["datetime"])

if __name__ == '__main__':
    unittest.main() 