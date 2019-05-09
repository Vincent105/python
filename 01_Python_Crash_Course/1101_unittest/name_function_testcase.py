import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """測試names_function"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('Vincent', 'Wang')
        self.assertEqual(formatted_name, 'Vincent Wang')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('Vincent', 'Wang', 'Yese')
        self.assertEqual(formatted_name, 'Vincent Yes Wang')

unittest.main()