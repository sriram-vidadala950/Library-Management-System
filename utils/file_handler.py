import os
import json

def create_path(path):
    if not os.path.exists(path):
        with open(path,"w") as file:
            json.dump([],file,indent=4)

def dump_data(path,data):
    create_path(path)
    with open(path,"w") as file:
        json.dump(data,file,indent=4)

def load_data(path):
    create_path(path)
    with open(path,"r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []
    return data