import discord
intents = discord.Intents.default()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
    

client = discord.Client(intents=discord.Intents.default())
client.run('MTE1MTk3NjI3MDM5NDA1MjczOQ.G4Rl-Y.s7talVoW5jH8A3oFM3TPZkbfzsekfIZ9XPofkw')