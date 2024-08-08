import os
import keyHandler
import discord
from discord.ext import commands
import re
import csv

from llama_cpp import Llama
from config import fetchPromptInit
from parseJson import fetchPersona

llm = Llama.from_pretrained(
        repo_id="TheBloke/Llama-2-7B-Chat-GGUF",
        filename="*Q3_K_M.gguf",
        verbose=False,
        # n_gpu_layers = -1, #Uncomment to use GPU accelleration
        # seed = 1337, #Uncomment to set a specific seed
        n_ctx = 2048, #Uncomment to increase the context window
)

description = '''Minerat BOT'''
TOKEN = keyHandler.serve_token()
# intents = discord.Intents.default()
# intents.members = True
# intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
@bot.event
async def on_ready() -> None:
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_message(message:discord.Message) -> None:
    if message.author.bot:
        return
    if message.content == "Hello":
        await message.channel.send("Hi! ")

    await bot.process_commands(message)

@bot.command()
async def ping(ctx: commands.Context) -> None:
    print("ping " + str(bot.latency * 1000) + "ms")
    await ctx.send(f"> Pong! {round(bot.latency * 1000)}ms")

@bot.hybrid_command()
async def echo(ctx: commands.context, message: str) -> None:
    """
    Echoes a message

    Parameters
    ----------
    ctx: commands.Context
        The context of the command invocation
    message: str
        The message to echo
    """
    await ctx.reply(message)

@bot.command()
async def personas(ctx: commands.Context) -> None:
    personasObj = fetchPersona()
    for item in personasObj["persona"]:
        print(item + " --> " + personasObj["persona"][item]["description"])
    await ctx.reply(str(personasObj))



bot.run(TOKEN)

