import unittest
from ConfReader import ConfReader

class testConfReader(unittest.TestCase):

    def setUp(self):
        self.config = ConfReader("test.conf", "test/")

    def test_parse_values(self):
        self.assertTrue(self.config.parse_values())

    def test_get_value(self):
        self.assertEqual(self.config.get_value("test"), "toto")