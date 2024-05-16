import unittest

from src.kmp_argoritm import kmp_search


class TestKMP(unittest.TestCase):
    def test_kmp_search_found(self):
        # якщо є шукане слово
        needle = "babato"
        haystack = "bababalabohababatotoiababato"
        self.assertEqual(kmp_search(needle, haystack), [16])

    def test_kmp_search_not_found(self):
        # якщо немає шуканого слова
        needle = "xyz"
        haystack = "bababalabohatoiababato"
        self.assertEqual(kmp_search(needle, haystack), [])

    def test_kmp_search_empty_needle(self):
        # якщо шуканого слова немає
        needle = ""
        haystack = "bababalabohatoiababato"
        self.assertFalse(needle, haystack)

    def test_kmp_search_empty_haystack(self):
        # якщо хайстек пустий
        needle = "babato"
        haystack = ""
        self.assertEqual(kmp_search(needle, haystack), [])

    def test_kmp_search_both_empty(self):
        # що то що то пусте
        needle = ""
        haystack = ""
        self.assertFalse(kmp_search(needle, haystack))


class TestPrefixFunction(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(prefix_func(""), "no needle")

    def test_single_character_string(self):
        self.assertEqual(prefix_func("a"), [0])

    def test_repeating_characters(self):
        self.assertEqual(prefix_func("aaaaa"), [0, 1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
