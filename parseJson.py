import json
import os

def fetchPersona():
    file_path = "personas.json"
    try:
        with open(file_path, "r") as file:
            personasObj = json.load(file)
        return personasObj
    except:
        print("Error: No 'personas.json' file exists; remember to rename the template accordingly.")

def fetchLLMConfig():
    file_path = "LLMConfig.json"
    try:
        with open(file_path, "r") as file:
            llmObj = json.load(file)
        return llmObj
    except:
        print("Error: No 'LLMConfigTemplate.json' file exists; remember to rename the template accordingly.")

def fetchHistory(user_id):
    save_path = "./user_history/"
    name_of_file = user_id
    completename = os.path.join(save_path, name_of_file + ".json")
    with open(completename) as file:
        return json.load(file)


def saveHistory(user_id, history):
    save_path = "./user_history/"
    completename = user_id + ".json"
    with open(os.path.join(save_path, completename), "w") as file:
        toFile = history
        file.write(toFile)
    return
