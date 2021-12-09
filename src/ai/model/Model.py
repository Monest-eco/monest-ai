import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import h5py
from ai.exceptions.model import *

class Model():

    # Model values
    __model = None
    __layers = []
    __history = None
    __compiled = False

    # Class parameters and constants
    __has_file = False
    __activations = ["relu", "softmax", "tanh", "sigmoid", "linear"]
    __file_name = None
    __path = None
    __save = False

    def __init__(self, file = None, save = False, name = None, path = None):
        if file != None:
            self.__has_file = True
            self.__model = tf.keras.models.load_model(file)
        else:
            self.__model = tf.keras.models.Sequential()
        if save:
            self.__save = save
            self.__file_name = name
            self.__path = path
            self.__compiled = True

    def add_dense_layer(self, neurons, activation):
        if not self.__has_file:
            if activation in self.__activations:
                if len(self.__layers) > 0:
                    if self.__layers[-1]['neurons'] <= neurons:
                        raise InvalidNeurons.InvalidNeurons("Too many neurons for this layer", neurons)
                self.__layers.append({"neurons": neurons, "activation": activation, "type": "Dense"})
            else:
                raise WrongActivation.WrongActivation("Undefined activation", activation)
        else:
            raise LoadedModel.LoadedModel("A model is loaded")

    def add_flatten_layer(self, shape):
        if not self.__has_file:
            if len(shape) != 2:
                raise InvalidShape.InvalidShape("Shape size is invalid", len(shape))
            self.__layers.append({"shape": shape, "type": "Flatten"})
        else:
            raise LoadedModel.LoadedModel("A model is loaded")

    def compile(self, loss, optimizer="sgd", metrics=["accuracy"]):
        if not self.__has_file:
            if len(self.__layers) > 0:
                for layer in self.__layers:
                    if layer["type"] == "Dense":
                        self.__model.add(tf.keras.layers.Dense(layer["neurons"], activation=layer["activation"]))
                    elif layer["type"] == "Flatten":
                        self.__model.add(tf.keras.layers.Flatten(input_shape=layer["shape"]))
                self.__model.compile(loss=loss, optimizer=optimizer, metrics=metrics)
                self.__compiled = True
            else:
                raise NoLayers.NoLayers("No layers found")
        else:
            raise LoadedModel.LoadedModel("A model is loaded")

    def fit(self, values, labels, epochs):
        if self.__compiled or self.__has_file:
            self.__history = self.__model.fit(values, labels, epochs=epochs)
        else:
            NoCompilation.NoCompilation("Model is not compiled")

    def predict(self, value):
        if self.__compiled or self.__has_file:
            return self.__model.predict(value)
        else:
            NoCompilation.NoCompilation("Model is not compiled")

    def save(self):
        if self.__save and (self.__compiled or self.__has_file):
            self.__model.save(self.__path + "/" + self.__file_name)
        else:
            raise NoSaveMode.NoSaveMode("This model is started in no save mode")

    def get_loss_curve(self):
        if self.__history != None:
            return self.__history.history["loss"]
        else:
            raise NoHistory.NoHistory("There are no histories for the fit")

    def get_accuracy_curve(self):
        if self.__history != None:
            return self.__history.history["acc"]
        else:
            raise NoHistory.NoHistory("There are no histories for the fit")