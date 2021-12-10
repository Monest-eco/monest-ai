import json
import os
from ai.exceptions.file import *
import numpy as np

class Dataset():

    # Dataset parameters
    __file = None
    __datas = None

    def __init__(self, file):
        self.__file = file
        self.__get_file_content()

    def __get_file_content(self):
        if os.path.isfile(self.__file):
            opened_file = open(self.__file, "r", encoding="utf-8")
            content = opened_file.read()
            opened_file.close()
            self.__datas = json.loads(content)
        else:
            raise UnreadFile.UnreadFile("File not found", self.__file)

    def get_datas(self):
        return self.__datas

    def get_shape_values(self, n):
        nb = len(self.__datas) // n

        if len(self.__datas) % n != 0:
            nb += 1
        metadata = np.ndarray(shape=(nb, 1, n), dtype=np.ndarray)
        metadata.fill(0)
        index = 0
        for i in range(0, len(metadata)):
            for x in range(0, len(metadata[i][0])):
                if index < len(self.__datas):
                    metadata[i][0].put(x, self.__datas[index]["intensity"])
                    index += 1
        return metadata

    def get_label_values(self):
        data = []

        for dic in self.__datas:
            data.append(dic["name"])
        return data

    def timestamp_values(self):
        data = []

        for dic in self.__datas:
            data.append(dic['time'])
        return data