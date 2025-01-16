import discord
from discord.ext import commands
import asyncio

class BotManager:
    def __init__(self, token):
        self.token = token
        self.bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

        @self.bot.event
        async def on_ready():
            print(f"Bot conectado como {self.bot.user}")

        @self.bot.event
        async def on_message(message):
            if message.author == self.bot.user:
                return
            print(f"Mensagem recebida: {message.content}")

    def start_bot(self):
        self.bot.run(self.token)

    def stop_bot(self):
        asyncio.get_event_loop().create_task(self.bot.close())