import discord
# from dotenv import load_dotenv

import os

#from discord.ext.commands import Bot

# @bot.command()
# async def 
#load_dotenv()
token = 'NjI1ODYyMjU0MDc1ODM4NDc0.XcMFhQ.BR7Jhlxc161O_nGbLsuXe67QNFA'
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
    
    if 'I\'m' in message.content:
        msg = message.content
        msg = msg[msg.find('I\'m')+4::]
        dad_joke = 'Hello {}, I\'m dad.'.format(msg)
        await message.channel.send(dad_joke)
        # await client.process_commands(msg)
# add i'm, I am, im, IM
'''
def dad_joke(message, client):
    return 'Hello {}, I\'m dad.'.format(message)
dad_joke_command = {
    'trigger': 'I\'m',
    'function': dad_joke,
}
'''



client.run(token)
