# -*- coding: UTF-8 -*-

from unittest import TestCase
from sample.util.datareader import InputDataReader


class Test(TestCase):
    def test_input_data_reader(self):
        reader = InputDataReader('../docs/data.csv')
        reader.read()
