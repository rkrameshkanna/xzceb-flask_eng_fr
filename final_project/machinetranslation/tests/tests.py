import unittest
from translator import french_to_english, english_to_french

class Testf2e(unittest.TestCase):
    def test_1(self):
        self.assertEqual(french_to_english('0'), '0')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


class Teste2f(unittest.TestCase):
    def test_1(self):
        self.assertEqual(english_to_french('0'), '0')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

unittest.main()