class InvalidShape(Exception):
    def __init__(self, message, shape_size):
        self.shape_size = shape_size
        super().__init__(message)