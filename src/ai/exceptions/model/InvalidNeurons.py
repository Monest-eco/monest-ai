class InvalidNeurons(Exception):
    def __init__(self, message, neurons_max):
        self.neurons_max = neurons_max - 1
        super().__init__(message)