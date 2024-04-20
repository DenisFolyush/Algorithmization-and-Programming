import unittest

from src.kmp_argoritm import kmp_search


class TestKMP(unittest.TestCase):
    def test_kmp_search(self):
        # текст якщо є шукане слово
        needle = "babato"
        haystack = "bababalabohatoiababato"
        self.assertTrue(kmp_search(needle, haystack))

        # якщо немає
        needle = "xyz"
        haystack = "bababalabohatoiababato"
        self.assertFalse(kmp_search(needle, haystack))

        # якщо шуканого слова немає
        needle = ""
        haystack = "bababalabohatoiababato"
        self.assertTrue(kmp_search(needle, haystack))

        # якщо хайстек пустий
        needle = "babato"
        haystack = ""
        self.assertFalse(kmp_search(needle, haystack))

        # що то що то пусте
        needle = ""
        haystack = ""
        self.assertTrue(kmp_search(needle, haystack))


if __name__ == '__main__':
    unittest.main()
