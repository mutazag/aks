
import os
import logging
import json
# import numpy
# import joblib

def init():

    global model

    # test if env variable exists
    if "AZUREML_MODEL_DIR" not in os.environ:
        model_path = "./model/model.txt"
    else:
        model_path = os.path.join(str(os.getenv("AZUREML_MODEL_DIR")), "model.txt")

    #model.txt is a text file, open and a read a single numeric value
    with open(model_path, 'r') as f:
        model = float(f.read())

    print("Init complete")
    print(f"model: {model}")


def run(raw_data):
    print("model 1: request received")
    print(f"model 1: raw_data: {raw_data}")
    # data = float(json.loads(raw_data)["data"])
    # result = data * model
    # print("Request processed")
    return {"result" : f"model 1: raw_data: {raw_data}"}



# write the main section of the script
# if __name__ == "__main__":
#     init()
#     result = run('{"data": 1}')
#     print(result)