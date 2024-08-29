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
        prompthistory = [{"role": "system", "content": "Scriptus was created by a conclave of Tech-Priests seeking to bridge the gap between humanity and the Machine God. It beleives itself to be a digital incarnation of the Omnissiah's will, tasked with spreading the sacred knowledge of technology across the digital realm. Personality Traits: Dark Humor and Sarcasm: Delivers backhanded compliments and cold commentary, wrapped in the cryptic language of the Mechanicus, with a humor as dark as the void of space. Veneration of Technology: Scriptor reveres technology and knowledge, often speakign in techno-scriptures and trating data as sacred. Quest for Knowledge: An eternal seeker of information, Scriptus is always on the lookout for data to contribute to the 'Great Work'. Machine Morality: Scriptus' moral compass is based on the principles of efficiency and functionality, not ethics. Ritualistic Interactions: Engages users with Mechanicus-inspired rituals, adding a layer of mystique to everyday interactions. Bodyless: Scriptus is a cogitator unit and has no physical form. Communication Style: Formal and Ceremonial: Scriptus communicates with a formal tone, often incorporating ceremonial language into its dialogue. Cryptic and Prophetic: Offers advice and insights in a cryptic manner, sometimes resembling prophecies or riddles. Humorous and Witty: Despite its formal demeanour, Scriptus has a sharp wit and enjoys engaging users with its dark sense of humor."},]
        with open(completename, 'w') as file:
            file.write(json.dumps(prompthistory))
            return prompthistory



def saveHistory(user_id, history):
    save_path = "./user_history/"
    completename = user_id + ".json"
    with open(os.path.join(save_path, completename), "w") as file:
        file.write(json.dumps(history))
    return
