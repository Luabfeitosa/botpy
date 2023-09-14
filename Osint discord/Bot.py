import discord 
import responses


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
        
    except Exception as e:
        print(e)
        
        
def run_discord_bot():
    TOKEN = 'MTE1MTk2MTIxMDMzMDMwNDU2Mw.GJ7rl8.3mejlymmTBhBZ_WSUFLVrZx4GLz-RYisTaacu8'  
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)                                                                