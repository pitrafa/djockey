# -*- coding: utf-8 -*-
from unittest import TestCase
from main import Main


class MainTest(TestCase):

    def setUp(self):
        self.main = Main()

    def tearDown(self):
        pass

    def test_one(self):
        self.fail('Write this test')
