import json

def fetchPersona():
    file_path = "personasTemplate.json"
    try:
        print(file_path)
        with open(file_path, "r") as file:
            personasObj = json.load(file)
        return personasObj
    except:
        print("Error: No 'personas.json' file exists. Remember to rename the template accordingly.")

def fetchLLMConnfig():
    try:
        LLMObj = json.loads('./LLMConfigTemplate.json')
    except:
        print("Error: No file named 'LLMConfigTemplate.json'")
