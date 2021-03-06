import discord
# from dotenv import load_dotenv

import os
import random
#from discord.ext.commands import Bot

# @bot.command()
# async def 
#load_dotenv()

token = os.environ['ENV_TOKEN']
# client = Bot()
client = discord.Client()

'''
class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} is connected to Discord')
client = CustomClient()
'''
'''
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('I\'m'):
        msg = 'Hello {}'.format(message.content)
        await client.send_message(message.channel,msg)
'''
'''
@client.command(name='I\'m',aliases='I am',pass_context=True)
async def joke(context):
    await message.content('Hi, ' + context.message + 'I\'m dad.')
'''

@client.event
async def on_ready():
    print('Bot is ready')
    # print(client.user.name)
    # print(client.user.id)
    # print('------')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if 'i\'m' in message.content.lower() or 'i am' in message.content.lower() or 'im' in message.content.lower():
        msg = message.content
        msg = msg[msg.find('I\'m')+4::]
        dad_joke = 'Hello {}, I\'m dad.'.format(msg)
        await message.channel.send(dad_joke)
    if 'dad' in message.content.lower() or 'father' in message.content.lower():
        dad_sayings = [
            'Ok buddy, I\'m getting cigarettes, I\'ll be right back.',
            'You\'re adopted.', 'Not now, I am working.',
            'Do your homework', 'When I was your age...', 'We took Fido to grandma\'s ranch upstate',
            'Kids these days'
        ]
        answer = random.choice(dad_sayings)
        await message.channel.send(answer)
    if 'hard' in message.content.lower() or 'sucks' in message.content.lower() or 'difficult' in message.content.lower() or 'I hate' in message.content.lower():
        replies = ['This will build character.', 'That\'s life']
        his_reply = random.choice(replies)
        await message.channel.send(his_reply)
        # await client.process_commands(msg)
# add i'm, I am, im, IM



client.run(token)
