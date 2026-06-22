# test_etherwave.py
"""
Tests for EtherWave module.
"""

import unittest
from etherwave import EtherWave

class TestEtherWave(unittest.TestCase):
    """Test cases for EtherWave class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EtherWave()
        self.assertIsInstance(instance, EtherWave)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EtherWave()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
