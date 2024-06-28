import discord
from discord.ext import commands

def get_token():
    token = Non
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()  # Eliminar espacios en blanco al principio y al final
            return token

TOKEN = get_token()

# definir variables para el bot:
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

# cuando el bot entra en linea:
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# cuando se recibe un mensaje:
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignore messages sent by the bot itself
    
    if 'hola' in message.content.lower():
        # Responde al mensaje con un saludo
        await message.channel.send(f'Hola {message.author.mention}!')

    # Aquí puedes agregar cualquier lógica para procesar los mensajes recibidos
    # Por ejemplo, imprimir el contenido del mensaje en la consola:
    print(f'Message from {message.author}: {message.content}')

    await bot.process_commands(message)# Esto es necesario para que los comandos sigan funcionando

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(TOKEN)

