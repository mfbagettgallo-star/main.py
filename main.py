#de la biblioteca de discord traeme los comando por defecto
from discord.ext import commands
import discord

#traigo los permisos por defecto y los almaceno en la variable
intents = discord.Intents.default()
#el bot pueda leer el contenido del mensaje
intents.message_content = True 

#creamos el bot y lo hacemos mediante la funcion bot
#comands prefijo sirve para que los usuarios si quieren hablar con el bot
#primero deben colocar el '-'
#intents aca le decimos que el bot va a tener estos permisos
bot  = commands.Bot(command_prefix='-', intents=intents)

#acale indicamos que la funcion de abajo sera un evento al que reaccionar
@bot.event
#async def le decimos que la funcion sera asincronica esto es que
#se ejecuta en el momento pero le dice al programa espera ya te respondo
async def en_linea ():

    print(f'Tú bot {bot.user} esta en linea')

#le indica que la funcion de abajo sera un comando propio del bot
@bot.command()
async def hola(ctx):#lo que el usuario mande lo recibe como en un paquete

    #await basicamente que la respuesta va en camino para que
    #el programa no falle. Lo devolvemos como un paquete 'ctx'
    # send es igual a enviar
    await ctx.send('Hola que mas')

@bot.command()
#por parametro tomamos el ctx que es lo que mande el usuario como paquete
# * -> que el usuario puede escribir N cantidad de texto 
#lo que mande el usuario lo vamos a tratar como un string
async def despedirse(ctx, *, mensaje:str):

    #lo que mande el usuario lo pasamos a minuscula y
    #le quitamos los espacios en blanco
    mensaje = mensaje.lower().strip()

    #y en condicionales usamos 'in' y no == porque como el usuaio 
    #puede excribir N cantidad con el 'in' iteramos en el mensaje
    #mientras que el igual solo compara las primeras palabras
    if 'bye' in mensaje:

        await ctx.send('GoodBye')

    elif 'hastaluego' in mensaje:

        await ctx.send('Hasta nunca')

    else:

        await ctx.send('Todo bien, cuidese')
async def jueguitos(ctx, *, juego:str):
    import random


def gen_pass(pass_length):
    contrasenha = contrasenha.lower().strip()
    if 'contraseña' in contrasenha:
        # Generate a password with the specified length
        elements = "+-/*!&$#?=@<>"
        contrasenha = ""


    for i in range(pass_length):
        contrasenha += random.choice(elements)

        return contrasenha
    print(contrasenha)

def gen_emodji():
    emoji = emoji.lower().strip()
    if 'emoji' in emoji:
        emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)


def flip_coin():
    moneda = moneda.lower().strip()
    if 'moneda' in moneda:
        moneda = ["cara!", "sello!"]

        flip = random.randint(0, 1)
        if flip == 0:
            return "cara!"
        else:
            return "sello!"

@bot.command()
async def dado(ctx, dice: str):
    dado = dado.lower().strip()
    if 'dado' in dado:
        
        """hace un lanzamiento de dados de varios numeros que diga el usuario."""
        try:
            dados, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('el formato debe ser de NdN')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

@bot.command()
async def stream(self, ctx, *, url):
    video = video.lower().strip()
    if 'video' in video:
        """pone un video de youtube en el canal de voz por medio de el URL que el usuario mande"""

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
        ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'ahora esta reproduciendo: {player.title}')


#el token lo sacamos de la pagina de desarrolladores de discord
token = 'MTU0OTU3MjQ0Nzg1Mjk2MTkwMw.GU1QkM.SXl-5GDnd0RKVQPTUfDfuhjSesHMTCmbthoKjE'

#cuando ejecutemos este archivo que arranque nuestro bot
#esto debe ser lo ultimo que este
bot.run(token)