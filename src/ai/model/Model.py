class Model():
    _model = None
    _layers = []
    _history = None
    _compiled = False

    _file_name = None
    _path = None
    _save = False
    _has_file = False

    def add_layer(self, layer_type, datas):
        """Add a layer"""
        pass

    def compile(self, loss, optimizer, metrics):
        """Compile the model with a loss, optimizer and metric type"""
        pass

    def fit(self, values, labels, epochs):
        """Fit the model with values corresponding to labels"""
        pass

    def predict(self, value):
        """The model will predict the value probability"""
        pass

    def save(self):
        """Save the current model with his fit"""
        pass

    def get_curve(self, curve_type):
        """Get the actual history curve"""
        pass
