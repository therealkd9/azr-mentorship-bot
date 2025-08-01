import discord
import os
from dotenv import load_dotenv
import openai

load_dotenv()

print("DISCORD TOKEN IS:", repr(os.getenv("DISCORD_TOKEN")))  # Debug line

openai.api_key = os.getenv("OPENAI_API_KEY")
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name == "🤖ask-azr-bot":
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are Ask AZR, the official AI coach for AZR University students. Always give simple, tactical, and motivating answers about Amazon FBA, OA, RA, and wholesale."},
                {"role": "user", "content": f"{message.content}"}
            ],
            max_tokens=500,
            temperature=0.3
        )
        await message.channel.send(response['choices'][0]['message']['content'])

client.run(os.getenv("DISCORD_TOKEN"))



