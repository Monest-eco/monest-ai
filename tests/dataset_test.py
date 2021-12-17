import unittest
import sys
sys.path.append("src/")
from ai.dataset.DatasetJSON import DatasetJSON

dataset = DatasetJSON("./tests/datatest.json")

class TestDataset(unittest.TestCase):
    def test_get_datas(self):
        self.assertIsInstance(dataset.get_datas(), object)

    def test_get_label_values(self):
        self.assertIsInstance(dataset.get_label_values(), object)

    def test_get_timestamp_values(self):
        self.assertIsInstance(dataset.timestamp_values(), object)

    def test_get_shape_values(self):
        self.assertIsInstance(dataset.get_shape_values(10), object)
