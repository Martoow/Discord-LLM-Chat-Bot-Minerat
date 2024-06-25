import keyHandler
import discord
from discord.ext import commands
import re

from llama_cpp import Llama
from config import *

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
print(token + "0")
PROMPT_INIT = f""" {PERSONA_DESC}
Pretend that you are {PERSONA_NAME}. Below is an instruction that describes a task. Write a response that appropriately completes this task.
"""

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('-----')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a die, NdN-format"""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times"""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def minerat(ctx, LLMprompt: str):
    """Sends a prompt to the LLM"""
    print(LLMprompt)
    LLMprompt = PROMPT_INIT + "Q: " + LLMprompt + " A: "
    output = llm(
            str(LLMprompt), # Prompt
            max_tokens = None, # Write "512" to generate up to 512 tokens, set to None to generate up to the end of the context window.
            stop = ["Q:"], #Stop generating just before the model would generate a new question.
            echo = True,  #Echo the prompt back in the output.
            )
    textOutput = output['choices'][0]['text'].strip()
    totalTokens = output['usage']['total_tokens']
    print("Total tokens: " + str(totalTokens))
    textOutput = re.sub('.*\n.*\n.*A:', '', textOutput)
    print(textOutput)
    await ctx.channel.send(textOutput)

bot.run(token)
