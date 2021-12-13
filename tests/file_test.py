import unittest
import sys
sys.path.append("src/")
from ai.file import *
from ai.dataset import *
from ai.model import *

file = File.File("./tests/")

class TestFile(unittest.TestCase):

    def test_get_files_number(self):
        self.assertEqual(file.get_number_files(), 2)
        self.assertEqual(file.get_number_backup_files(), 2)

    def test_get_file_paths(self):
        self.assertEqual(file.get_file_path(0), "./tests/ai_test.h5")
        self.assertEqual(file.get_backup_file_path(0), "./tests/backup_ai_cool.h5")

    def test_get_file_names(self):
        self.assertEqual(file.get_file_name(0), "ai_test")
        self.assertEqual(file.get_backup_file_name(0), "backup_ai_cool")

    def test_get_file_objects(self):
        obj = file.get_file_object(0)
        obj_backup = file.get_backup_file_object(0)

        self.assertDictEqual(obj, {"path": "./tests/ai_test.h5", "name": "ai_test"})
        self.assertDictEqual(obj_backup, {"path": "./tests/backup_ai_cool.h5", "name": "backup_ai_cool"})

    def test_get_file_contents(self):
        content = file.get_file_content(0)
        content_backup = file.get_backup_file_content(0)

        self.assertEqual(content, "yes")
        self.assertEqual(content_backup, "no")

    def test_append_files(self):
        file.append_file("./bin/test/t.h5")
        file.append_backup_file("./bin/test/t.h5")

        self.assertEqual(file.get_number_files(), 2)
        self.assertEqual(file.get_number_backup_files(), 2)

if __name__ == "__main__":
    unittest.main()