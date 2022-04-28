import os
from transformers import pipeline
from dotenv import load_dotenv
import discord
import interactions

def getGenerator():
    return pipeline('text-generation', model='EleutherAI/gpt-neo-125M')

def getResponse(generator, prompt, length, temp):
    response = generator(prompt, max_length=length, do_sample=True, temperature=temp)
    return response[0]['generated_text']

if __name__ == "__main__":

    # get the .env variables loaded
    load_dotenv()
    # get the Discord stuff sorted
    TOKEN = os.getenv('DISCORD_TOKEN')
    client = discord.Client()

    # get that generator
    generator = getGenerator()

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    client.run(TOKEN)
