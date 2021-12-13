import glob
import os
from ai.exceptions.file import *

class File():

    __global_path = None
    __files = []
    __backup_files = []

    def __init__(self, global_path):
        self.__global_path = global_path
        self.__files = [{"path": f, "name": f.split('/')[-1].split('.h5')[0]} for f in glob.glob("%s/ai_*.h5" % (self.__global_path))]
        self.__backup_files = [{"path": f, "name": f.split('/')[-1].split('.h5')[0]} for f in glob.glob("%s/backup_ai_*.h5" % (self.__global_path))]

    def get_number_files(self):
        return len(self.__files)

    def get_number_backup_files(self):
        return len(self.__backup_files)

    def get_file_path(self, index):
        if len(self.__files) > index and index >= 0:
            return self.__files[index]["path"]
        else:
            raise IndexRange.IndexRange("Index out of range", index)

    def get_backup_file_path(self, index):
        if len(self.__backup_files) > index and index >= 0:
            return self.__backup_files[index]["path"]
        else:
            raise IndexRange.IndexRange("Index out of range", index)

    def get_file_name(self, index):
        if len(self.__files) > index and index >= 0:
            return self.__files[index]["name"]
        else:
            raise IndexRange.IndexRange("Index out of range", index)

    def get_backup_file_name(self, index):
        if len(self.__backup_files) > index and index >= 0:
            return self.__backup_files[index]["name"]
        else:
            raise IndexRange.IndexRange("Index out of range", index)

    def get_file_object(self, index):
        if len(self.__files) > index and index >= 0:
            return self.__files[index]
        else:
            raise IndexRange.IndexRange("Index out of range", index)

    def get_backup_file_object(self, index):
        if len(self.__backup_files) > index and index >= 0:
            return self.__backup_files[index]
        else:
            raise IndexRange.IndexRange("Index out of range", index)

    def get_file_content(self, index):
        if len(self.__files) > index and index >= 0:
            file = open(self.__files[index]["path"], "r", encoding='utf-8')
            content = file.read()
            file.close()
            return content
        else:
            raise IndexRange.IndexRange("Index out of range", index)

    def get_backup_file_content(self, index):
        if len(self.__backup_files) > index and index >= 0:
            file = open(self.__backup_files[index]["path"], 'r', encoding='utf-8')
            content = file.read()
            file.close()
            return content
        else:
            raise IndexRange.IndexRange("Index out of range", index)

    def append_file(self, path):
        if not path.endswith('.h5'):
            raise FileExtension.FileExtension("Wrong extension", path.split('.')[-1])
        if not os.path.isfile(path):
            raise UnreadFile.UnreadFile("File is not exist", path)
        self.__files.append({"path": path, "name": path.split('/')[-1].split('.h5')[0]})

    def append_backup_file(self, path):
        if not path.endswith('.h5'):
            raise FileExtension.FileExtension("Wrong extension", path.split('.')[-1])
        if not os.path.isfile(path):
            raise UnreadFile.UnreadFile("File is not exist", path)
        self.__files.append({"path": path, "name": path.split('/')[-1].split('.h5')[0]})