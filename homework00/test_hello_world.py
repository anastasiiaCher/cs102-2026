"""Модуль с функцией text() для домашнего задания."""

import unittest

import hello_world


class HelloTestCase(unittest.TestCase):
    """Возвращает приветственное сообщение."""
    def test_hello(self):
        m = "message"
        self.assertEqual(m, hello_world.text())