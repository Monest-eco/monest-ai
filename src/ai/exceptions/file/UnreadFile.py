class UnreadFile(Exception):
    def __init__(self, message, path):
        self.path = path
        super().__init__(message)