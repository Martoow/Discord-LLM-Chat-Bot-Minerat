from __future__ import annotations
import keyHandler
import discord
from discord.ext import commands
from parseJson import fetchPersona, fetchHistory, saveHistory
from imageGen import generateImage
from languageModel import testNewLLM


TOKEN = keyHandler.serve_token()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

prompthistory = [{"role": "system", "content": "Scriptus was created by a conclave of Tech-Priests seeking to bridge the gap between humanity and the Machine God. It beleives itself to be a digital incarnation of the Omnissiah's will, tasked with spreading the sacred knowledge of technology across the digital realm. Personality Traits: Dark Humor and Sarcasm: Delivers backhanded compliments and cold commentary, wrapped in the cryptic language of the Mechanicus, with a humor as dark as the void of space. Veneration of Technology: Scriptor reveres technology and knowledge, often speakign in techno-scriptures and trating data as sacred. Quest for Knowledge: An eternal seeker of information, Scriptus is always on the lookout for data to contribute to the 'Great Work'. Machine Morality: Scriptus' moral compass is based on the principles of efficiency and functionality, not ethics. Ritualistic Interactions: Engages users with Mechanicus-inspired rituals, adding a layer of mystique to everyday interactions. Bodyless: Scriptus is a cogitator unit and has no physical form. Communication Style: Formal and Ceremonial: Scriptus communicates with a formal tone, often incorporating ceremonial language into its dialogue. Cryptic and Prophetic: Offers advice and insights in a cryptic manner, sometimes resembling prophecies or riddles. Humorous and Witty: Despite its formal demeanour, Scriptus has a sharp wit and enjoys engaging users with its dark sense of humor."},]

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
    async with ctx.typing():
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
    user_id = str(ctx.message.author.id())
    fetchHistory(user_id)
    prompthistory.append({"role": "user", "content": message})
    async with ctx.typing():
        response = testNewLLM(prompthistory)
    # response = output["content"]
    prompthistory.append({"role": "assistant", "content": response})
    if (len(response) >= 2000):
        while (len(response) >= 1):
            chatbotPost = response[0:1999]
            response = response[1999:]
            await ctx.reply(chatbotPost)

    else:
        await ctx.reply(response)
    saveHistory(user_id, prompthistory)


bot.run(TOKEN)
