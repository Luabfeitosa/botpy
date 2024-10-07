import discord
import os
import requests
from discord.ext import commands
from bs4 import BeautifulSoup
import asyncio
from credentials import secrets

api_key = secrets.get('API_KEY')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

async def buscar_informacoes_sobre_CS2():
    url = 'https://www.threads.net/search?q=uva' 

    try: 
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            
            publicacoes = soup.find_all('div', class_='post')

            resultados = []
            for publicacao in publicacoes:
                if 'CS2' in publicacao.get_text().lower():
                    resultados.appendappend(publicacao.get_text())

            if len(resultados) == 0:       
                return "Nenhuma publicação encontrada."

            return '\n\n' .join(resultados[:5]) 
        
        else:
            return f"Erro ao acessar o Threads: {response.status_code}"
    except Exception as e:
        return f"Erro ao buscar informações: {e}"    

async def enviar_mensagem_periodicamente():
    await client.wait_until_ready()
    channel = client.get_channel(1292373783411163167)
    

    while not client.is_closed():
        informacao = await buscar_informacoes_sobre_CS2 ()


        await channel.send(f"Informações sobre CS2: {informacao}")

        await asyncio.sleep(30)

@client.event
async def on_ready():
    print(f'{client.user} está online e conectado ao Discord!')


class MyClient(discord.Client):
    async def setup_hook(self) -> None:
        self.bg_task = self.loop.create_task(enviar_mensagem_periodicamente())



client = MyClient(intents=intents)    
client.run(api_key)