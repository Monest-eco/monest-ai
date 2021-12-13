from ai.model import *
from ai.file import *
from ai.dataset import *

if __name__ == "__main__":
    file = File.File("./bin")
    model = None
    dataset = None

    if file.get_number_files() > 0:
        model = Model.Model(file.get_file_path(0), True, file.get_file_name(0), file.get_file_path(0))
    else:
        model = Model.Model(save=True, name="ai_result", path="./bin")
        model.add_flatten_layer([1, 300])
        model.add_dense_layer(500, "relu")
        model.add_dense_layer(250, "relu")
        model.add_dense_layer(2, "sigmoid")
        model.compile()
        model.save()
    # data = Dataset.Dataset("./bin/data_fridge.json")
    # metadata = data.get_shape_values(300)
    # for i in range(0, len(metadata)):
    #     model.fit()