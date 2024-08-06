import keyHandler
import discord
from discord.ext import commands
import re
import csv

from llama_cpp import Llama
from config import fetchPromptInit

TOKEN = keyHandler.serve_token()
llm = Llama.from_pretrained(
        repo_id="TheBloke/Llama-2-7B-Chat-GGUF",
        filename="*Q3_K_M.gguf",
        verbose=False,
        # n_gpu_layers = -1, #Uncomment to use GPU accelleration
        # seed = 1337, #Uncomment to set a specific seed
        n_ctx = 2048, #Uncomment to increase the context window
)

description = '''Minerat BOT'''
token = keyHandler.serve_token()
# PROMPT_INIT = f""" {PERSONA_DESC}
# Pretend that you are {PERSONA_NAME}. Below is an instruction that describes a task. Write a response that appropriately completes this task.
# """

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# bot = commands.Bot(command_prefix='!minerat', description=description, intents=intents)

class myClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('-----')

    def chatbot_prompt(array, array2):
        # print(array)
        promptInit = array2[1]
        LLMprompt = array2[0]
        LLMprompt = str(promptInit) + "Q: " + LLMprompt + " A: "
        output = llm(
                str(LLMprompt), # Prompt
                max_tokens = None, # Write "512" to generate up to 512 tokens, set to None to generate up to the end of the context window.
                stop = ["Q:"], #Stop generating just before the model would generate a new question.
                echo = True,  #Echo the prompt back in the output.
                )
        textOutput = output['choices'][0]['text'].strip()
        totalTokens = output['usage']['total_tokens']
        print(textOutput)
        print("Total tokens: " + str(totalTokens))
        textOutput = re.sub('(.*\n)*.*A:', '', textOutput)
        return textOutput

    async def on_message(self, message):
        """Receives and interprets messages from the users."""
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!minerat'):
            textInput = ""
            array = []
            elementArray = []
            textInput = csv.reader([message.content], delimiter=' ', skipinitialspace=True)
            for i in textInput:
                    array.append(i)
            for a in array:
                for b in a:
                    elementArray.append(b)
            elementArray.pop(0)
            match elementArray:
                case ['--personas']:
                    await message.channel.send("## Available personas:\n - **Minerat**, a Skaven clanrat with a penchant for mines.\n- **Justicia**, a Zealot in the service of big E himself.\n- **Cogitatus**, a Mechanicus Enginseer who runs on callous cold logic.")
                case ['--help']:
                    await message.channel.send("## Available commands:\n **-p** or **--personas**: lists the available personas available for prompts.")
                case ['skritchit', prompt]:
                    personaName = "justicia"
                    promptArray = []
                    promptArray.append(prompt)
                    print("Your prompt to " + personaName + ": " + prompt)
                    promptInit = fetchPromptInit(personaName)
                    promptArray.append(promptInit)
                    chatbotReply = self.chatbot_prompt(promptArray)
                    if (len(chatbotReply) >= 2000):
                        while(len(chatbotReply) >= 1):
                            chatbotPost = chatbotReply[0:1999]
                            chatbotReply = chatbotReply[1999:]
                            await message.reply(chatbotPost)
                    else: await message.reply(chatbotReply)
                case ['justicia', prompt]:
                    personaName = "justicia"
                    promptArray = []
                    promptArray.append(prompt)
                    print("Your prompt to " + personaName + ": " + prompt)
                    promptInit = fetchPromptInit(personaName)
                    promptArray.append(promptInit)
                    chatbotReply = self.chatbot_prompt(promptArray)
                    if (len(chatbotReply) >= 2000):
                        while(len(chatbotReply) >= 1):
                            chatbotPost = chatbotReply[0:1999]
                            chatbotReply = chatbotReply[1999:]
                            await message.reply(chatbotPost)
                    else: await message.reply(chatbotReply)
                case ['cogitatus', prompt]:
                    personaName = "cogitatus"
                    promptArray = []
                    promptArray.append(prompt)
                    print("Your prompt to " + personaName + ": " + prompt)
                    promptInit = fetchPromptInit(personaName)
                    promptArray.append(promptInit)
                    chatbotReply = self.chatbot_prompt(promptArray)
                    if (len(chatbotReply) >= 2000):
                        while(len(chatbotReply) >= 1):
                            chatbotPost = chatbotReply[0:1999]
                            chatbotReply = chatbotReply[1999:]
                            await message.reply(chatbotPost)
                    else: await message.reply(chatbotReply)
                case ['deadpool', prompt]:
                    personaName = "deadpool"
                    promptArray = []
                    promptArray.append(prompt)
                    print("Your prompt to " + personaName + ": " + prompt)
                    promptInit = fetchPromptInit(personaName)
                    promptArray.append(promptInit)
                    chatbotReply = self.chatbot_prompt(promptArray)
                    if (len(chatbotReply) >= 2000):
                        while(len(chatbotReply) >= 1):
                            chatbotPost = chatbotReply[0:1999]
                            chatbotReply = chatbotReply[1999:]
                            await message.reply(chatbotPost)
                    else: await message.reply(chatbotReply)
                case ['scriptus', prompt]:
                    personaName = elementArray[0]
                    promptArray = []
                    promptArray.append(prompt)
                    print("Your prompt to " + personaName + ": " + prompt)
                    promptInit = fetchPromptInit(personaName)
                    promptArray.append(promptInit)
                    chatbotReply = self.chatbot_prompt(promptArray)
                    if (len(chatbotReply) >= 2000):
                        while(len(chatbotReply) >= 1):
                            chatbotPost = chatbotReply[0:1999]
                            chatbotReply = chatbotReply[1999:]
                            await message.reply(chatbotPost)
                    else: await message.reply(chatbotReply)
                case ['corpo', prompt]:
                    personaName = elementArray[0]
                    promptArray = []
                    promptArray.append(prompt)
                    print("Your prompt to " + personaName + ": " + prompt)
                    promptInit = fetchPromptInit(personaName)
                    promptArray.append(promptInit)
                    chatbotReply = self.chatbot_prompt(promptArray)
                    if (len(chatbotReply) >= 2000):
                        while(len(chatbotReply) >= 1):
                            chatbotPost = chatbotReply[0:1999]
                            chatbotReply = chatbotReply[1999:]
                            await message.reply(chatbotPost)
                    else: await message.reply(chatbotReply)
                case ['llm', prompt]:
                    personaName = elementArray[0]
                    promptArray = []
                    promptArray.append(prompt)
                    print("Your prompt to " + personaName + ": " + prompt)
                    promptInit = fetchPromptInit(personaName)
                    promptArray.append(promptInit)
                    chatbotReply = self.chatbot_prompt(promptArray)
                    if (len(chatbotReply) >= 2000):
                        while(len(chatbotReply) >= 1):
                            chatbotPost = chatbotReply[0:1999]
                            chatbotReply = chatbotReply[1999:]
                            await message.reply(chatbotPost)
                    else: await message.reply(chatbotReply)


                case other:
                    print("Bad command.")


