import json
import os
from ai.exceptions.file import *
import numpy as np

class Dataset():

    # Constants
    __labels = {"nothing": 0, "fridge": 1, "oven": 2}

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
        metadata = np.ndarray(shape=(nb, n), dtype=np.float32)
        metadata.fill(0)
        index = 0
        for i in range(0, len(metadata)):
            for x in range(0, len(metadata[i])):
                if index < len(self.__datas):
                    metadata[i].put(x, self.__datas[index]["intensity"])
                    index += 1
        return (metadata - np.mean(metadata)) / np.std(metadata)

    def get_label_values(self):
        data = np.ndarray(shape=(len(self.__datas)), dtype=int)
        data.fill(0)

        for i in range(0, len(self.__datas)):
            dic = self.__datas[i]
            data.put(i, self.__labels.get(dic["name"]))
        return data

    def timestamp_values(self):
        data = []

        for dic in self.__datas:
            data.append(dic['time'])
        return data