import json
import os
from ai.exceptions.file.UnreadFile import UnreadFile
import numpy as np

class Dataset():

    _file = None
    _datas = None

    def get_datas(self):
        pass

    def get_shape_values(self, n):
        pass

    def get_label_values(self):
        pass

    def timestamp_values(self):
        pass