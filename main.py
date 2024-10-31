import discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$ıklım değışıklığı nedır?'):
        await message.channel.send("cevasbı dklfskldfkdk")
    
   
        
client.run("GİZLİ TOKEN BURAYA")
