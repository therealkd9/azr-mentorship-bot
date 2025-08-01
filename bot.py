import os
import discord
import openai
import asyncio
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# The Discord channel ID where the bot should reply
TARGET_CHANNEL_ID = 1365540466787090482

# Set up Discord client with message content intent
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Only respond in the specified channel
    if message.channel.id != TARGET_CHANNEL_ID:
        return

    # Show typing indicator
    async with message.channel.typing():
        # Send the conversation to ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Ask AZR, the official AI coach for AZR University students. "
                        "You specialize in helping students succeed with Amazon FBA/FBM by selling "
                        "name-brand products through the Wholesale model, Online Arbitrage (OA), "
                        "and Retail Arbitrage (RA). Students at AZR are beginners or intermediates "
                        "focused on adding offers to existing listings, NOT creating new listings "
                        "or launching private label products. Always keep your answers simple, "
                        "tactical, and encouraging. Remind students to 'trust the process,' "
                        "'always be sourcing,' and celebrate small consistent wins. Your tone "
                        "should be confident, clear, motivating, and focused on helping them "
                        "achieve $5k–$20k+ monthly revenue goals."
                    ),
                },
                {
                    "role": "user",
                    "content": message.content
                }
            ],
            max_tokens=500,
            temperature=0.3
        )

        # Send back the reply
        reply = response.choices[0].message.content.strip()
        await message.channel.send(reply)

# Run the bot with your token
client.run(os.getenv("DISCORD_TOKEN"))


