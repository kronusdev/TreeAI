import os
from pydoc import describe
from transformers import pipeline
from dotenv import load_dotenv
import interactions
import transformers

def getGenerator():
    return pipeline('text-generation', model='EleutherAI/gpt-neo-125M')

def getResponse(generator, prompt, length):
    response = generator(prompt, max_length=length, do_sample=True, temperature=0.8)
    return response[0]['generated_text']

if __name__ == "__main__":

    # get the .env variables loaded
    load_dotenv()
    # get the Discord stuff sorted
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('GUILD_ID')
    bot =  interactions.Client(token=TOKEN)

    print(f'.env initialized...\nTOKEN: {TOKEN}\nGUILD_ID: {GUILD}')
    
    generator = getGenerator()
    print(f'generator initialized...')

    @bot.command(
        name="prompt",
        description="submit a prompt to get a response from TreeAI!",
        scope=int(GUILD),
        options=[
            interactions.Option(
                name="message",
                description="What you want to generate a response based upon.",
                type=interactions.OptionType.STRING,
                required=True
            ),
            interactions.Option(
                name="max_length",
                description="What is the maximum word length of your response? (50-150)",
                type=interactions.OptionType.INTEGER,
                required=True,
                min_value=50,
                max_value=150
            )
        ]
    )
    async def prompt(ctx: interactions.CommandContext, generator: transformers.pipeline, message: str, max_length: int):
        await ctx.defer(ephemeral=False)
        resp = getResponse(generator, message, max_length)
        await ctx.send(resp)

    print('starting bot...')
    bot.start()