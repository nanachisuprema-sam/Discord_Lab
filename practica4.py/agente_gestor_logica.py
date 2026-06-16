import discord
from discord.ext import commands
# Importamos las funciones de tu archivo original
import practica04 

# Configuración de permisos de Discord
intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix='!', intents=intents)

lista_tareas_global = []

@bot.event
async def on_ready():
    print("=== Bot de Gestión de Tareas (Discord) ===")
    print(f"Conectado exitosamente como {bot.user}\n")

# --- IMPLEMENTACIÓN DE COMANDOS ---

@bot.command(name="add")
async def add(ctx, *, descripcion: str = ""):
    """Comando para agregar una tarea (!add [texto])"""
    if not descripcion:
        await ctx.send("⚠️ Error: Debes incluir una descripción. Ejemplo: `!add Estudiar Python`")
        return
    
    # Llamamos a la función de tu archivo agente_logica
    respuesta = practica04.agregar_tarea(lista_tareas_global, descripcion)
    await ctx.send(respuesta)

@bot.command(name="list")
async def list_tareas(ctx):
    """Comando para listar las tareas (!list)"""
    respuesta = practica04.listar_tareas(lista_tareas_global)
    await ctx.send(respuesta)

@bot.command(name="del")
async def del_tarea(ctx, numero: str = ""):
    """Comando para eliminar una tarea (!del [numero])"""
    if not numero:
        await ctx.send("⚠️ Error: Debes incluir el número de tarea. Ejemplo: `!del 1`")
        return
        
    respuesta = practica04.eliminar_tarea(lista_tareas_global, numero)
    await ctx.send(respuesta)

# --- MANEJO DE ERRORES (Comando no reconocido pedido por la práctica) ---
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        comando = ctx.invoked_with
        print(f" Error: Comando '!{comando}' no reconocido.")
        # Opcional: Le avisa al usuario en Discord
        await ctx.send(f"❌ Error: Comando `!{comando}` no reconocido.")
    else:
        raise error
#TOKEN = "no me deja agregar"
#bot.run(TOKEN)
