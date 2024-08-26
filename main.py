import keyHandler
import discord
from discord.ext import commands
from parseJson import fetchPersona
from imageGen import generateImage
from languageModel import generateResponse, testNewLLM


TOKEN = keyHandler.serve_token()
# intents = discord.Intents.default()
# intents.members = True
# intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready() -> None:
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")


@bot.event
async def on_message(message: discord.Message) -> None:
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
async def image(ctx: commands.Context, prompt: str) -> None:
    imageFilePath = generateImage(prompt)
    await ctx.reply(file=discord.File(imageFilePath))


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


@bot.command()
async def test(ctx: commands.Context) -> None:
    response = testNewLLM()
    await ctx.reply(response)


@bot.hybrid_command()
async def prompt(ctx: commands.Context, message: str) -> None:
    """
    Takes a prompt and passes it to the LLM for a response.

    Parameters
    ----------
    ctx: commands.Context
        The context of the command invocation
    message: str
        The message that is passed to the LLM as a prompt.
    """
    response = generateResponse(message)
    if (len(response) >= 2000):
        while (len(response) >= 1):
            chatbotPost = response[0:1999]
            response = response[1999:]
            await ctx.reply(chatbotPost)
    else:
        await ctx.reply(response)


bot.run(TOKEN)
