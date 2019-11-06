import discord
#from discord.ext.commands import Bot

# @bot.command()
# async def 
TOKEN = 'NjI1ODYyMjU0MDc1ODM4NDc0.XcIxZQ.OGO4u6HjmlEimqXLvHopKk78_kg'
# client = Bot()

client = discord.Client()
'''
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('I\'m'):
        mssg = 'Hello {message.conent}'.format(message)
        await client.send_message(message.channel,mssg)
'''
'''
@client.command(name='I\'m',aliases='I am',pass_context=True)
async def joke(context):
    await message.content('Hi, ' + context.message + 'I\'m dad.')
'''
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        pass

def dad_joke(message, client):
    return 'Hello {}, I\'m dad.'.format(message)
dad_joke_command = {
    'trigger': 'I\'m',
    'function': dad_joke,
}



client.run(TOKEN)
