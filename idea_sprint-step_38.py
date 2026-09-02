# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: IdeaSprint
import unittest


class TestEdgeCases(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(list_to_list([]), [])

    def test_single_element(self):
        self.assertEqual(list_to_list([1]), [1])

    def test_duplicate_elements(self):
        self.assertEqual(list_to_list([1, 1, 1]), [1])

    def test_negative_numbers(self):
        self.assertEqual(list_to_list([-1, -2, -3]), [-1, -2, -3])

    def test_mixed_types(self):
        self.assertEqual(list_to_list([1, 'a', 2.0]), [1, 'a', 2.0])

    def test_large_input(self):
        big = [i for i in range(10000)]
        self.assertEqual(list_to_list(big), big)

    def test_empty_string(self):
        self.assertEqual(list_to_list(''), [])

    def test_none_input(self):
        self.assertIsNone(list_to_list(None))


if __name__ == '__main__':
    unittest.main()
