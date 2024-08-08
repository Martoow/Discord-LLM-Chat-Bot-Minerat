import json

def fetchPersona():
    file_path = "personas.json"
    try:
        print(file_path)
        with open(file_path, "r") as file:
            personasObj = json.load(file)
        return personasObj
    except:
        print("Error: No 'personas.json' file exists; remember to rename the template accordingly.")

def fetchLLMConfig():
    file_path = "LLMConfigTemplate.json"
    try:
        print(file_path)
        with open(file_path, "r") as file:
            llmObj = json.load(file)
        return llmObj
    except:
        print("Error: No 'LLMConfigTemplate.json' file exists; remember to rename the template accordingly.")

