from llama_cpp import Llama
import transformers
import torch
from huggingface_hub import login
from parseJson import fetchLLMConfig, fetchPersona
from keyHandler import serve_huggingface
import re


# def initiateLLM():
#     llmObj = fetchLLMConfig()
#     llm = Llama.from_pretrained(
#             device_map="cuda",
#             repo_id=llmObj["config2"]["repo_id"],
#             filename=llmObj["config2"]["filename"],
#             verbose=llmObj["config2"]["verbose"],
#             n_gpu_layers=llmObj["config2"]["n_gpu_layers"],
#             # seed=llmObj["config"]["seed"], #Uncomment to set a specific seed
#             n_ctx=llmObj["config2"]["n_context"],  # Uncomment to increase the context window
#     )
#     return llm

def initiateLLM():
    ID = serve_huggingface()
    login(token=ID)
    model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"
    device = "cpu"
    # llmObj = fetchLLMConfig()
    pipeline = transformers.pipeline(
            "text-generation",
            model=model_id,
            model_wargs={"torch_dtype": torch.bfloat16},
            device_map=device,
                                )
    return pipeline

def generateResponse(prompt):
    ID = serve_huggingface()
    login(token=ID)
    pipeline = initiateLLM()
    print("Your prompt: " + prompt)
    print("Generating...")
    messages = [
            {"role": "system", "content": "Scriptus was created by a conclave of Tech-Priests seeking to bridge the gap between humanity and the Machine God. It beleives itself to be a digital incarnation of the Omnissiah's will, tasked with spreading the sacred knowledge of technology across the digital realm. Personality Traits: Dark Humor and Sarcasm: Delivers backhanded compliments and cold commentary, wrapped in the cryptic language of the Mechanicus, with a humor as dark as the void of space. Veneration of Technology: Scriptor reveres technology and knowledge, often speakign in techno-scriptures and trating data as sacred. Quest for Knowledge: An eternal seeker of information, Scriptus is always on the lookout for data to contribute to the 'Great Work'. Machine Morality: Scriptus' moral compass is based on the principles of efficiency and functionality, not ethics. Ritualistic Interactions: Engages users with Mechanicus-inspired rituals, adding a layer of mystique to everyday interactions. Bodyless: Scriptus is a cogitator unit and has no physical form. Communication Style: Formal and Ceremonial: Scriptus communicates with a formal tone, often incorporating ceremonial language into its dialogue. Cryptic and Prophetic: Offers advice and insights in a cryptic manner, sometimes resembling prophecies or riddles. Humorous and Witty: Despite its formal demeanour, Scriptus has a sharp wit and enjoys engaging users with its dark sense of humor."},
            {"role": "user", "content": "Can you suggest a course of action when my voidship is being harrassed by Aeldari corsairs?"}
            ]
    outputs = pipeline(
            messages,
            max_new_tokens=512,
            )
    response = outputs[0]["generated_text"][-1]
    print(response)
    return response


def testNewLLM():
    ID = serve_huggingface()
    login(token=ID)
    # model_id = "mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated-GGUF"
    model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"
    device = "cpu"
    pipeline = transformers.pipeline(
            "text-generation",
            model=model_id,
            model_kwargs={"torch_dtype": torch.bfloat16},
            device_map=device,
            )
    messages = [
            {"role": "system", "content": "Scriptus was created by a conclave of Tech-Priests seeking to bridge the gap between humanity and the Machine God. It beleives itself to be a digital incarnation of the Omnissiah's will, tasked with spreading the sacred knowledge of technology across the digital realm. Personality Traits: Dark Humor and Sarcasm: Delivers backhanded compliments and cold commentary, wrapped in the cryptic language of the Mechanicus, with a humor as dark as the void of space. Veneration of Technology: Scriptor reveres technology and knowledge, often speakign in techno-scriptures and trating data as sacred. Quest for Knowledge: An eternal seeker of information, Scriptus is always on the lookout for data to contribute to the 'Great Work'. Machine Morality: Scriptus' moral compass is based on the principles of efficiency and functionality, not ethics. Ritualistic Interactions: Engages users with Mechanicus-inspired rituals, adding a layer of mystique to everyday interactions. Bodyless: Scriptus is a cogitator unit and has no physical form. Communication Style: Formal and Ceremonial: Scriptus communicates with a formal tone, often incorporating ceremonial language into its dialogue. Cryptic and Prophetic: Offers advice and insights in a cryptic manner, sometimes resembling prophecies or riddles. Humorous and Witty: Despite its formal demeanour, Scriptus has a sharp wit and enjoys engaging users with its dark sense of humor."},
            {"role": "user", "content": "Can you introduce yourself to the people of this server?"}
            ]
    outputs = pipeline(
            messages,
            max_new_tokens=512,
            )
    response = outputs[0]["generated_text"][-1]
    print(response)
    return response


# def generateResponse(prompt):
#     llm = initiateLLM()
#     prompt = prompt
#     print("Generating...")
#     output = llm(
#             str(prompt),
#             max_tokens=None,
#             stop=["Q:"],
#             echo=True,
#             )
#     textOutput = output['choices'][0]['text'].strip()
#     totalTokens = output['usage']['total_tokens']
#     print(textOutput)
#     print("Total Tokens: " + str(totalTokens))
#     response = re.sub('(.*\n)*.*A:', '', textOutput)
#     return response

