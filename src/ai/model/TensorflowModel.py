import os
from ai.exceptions.model.InvalidType import InvalidType
from ai.model.Model import Model
from ai.model.enums.TensorFlowEnum import TensorflowEnum,TensorCurve
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import h5py
from ai.exceptions.model.InvalidNeurons import InvalidNeurons
from ai.exceptions.model.LoadedModel import LoadedModel
from ai.exceptions.model.NoCompilation import NoCompilation
from ai.exceptions.model.NoHistory import NoHistory
from ai.exceptions.model.NoLayers import NoLayers
from ai.exceptions.model.NoSaveMode import NoSaveMode
from ai.exceptions.model.WrongActivation import WrongActivation
from ai.exceptions.model.InvalidCurve import InvalidCurve

class TensorflowModel(Model):
    """This class is used to make a machine learning using TensorFlow."""

    # Class parameters and constants
    __activations = ["relu", "softmax", "tanh", "sigmoid", "linear"]

    def __init__(self, file: str = None, save: bool = False, name: str = None, path: str = None):
        if file != None:
            self._has_file = True
            self._model = tf.keras.models.load_model(file)
        else:
            self._model = tf.keras.models.Sequential()
        if save:
            self._save = save
            self._file_name = name
            self._path = path
            self._compiled = True

    def add_layer(self, layer_type: TensorflowEnum, datas: dict):
        """Add a layer to your AI"""
        if not self._has_file:
            if layer_type == TensorflowEnum.DENSE:
                neurons = datas["neurons"]
                activation = datas["activation"]
                if activation in self.__activations:
                    if len(self._layers) > 0:
                        for layer in self._layers:
                            if layer["type"] == "Dense":
                                if layer["neurons"] <= neurons:
                                    raise InvalidNeurons("Too many neurons for this layer", neurons)
                    self._layers.append({"neurons": neurons, "activation": activation, "type": "Dense"})
                else:
                    WrongActivation("Undefined activation", activation)
            elif layer_type == TensorflowEnum.FLATTEN:
                shape = datas["shape"]
                self._layers.append({"shape": shape, "type": "Flatten"})
            else:
                raise InvalidType("Layer type is not defined")
        else:
            raise LoadedModel("A model is loaded")

    def compile(self, loss="sparse_categorical_crossentropy", optimizer="sgd", metrics=["accuracy"]):
        """Compile your AI for using it"""
        if not self._has_file:
            if len(self._layers) > 0:
                for layer in self._layers:
                    if layer["type"] == "Dense":
                        self._model.add(tf.keras.layers.Dense(layer["neurons"], activation=layer["activation"]))
                    elif layer["type"] == "Flatten":
                        self._model.add(tf.keras.layers.Flatten(input_shape=layer["shape"]))
                self._model.compile(loss=loss, optimizer=optimizer, metrics=metrics)
                self._compiled = True
            else:
                raise NoLayers("No layers found")
        else:
            raise LoadedModel("A model is loaded")

    def fit(self, values, labels, epochs):
        """Train your AI with this function"""
        if self._compiled or self._has_file:
            self._history = self._model.fit(values, labels, epochs=epochs)
        else:
            raise NoCompilation("Model is not compiled")

    def predict(self, value):
        """Make a prediction of the electrical curve, return probabilities"""
        if self._compiled or self._has_file:
            return self._model.predict(value)
        else:
            raise NoCompilation("Model is not compiled")

    def save(self):
        """Save your AI model after his compilation and training"""
        if self._save and (self._compiled or self._has_file):
            self._model.save(self._path + "/" + self._file_name + ".h5")
        else:
            raise NoSaveMode("This model is started in no save mode")

    def get_curve(self, curve_type):
        """Get the training curve, loss and accuracy"""
        if curve_type == TensorCurve.LOSS:
            if self._history != None:
                return self._history.history["loss"]
            else:
                raise NoHistory("There are no histories for the fit")
        elif curve_type == TensorCurve.ACCURACY:
            if self.__history != None:
                return self._history.history["acc"]
            else:
                raise NoHistory("There are no histories for the fit")
        else:
            raise InvalidCurve("Curve doesn't exist")
