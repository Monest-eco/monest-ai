import json
import os
from ai.dataset.Dataset import Dataset
from ai.exceptions.file.UnreadFile import UnreadFile
import numpy as np

class DatasetJSON(Dataset):

    # Constants
    __labels = {"nothing": 0, "fridge": 1, "oven": 2}

    def __init__(self, file):
        self._file = file
        self.__get_file_content()

    def __get_file_content(self):
        if os.path.isfile(self._file):
            opened_file = open(self._file, "r", encoding="utf-8")
            content = opened_file.read()
            opened_file.close()
            self._datas = json.loads(content)
        else:
            raise UnreadFile("File not found", self._file)

    def get_datas(self):
        return self._datas

    def get_shape_values(self, n):
        nb = len(self._datas) // n

        if len(self._datas) % n != 0:
            nb += 1
        metadata = np.ndarray(shape=(nb, n), dtype=np.float32)
        metadata.fill(0)
        index = 0
        for i in range(0, len(metadata)):
            for x in range(0, len(metadata[i])):
                if index < len(self._datas):
                    metadata[i].put(x, self._datas[index]["data_esp32"])
                    index += 1
        return (metadata - np.mean(metadata)) / np.std(metadata)

    def get_label_values(self):
        data = np.ndarray(shape=(len(self._datas)), dtype=int)
        data.fill(0)

        for i in range(0, len(self._datas)):
            dic = self._datas[i]
            data.put(i, self.__labels.get(dic["name"]))
        return data

    def timestamp_values(self):
        data = []

        for dic in self._datas:
            data.append(dic['date_esp32'])
        return data