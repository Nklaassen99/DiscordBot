# Libraries importeren die nodig zijn om de bot werkend te krijgen
import os
import random

import discord
# Hier probeer ik met dotenv de token veilig te stellen in een apart document, zodat mensen met de source code alleen niet de bot kunne runnen. Deze poging is helaas gefaald sinds ik een onbekende error krijg.
from dotenv import load_dotenv

load_dotenv('token.env')
# Hier staat de Discord TOKEN publiek dus iemand met de code kan de bot meteen runnen
TOKEN = 'NzUyNzk0ODYxOTcwNzg0MjU4.X1c02Q.lBXuGu7l4WHxk7A96y47Qt6ONAA'
# Hier staat de Server naam als variabelen genoteerd. Deze haalt hij wel uit het env bestand. (Deze is meegeleverd
GUILD = os.getenv('DISCORD_GUILD')


client = discord.Client()

# Hier geef ik de bot het commando om een notificatie te geven in de server als er een nieuw iemand in komt.
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} has connected to Discord!')
    print(f'{guild.name}(id: {guild.id})')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

# Hier geef ik de bot het commando om een DM (Direct message) te sturen naar degene die net gejoind is om hem welkom te heten.
    @client.event
    async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Hallo {member.name}, Welkom op in de Discord server, deze word voor nu gebruikt om mij te testen op bruikbaarheid'
        )

#Hier probeer ik de bot te laten reageren op bepaalde commando's, er word gereageerd op 2 commando's met allebei random reacties die staan benoemd hieronder.
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    murat_quotes = [
        'Murat Bozkurt is geen goede ICT\'er',
        'Murat heeft geen verstand van ICT',
        'Murat is waarschijnlijk niet eens aanwezig op school.'
    ]

    simp_response = [
        'Ho eens even, simpen is een way of life. We gaan hier niemand voor op zijn vingers tikken.',
        f'LMFAO {message.author.mention} is een simp voor {random.choice(guild.members)}!'
    ]
# Hier geef ik aan dat het respons wat de bot geeft random is tussen de responses die ik heb opgedragen.
    if message.content == '!Murat':
        response = random.choice(murat_quotes)
        await message.channel.send(response)

    if message.content == '!Simp':
        response = random.choice(simp_response)
        await message.channel.send(response)







client.run(TOKEN)