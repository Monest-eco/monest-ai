class IndexRange(Exception):
    def __init__(self, message, index):
        self.index = index
        super().__init__(message)