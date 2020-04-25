import os
import discord
import random
import asyncio
import youtube_dl
from dotenv import load_dotenv
from youtube_search.yt import YT
from youtube_search.yt import YTDLSource
from discord.ext import commands
from discord.utils import get

load_dotenv()

token = os.getenv('Discord_Token')
guildx = os.getenv('Discord_Guild')
new_channel_id = os.getenv("New_Channel_ID")
bot = commands.Bot(command_prefix = '!')
client = discord.Client()

resultsx = []
players = {}
queue = []

@bot.command(name='play')
async def play(ctx, *args):
    if ctx.message.author.voice == None:
        await ctx.send('Join a voice channel before using this command.')
    else:     
        user_channel = ctx.message.author.voice.channel
        if args[0] == '1':
            if len(resultsx) == 0:
                await ctx.send('Please make a request before choosing a number.')
            else:
                url = 'https://www.youtube.com' + resultsx[0][1]
                if ctx.voice_client != None:
                    if ctx.voice_client.is_playing():
                        queue.append(url)
                        await ctx.send('Your request was added to the queue.')
                else:
                    if ctx.voice_client != user_channel and ctx.voice_client != None:
                        if ctx.voice_client.is_playing() == False:
                            vc = await ctx.voice_client.move_to(user_channel)
                            player = await YTDLSource.from_url(url)
                            vc.play(player)
                            resultsx.clear()
                        else:
                            await ctx.send('Sorry, I am playing music in another channel.')
                    elif ctx.voice_client != user_channel:
                        vc = await user_channel.connect()
                        player = await YTDLSource.from_url(url)
                        vc.play(player)
                        resultsx.clear()
                    else:
                        vc = ctx.voice_client
                        player = await YTDLSource.from_url(url)
                        vc.play(player)
                        resultsx.clear()
        elif args[0] == '2':
            if len(resultsx) == 0:
                await ctx.send('Please make a request before choosing a number.')
            else:
                url = 'https://www.youtube.com' + resultsx[1][1]
                if ctx.voice_client != None:                
                    if ctx.voice_client.is_playing():
                        queue.append(url)
                        await ctx.send('Your request was added to the queue.')
                else:                            
                    if ctx.voice_client != user_channel and ctx.voice_client != None:
                        if ctx.voice_client.is_playing() == False:
                            vc = await ctx.voice_client.move_to(user_channel)
                            player = await YTDLSource.from_url(url)
                            vc.play(player)
                            resultsx.clear()
                        else:
                            await ctx.send('Sorry, I am playing music in another channel.')
                    elif ctx.voice_client != user_channel:
                        vc = await user_channel.connect()
                        player = await YTDLSource.from_url(url)
                        vc.play(player)
                        resultsx.clear()
                    else:
                        vc = ctx.voice_client
                        player = await YTDLSource.from_url(url)
                        vc.play(player)
                        resultsx.clear()
        elif args[0] == '3':
            if len(resultsx) == 0:
                await ctx.send('Please make a request before choosing a number.')
            else:
                url = 'https://www.youtube.com' + resultsx[2][1]
                if ctx.voice_client != None:                
                    if ctx.voice_client.is_playing():
                        queue.append(url)
                        await ctx.send('Your request was added to the queue.')
                else:                
                    if ctx.voice_client != user_channel and ctx.voice_client != None:
                        if ctx.voice_client.is_playing() == False:
                            vc = await ctx.voice_client.move_to(user_channel)
                            player = await YTDLSource.from_url(url)
                            vc.play(player)
                            resultsx.clear()
                        else:
                            await ctx.send('Sorry, I am playing music in another channel.')
                    elif ctx.voice_client != user_channel:
                        vc = await user_channel.connect()
                        player = await YTDLSource.from_url(url)
                        vc.play(player)
                        resultsx.clear()                    
                    else:
                        vc = ctx.voice_client
                        player = await YTDLSource.from_url(url)
                        vc.play(player)
                        resultsx.clear()
        elif args[0] == '4':
            if len(resultsx) == 0:
                await ctx.send('Please make a request before choosing a number.')
            else:
                url = 'https://www.youtube.com' + resultsx[3][1]
                if ctx.voice_client != None:                
                    if ctx.voice_client.is_playing():
                        queue.append(url)
                        await ctx.send('Your request was added to the queue.')
                else:                 
                    if ctx.voice_client != user_channel and ctx.voice_client != None:
                        if ctx.voice_client.is_playing() == False:
                            vc = await ctx.voice_client.move_to(user_channel)
                            player = await YTDLSource.from_url(url)
                            vc.play(player)
                            resultsx.clear()
                        else:
                            await ctx.send('Sorry, I am playing music in another channel.')
                    elif ctx.voice_client != user_channel:
                        vc = await user_channel.connect()
                        player = await YTDLSource.from_url(url)
                        vc.play(player)
                        resultsx.clear()                    
                    else:
                        vc = ctx.voice_client
                        player = await YTDLSource.from_url(url)
                        vc.play(player)
                        resultsx.clear()
        elif args[0] == '5':
            if len(resultsx) == 0:
                await ctx.send('Please make a request before choosing a number.')
            else:
                url = 'https://www.youtube.com' + resultsx[4][1] 
                if ctx.voice_client != None:                
                    if ctx.voice_client.is_playing():
                        queue.append(url)
                        await ctx.send('Your request was added to the queue.')
                else:                 
                    if ctx.voice_client != user_channel and ctx.voice_client != None:
                        if ctx.voice_client.is_playing() == False:
                            vc = await ctx.voice_client.move_to(user_channel)
                            player = await YTDLSource.from_url(url)
                            vc.play(player)
                            resultsx.clear()
                        else:
                            await ctx.send('Sorry, I am playing music in another channel.')
                    elif ctx.voice_client != user_channel:
                        vc = await user_channel.connect()
                        player = await YTDLSource.from_url(url)
                        vc.play(player)
                        resultsx.clear()                    
                    else:
                        vc = ctx.voice_client
                        player = await YTDLSource.from_url(url)
                        vc.play(player)
                        resultsx.clear()
        else:                        
            seperator = ' '
            search_query = seperator.join(args)
            results = YT(search_query, max_results = 5).export()
            resultsx.append(results[0])
            resultsx.append(results[1])
            resultsx.append(results[2])
            resultsx.append(results[3])
            resultsx.append(results[4])
            output = '''1. {name1}\n2. {name2}\n3. {name3}\n4. {name4}\n5. {name5}\
            '''.format(name1=results[0][0], name2=results[1][0], name3=results[2][0], name4=results[3][0], name5=results[4][0])
            await ctx.send(output)

