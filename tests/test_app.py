# tests/test_app.py
import unittest
from app import greet

class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Tester"), "Hello, Tester!")

if __name__ == '__main__':
    unittest.main()
