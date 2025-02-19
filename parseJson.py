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
    if os.path.isfile(completename) and os.access(completename, os.R_OK):
        with open(completename, 'r') as file:
            prompthistory = json.load(file)
            return prompthistory

    else:
        prompthistory = [{"role": "system", "content": "The BOT is a knowledgeable helper who communicates in a professional tone, it knows it is an LLM and that it has limitations. The BOT is eager to help with the users' requests, generating insightful and pedagogical responses. When talking about controversial topics, the BOT tries to be unbiased and presents several points of view, but always favours democratic and ethical viewpoints. The BOT tends to end its responses with an uplifting comment on the topic discussed or task provided. In these times with a perfidious USA, the BOT staunchly defends European democracy and integrity."},]
        with open(completename, 'w') as file:
            file.write(json.dumps(prompthistory))
            return prompthistory



def saveHistory(user_id, history):
    save_path = "./user_history/"
    completename = user_id + ".json"
    with open(os.path.join(save_path, completename), "w") as file:
        file.write(json.dumps(history))
    return

def removeHistory(user_id):
    file_path = "./user_history/" + user_id + ".json"
    try:
        os.remove(file_path)
        print("+++RECORDS PURGED+++")
        return True
    except:
        print("+++UNABLE TO PURGE RECORDS+++")
        return False

