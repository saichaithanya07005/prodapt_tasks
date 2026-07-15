import unittest
from text_utilities import word_count, unique_words, string_reversal

class TestTextUtilities(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(word_count("Hello World"), 2)

    def test_word_count_empty(self):
        self.assertEqual(word_count(""), 0)

    def test_unique_words(self):
        self.assertEqual(set(unique_words("hello hello world")), {"hello", "world"})

    def test_string_reversal(self):
        self.assertEqual(string_reversal("abc"), "cba")

    def test_single_word(self):
        self.assertEqual(word_count("Python"), 1)
        self.assertEqual(string_reversal("Python"), "nohtyP")

    def test_special_characters(self):
        self.assertEqual(string_reversal("@#123"), "321#@")
if __name__ == "__main__":
    unittest.main()