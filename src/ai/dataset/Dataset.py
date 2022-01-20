import json
import os
from ai.exceptions.file.UnreadFile import UnreadFile
import numpy as np

class Dataset():

    _file = None
    _datas = None

    def get_datas(self):
        """Get data from file"""
        pass

    def get_shape_values(self, n):
        """Get datas with a shape of n*n"""
        pass

    def get_label_values(self):
        """Get label from datas, use it for training the IA"""
        pass

    def timestamp_values(self):
        """Get the timestamp value, this is for knowing when the electrical curve was got"""
        pass