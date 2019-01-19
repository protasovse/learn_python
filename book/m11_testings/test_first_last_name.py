import unittest
from name_function import *


class NamesTestCase(unittest.TestCase):
    """Тесты для 'name_function.py'."""

    def test_first_last_name(self):
        """Имена вида 'Иванов Антон' работают правильно?"""
        formatted_name = get_formatted_name('иванов', 'антон')
        self.assertEqual(formatted_name, 'Иванов Антон')

    def test_first_last_middle_name(self):
        """Имена вида 'Антон Велерьевич Иванов' работают правильно?"""
        formatted_name = get_formatted_name('антон', 'иванов', 'валерьевич')
        self.assertEqual(formatted_name, 'Антон Валерьевич Иванов')


if __name__ == '__main__':
    unittest.main()
