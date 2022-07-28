import unittest
from translator import french_to_english, english_to_french

class TestMyModule(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(english_to_french("Nice to meet you!"), "Ravi de vous rencontrer !")
        self.assertEqual(english_to_french("I'm the best FullStack"), "Je suis le meilleur FullStack")
        self.assertEqual(english_to_french(None), "")
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english("Ravi de vous rencontrer !"), "Nice to meet you!")
        self.assertEqual(french_to_english("Je suis le meilleur FullStack"), "I'm the best FullStack")
        self.assertEqual(french_to_english(None), "")
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ == "__main__":
    unittest.main()