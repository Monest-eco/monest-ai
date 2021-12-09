class WrongActivation(Exception):
    def __init__(self, message, activation):
        self.activation = activation
        super().__init__(message)