# class myClient(discord.Client):
#     async def on_ready(self):
#         print(f'Logged in as {self.user} (ID: {self.user.id})')
#         print('-----')
# 
#     async def llm():
#         await message.reply("Hello there!")
# 
#     def chatbot_prompt(array, array2):
#         promptInit = array2[1]
#         LLMprompt = array2[0]
#         LLMprompt = str(promptInit) + "Q: " + LLMprompt + " A: "
#         output = llm(
#                 str(LLMprompt), # Prompt
#                 max_tokens = None, # Write "512" to generate up to 512 tokens, set to None to generate up to the end of the context window.
#                 stop = ["Q:"], #Stop generating just before the model would generate a new question.
#                 echo = True,  #Echo the prompt back in the output.
#                 )
#         textOutput = output['choices'][0]['text'].strip()
#         totalTokens = output['usage']['total_tokens']
#         print(textOutput)
#         print("Total tokens: " + str(totalTokens))
#         textOutput = re.sub('(.*\n)*.*A:', '', textOutput)
#         return textOutput
# 
#     async def on_message(self, message):
#         """Receives and interprets messages from the users."""
#         if message.author.id == self.user.id:
#             return
#         if message.content.startswith('!minerat'):
#             textInput = ""
#             array = []
#             elementArray = []
#             textInput = csv.reader([message.content], delimiter=' ', skipinitialspace=True)
#             for i in textInput:
#                     array.append(i)
#             for a in array:
#                 for b in a:
#                     elementArray.append(b)
#             elementArray.pop(0)
#             match elementArray:
#                 case ['--personas']:
#                     await message.channel.send("## Available personas:\n - **Minerat**, a Skaven clanrat with a penchant for mines.\n- **Justicia**, a Zealot in the service of big E himself.\n- ")
#                 case ['--help']:
#                     await message.channel.send("## Available commands:\n **-p** or **--personas**: lists the available personas available for prompts.")
#                 case ['skritchit', prompt]:
#                     personaName = "skritchit"
#                     promptArray = []
#                     promptArray.append(prompt)
#                     print("Your prompt to " + personaName + ": " + prompt)
#                     promptInit = fetchPromptInit(personaName)
#                     promptArray.append(promptInit)
#                     chatbotReply = self.chatbot_prompt(promptArray)
#                     if (len(chatbotReply) >= 2000):
#                         while(len(chatbotReply) >= 1):
#                             chatbotPost = chatbotReply[0:1999]
#                             chatbotReply = chatbotReply[1999:]
#                             await message.reply(chatbotPost)
#                     else: await message.reply(chatbotReply)
#                 case ['ikit', prompt]:
#                     personaName = "ikit"
#                     promptArray = []
#                     promptArray.append(prompt)
#                     print("Your prompt to " + personaName + ": " + prompt)
#                     promptInit = fetchPromptInit(personaName)
#                     promptArray.append(promptInit)
#                     chatbotReply = self.chatbot_prompt(promptArray)
#                     if (len(chatbotReply) >= 2000):
#                         while(len(chatbotReply) >= 1):
#                             chatbotPost = chatbotReply[0:1999]
#                             chatbotReply = chatbotReply[1999:]
#                             await message.reply(chatbotPost)
#                     else: await message.reply(chatbotReply)
#                 case ['justicia', prompt]:
#                     personaName = "justicia"
#                     promptArray = []
#                     promptArray.append(prompt)
#                     print("Your prompt to " + personaName + ": " + prompt)
#                     promptInit = fetchPromptInit(personaName)
#                     promptArray.append(promptInit)
#                     chatbotReply = self.chatbot_prompt(promptArray)
#                     if (len(chatbotReply) >= 2000):
#                         while(len(chatbotReply) >= 1):
#                             chatbotPost = chatbotReply[0:1999]
#                             chatbotReply = chatbotReply[1999:]
#                             await message.reply(chatbotPost)
#                     else: await message.reply(chatbotReply)
#                 case ['deadpool', prompt]:
#                     personaName = "deadpool"
#                     promptArray = []
#                     promptArray.append(prompt)
#                     print("Your prompt to " + personaName + ": " + prompt)
#                     promptInit = fetchPromptInit(personaName)
#                     promptArray.append(promptInit)
#                     chatbotReply = self.chatbot_prompt(promptArray)
#                     if (len(chatbotReply) >= 2000):
#                         while(len(chatbotReply) >= 1):
#                             chatbotPost = chatbotReply[0:1999]
#                             chatbotReply = chatbotReply[1999:]
#                             await message.reply(chatbotPost)
#                     else: await message.reply(chatbotReply)
#                 case ['scriptus', prompt]:
#                     personaName = elementArray[0]
#                     promptArray = []
#                     promptArray.append(prompt)
#                     print("Your prompt to " + personaName + ": " + prompt)
#                     promptInit = fetchPromptInit(personaName)
#                     promptArray.append(promptInit)
#                     chatbotReply = self.chatbot_prompt(promptArray)
#                     if (len(chatbotReply) >= 2000):
#                         while(len(chatbotReply) >= 1):
#                             chatbotPost = chatbotReply[0:1999]
#                             chatbotReply = chatbotReply[1999:]
#                             await message.reply(chatbotPost)
#                     else: await message.reply(chatbotReply)
#                 case ['corpo', prompt]:
#                     personaName = elementArray[0]
#                     promptArray = []
#                     promptArray.append(prompt)
#                     print("Your prompt to " + personaName + ": " + prompt)
#                     promptInit = fetchPromptInit(personaName)
#                     promptArray.append(promptInit)
#                     chatbotReply = self.chatbot_prompt(promptArray)
#                     if (len(chatbotReply) >= 2000):
#                         while(len(chatbotReply) >= 1):
#                             chatbotPost = chatbotReply[0:1999]
#                             chatbotReply = chatbotReply[1999:]
#                             await message.reply(chatbotPost)
#                     else: await message.reply(chatbotReply)
#                 case ['llm', prompt]:
#                     personaName = elementArray[0]
#                     promptArray = []
#                     promptArray.append(prompt)
#                     print("Your prompt to " + personaName + ": " + prompt)
#                     promptInit = fetchPromptInit(personaName)
#                     promptArray.append(promptInit)
#                     chatbotReply = self.chatbot_prompt(promptArray)
#                     if (len(chatbotReply) >= 2000):
#                         while(len(chatbotReply) >= 1):
#                             chatbotPost = chatbotReply[0:1999]
#                             chatbotReply = chatbotReply[1999:]
#                             await message.reply(chatbotPost)
#                     else: await message.reply(chatbotReply)
# 
# 
#                 case other:
#                     print("Bad command.")
# 
# client = myClient(intents=intents)
# client.run(token)