#            await message.channel.send("Available personas:\n - Minerat, a Skaven clanrat with a penchant for mines.\n- Justicia, a Zealot in the service of big E himself.\n- Cogitatus, a Mechanicus Enginseer who runs on callous cold logic.")
#            print(meassage)
#            print("Available personas:\n - Minerat, a Skaven clanrat with a penchant for mines.\n- Justicia, a Zealot in the service of big E himself.\n- Cogitatus, a Mechanicus Enginseer who runs on callous cold logic.")
            

#    async def repeat(ctx, times: int, content='repeating...'):
#        """Repeats a message multiple times"""
#        for i in range(times):
#            await ctx.send(content)
#
#    async def minerat(ctx, LLMprompt: str):
#        """Sends a prompt to the LLM"""
#        print("Processing: " + LLMprompt)
#        LLMprompt = PROMPT_INIT + "Q: " + LLMprompt + " A: "
#        output = llm(
#                str(LLMprompt), # Prompt
#                max_tokens = None, # Write "512" to generate up to 512 tokens, set to None to generate up to the end of the context window.
#                stop = ["Q:"], #Stop generating just before the model would generate a new question.
#                echo = True,  #Echo the prompt back in the output.
#                )
#        textOutput = output['choices'][0]['text'].strip()
#        totalTokens = output['usage']['total_tokens']
#        print("Total tokens: " + str(totalTokens))
#        textOutput = re.sub('.*\n.*\n.*A:', '', textOutput)
#        print("Q: " + LLMprompt)
#        print("A: " + textOutput)
#        await ctx.channel.send(textOutput)

client = myClient(intents=intents)
client.run(token)
