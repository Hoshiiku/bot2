import discord
from bot_logic import gen_pass
import random

coin = 0
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    global coin
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith("generate password"):
        await message.channel.send(f"Your password is {gen_pass(10)}")

    elif message.content.startswith("how are you doing?"):
        await message.channel.send("I'm doing good, and you?")
    elif message.content.startswith("Throw a coin"):
        coin = random.randint(1, 2)
        if coin == 1:
            await message.channel.send("The face that shows is heads")
        else:
            await message.channel.send("The face that shows is tails")
    
    else:
        await message.channel.send(message.content)

    

client.run("MAIN TOKEN GOES HERE")

