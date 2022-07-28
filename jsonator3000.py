import json
from flask import Flask
from flask import request

app = Flask(__name__)

def data_type_in_line(line,java_data_types):
    for type in java_data_types:
        if (type in line and not ("(" in line) and not ("import" in line) and not ("serial" in line)):
            split_line = line.split(" ")
            return split_line

def get_default_value(java_type):
    if (java_type == "short" or java_type == "int" or java_type == "long" or java_type == "Integer" or java_type == "Long"):
        return 0
    elif (java_type == "float" or java_type == "double" or java_type == "Double"):
        return 0.0
    elif (java_type == "boolean" or java_type == "Boolean"):
        return True
    return ""

def get_json_from_java_object(java_entity):
    java_data_types = ["boolean", "byte", "char", "short", "int", "long", "float", "double", "String", "Integer", "List", "Long", "Date", "Double", "Boolean"]
    json_object = {}
    for line in java_entity.splitlines():
        attribute = data_type_in_line(line, java_data_types)
        if (attribute):
            json_object[attribute[len(attribute) - 1].replace(";", "")] = get_default_value(attribute[len(attribute) - 2])
    return json_object

@app.route("/")
def home():
  return "Home page"

@app.route("/entity-to-json",methods=['POST'])
def entity_to_json():
    return get_json_from_java_object(request.get_data().decode("utf-8"))

if __name__ == "__main__":
  app.run()
