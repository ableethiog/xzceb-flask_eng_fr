import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        # Test a simple translation
        english_text = 'Hello'
        french_text = english_to_french(english_text)
        expected_output = 'Bonjour'
        self.assertEqual(english_to_french(french_text), expected_output)

        # Test with an empty string
        english_text = ''
        expected_output = ''
        french_text = english_to_french(english_text)
        self.assertNotEqual(english_to_french(french_text), expected_output)


    def test_french_to_english(self):
        # Test a simple translation
        french_text = 'Bonjour'
        expected_output = 'Hello'
        english_text = french_to_english(french_text)
        self.assertEqual(french_to_english(english_text), expected_output)

        # Test with an empty string
        french_text = ''
        expected_output = ''
        english_text = french_to_english(french_text)
        self.assertNotEqual(french_to_english(english_text), expected_output)

if __name__ == '__main__':
    unittest.main()