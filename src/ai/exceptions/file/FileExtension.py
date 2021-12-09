class FileExtension(Exception):
    def __init__(self, message, extension):
        self.extension = extension
        super().__init__(message)