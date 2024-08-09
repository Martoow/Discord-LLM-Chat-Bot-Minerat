from llama_cpp import Llama
from parseJson import fetchLLMConfig, fetchPersona
import re


def initiateLLM():
    llmObj = fetchLLMConfig()
    llm = Llama.from_pretrained(
            repo_id=llmObj["config"]["repo_id"],
            filename=llmObj["config"]["filename"],
            verbose=llmObj["config"]["verbose"],
            # n_gpu_layers=llmObj["config"]["n_gpu_layers"], #Uncomment to use GPU accelleration
            # seed=llmObj["config"]["seed"], #Uncomment to set a specific seed
            n_ctx=llmObj["config"]["n_context"],  # Uncomment to increase the context window
    )
    return llm


def constructPost(prompt):
    """
    Takes the prompt from the user, passes it to the language model, constructs a response and sends it back to the main function to be posted to the relevant channel.
    """
    personaObj = fetchPersona()
    name = personaObj["persona"]["scriptus"]["name"]
    definition = personaObj["persona"]["scriptus"]["definition"]
    print("Your prompt to " + name + ": " + prompt)
    promptInit = f'''{definition!s} Pretend your are {name!s}. Below is an instruction that describes a task, write a response that appropriately completes the task.'''
    prompt = promptInit + " Q: " + prompt
    response = generateResponse(prompt)
    return response


def generateResponse(prompt):
    llm = initiateLLM()
    prompt = prompt
    print("Generating...")
    output = llm(
            str(prompt),
            max_tokens=None,
            stop=["Q:"],
            echo=True,
            )
    textOutput = output['choices'][0]['text'].strip()
    totalTokens = output['usage']['total_tokens']
    print(textOutput)
    print("Total Tokens: " + str(totalTokens))
    response = re.sub('(.*\n)*.*A:', '', textOutput)
    return response
