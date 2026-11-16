"""Module providing a function printing python version."""

import unittest

import hello_world


class HelloTestCase(unittest.TestCase):
    def test_hello(self):
        """Function printing python version."""
        m = "message"
        self.assertEqual(m, hello_world.text())
        
