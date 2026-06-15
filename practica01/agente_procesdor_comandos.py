import datetime
import discord
from discord.ext import commands
import procesador_procesador

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

HORA_INICIO = datetime.datetime.now()
NOMBRE_BOT = "Susanita"

@bot.event
async def on_ready():
    """Se ejecuta cuando el bot se conecta a Discord exitosamente."""
    print(f"Bot conectado como {bot.user}")
    print(procesador_procesador.obtener_saludo(NOMBRE_BOT))

@bot.command(name="saludo")
async def saludo(ctx):
    """Comando !saludo: Llama a obtener_saludo del archivo base."""
    respuesta = procesador_procesador.obtener_saludo(NOMBRE_BOT)
    await ctx.send(respuesta)

@bot.command(name="uptime")
async def uptime(ctx):
    """Comando !uptime: Llama a calcular_uptime del archivo base."""
    respuesta = procesador_procesador.calcular_uptime(HORA_INICIO)
    await ctx.send(respuesta)

@bot.command(name="ayuda_bot")
async def ayuda_bot(ctx):
    """Comando !ayuda_bot: Llama a mostrar_ayuda del archivo base."""
    respuesta = procesador_procesador.mostrar_ayuda()
    await ctx.send(respuesta)

bot.run('token (no me deja subirlo lol)')
