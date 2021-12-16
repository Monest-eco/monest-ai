from ai.model.TensorflowModel import TensorflowModel
from ai.file.File import File
from ai.dataset.DatasetJSON import DatasetJSON
from ai.model.enums.TensorFlowEnum import TensorflowEnum

if __name__ == "__main__":
    file = File("./bin")
    model = None
    dataset = None

    if file.get_number_files() > 0:
        model = TensorflowModel(file.get_file_path(0), True, file.get_file_name(0), file.get_file_path(0))
    else:
        model = TensorflowModel(save=True, name="ai_result", path="./bin")
        model.add_layer(TensorflowEnum.FLATTEN, {"shape": [300]})
        model.add_layer(TensorflowEnum.DENSE, {"neurons": 500, "activation": "relu"})
        model.add_layer(TensorflowEnum.DENSE, {"neurons": 250, "activation": "relu"})
        model.add_layer(TensorflowEnum.DENSE, {"neurons": 2, "activation": "sigmoid"})
        model.compile()
        # model.save()
    # data = DatasetJSON("./bin/datas/data_fridge3.json")
    # metadata = data.get_shape_values(300)
    # labels = data.get_label_values()
    # labels = labels[:len(metadata)]
    # model.fit(metadata, labels, 40)