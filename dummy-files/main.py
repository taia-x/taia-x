from Sensors import *
import json


def dummy_file():
    dict1 = {
        "sensor1": "data1",
        "sensor2": "data2",
        "sensor3": "data3",
        "sensor4": "data4"
    }
    json1 = json.dumps(dict1, indent=4)
    return json1


def save_file(name, path1):
    with open(f"{path1 + name}.json", "w") as outfile:
        outfile.write(dummy_file())


def main(path1=None):
    name = "example1"
    save_file(name, path1)


if __name__ == "__main__":
    print("In construction for generating dummy files..")
    path = ""
    main(path)
