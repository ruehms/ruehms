"""Test Codes / Rana Shiba"""
import unittest
from translator import english_to_french, french_to_english

class TestEn_to_Fr(unittest.TestCase):
    def test_1(self):
        self.assertEqual(english_to_french('Thank you'), 'Je vous remercie')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_2(self):
        self.assertEqual(english_to_french(''), '')

class TestFr_to_En(unittest.TestCase):
    def test_3(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')
        self.assertEqual(french_to_english('Nuit'), 'Night')
        
    def test_4(self):
        self.assertEqual(french_to_english(''), '')
    
if __name__ == "__main__":
    unittest.main()