@bot.command(name='url', pass_context=True)
async def url(ctx, url):
    if ctx.message.author.voice == None:
        await ctx.send('Join a voice channel before using this command.')
    else:
        user_channel = ctx.message.author.voice.channel
        if url.startswith('https://www.youtube.com/watch?v=') or url.startswith('www.youtube.com/watch?v='):
            if ctx.voice_client != None:
                if ctx.voice_client.is_playing():
                    queue.append(url)
                    await ctx.send('Your request was added to the queue.')
            else: 
                if ctx.voice_client != user_channel and ctx.voice_client != None:
                    if ctx.voice_client.is_playing() == False:
                        vc = await ctx.voice_client.move_to(user_channel)
                        player = await YTDLSource.from_url(url)
                        vc.play(player)
                    else:
                        await ctx.send('Sorry, I am playing music in another channel.')
                elif ctx.voice_client != user_channel:
                    vc = await user_channel.connect()
                    player = await YTDLSource.from_url(url)
                    vc.play(player)
                else:
                    vc = ctx.voice_client
                    player = await YTDLSource.from_url(url)
                    vc.play(player)
        else:
            await ctx.send('Please send valid YouTube URL.')

@bot.command(name='pause')
async def play(ctx):
    if ctx.voice_client is None:
        messages = ['Dumb shit.', 'I need to be playing music to pause, you nonce.', 'Brainless fuck.']
        await ctx.send(random.choice(messages))
    elif ctx.voice_client.is_playing():
        if ctx.voice_client.channel != ctx.message.author.voice.channel:
            await ctx.send('Join my voice channel to pause.')
        else:
            await ctx.voice_client.pause()
    else:
            await ctx.send('I am already paused.')

#@bot.event
#async def on_message(message):
    #if
        #await ctx.send('Haha Jay is gay!')

@bot.command(name='state')
async def state(ctx):
    await ctx.send(ctx.message.author.voice)
    await ctx.send(ctx.voice_client.is_playing())

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel and before.channel is not None:
        if len(before.channel.members) == 1 and before.channel.guild.me in before.channel.members:
            voice_client = get(bot.voice_clients, channel=before.channel)
            if voice_client:
                await voice_client.disconnect()

    if before.channel is not None and before.channel == after.channel and member == after.channel.guild.me:
        if after.channel.guild.voice_client.is_playing() == False:
            if len(queue) > 0:
                voice_client = get(bot.voice_clients, channel = after.channel)
                player = await YTDLSource.from_url(queue[0])
                await voice_client.play(player)
                queue.pop[0]



bot.run(token)
