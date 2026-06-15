import discord
from discord.ext import commands
import tareas_agente 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

MIS_TAREAS = []

@bot.event
async def on_ready():
    print(f"Bot de tareas conectado como {bot.user}")

@bot.command(name="add")
async def add(ctx, *, descripcion: str = ""):
    """Comando !add [tarea]: Agrega una nueva tarea."""
    if not descripcion:
        await ctx.send("Error: Debes escribir una descripción para la tarea. Ejemplo: !add Estudiar Git")
        return
        
    respuesta = tareas_agente.agregar_tarea(MIS_TAREAS, descripcion)
    await ctx.send(respuesta)

@bot.command(name="list")
async def list_tareas(ctx):
    """Comando !list: Muestra todas las tareas guardadas."""
    # Llamamos a tu función listar_tareas
    respuesta = tareas_agente.listar_tareas(MIS_TAREAS)
    await ctx.send(respuesta)

@bot.command(name="delete")
async def delete(ctx, indice: str = ""):
    """Comando !delete [número]: Elimina una tarea por su índice."""
    if not indice:
        await ctx.send("Error: Debes indicar el número de tarea a eliminar. Ejemplo: !delete 1")
        return
        
    respuesta = tareas_agente.eliminar_tarea(MIS_TAREAS, indice)
    await ctx.send(respuesta)

bot.run('no_me_deja_poner_token')
