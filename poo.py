#!/usr/bin/env python3

import os
import asyncio
import random

import discord
from discord.ext import commands

import youtube_dl

from dotenv import load_dotenv

from mcstatus import JavaServer

from mcpi.minecraft import Minecraft

mc = Minecraft.create("85.14.195.116", 4711)


load_dotenv()
MC_SERVER_IP = os.getenv("MC_SERVER_IP")
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="$")
mcserver = JavaServer.lookup(MC_SERVER_IP)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user.name}.")


@bot.command(
    brief="Pings the user",
    help="This thing is self-explanatory, why would you even ask for extra help?",
)
async def ping(ctx):
    await ctx.send("pong")


@bot.command(
    brief="Play a song from YouTube",
    help="Takes a YouTube URL as an argument and joins your current vc to play the audio",
)
async def play(ctx, url):
    voice_clients = {}

    yt_dl_opts = {"format": "bestaudio/best"}
    ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

    ffmpeg_options = {"options": "-vn"}

    msg = ctx.message

    if ctx.author.voice:
        voice_client = await msg.author.voice.channel.connect()
        voice_clients[voice_client.guild.id] = voice_client
    else:
        await ctx.send("You are not connected to a voice channel :poop:")

    try:
        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(
            None, lambda: ytdl.extract_info(url, download=False)
        )

        song = data["url"]
        print("Test")
        player = discord.FFmpegPCMAudio(song, **ffmpeg_options)

        print("Test")
        voice_clients[msg.guild.id].play(player)
    except Exception as err:
        print(err)


@bot.command(
    brief="Leaves current voice channel",
    help="Read the name of the command jesus fucking christ",
)
async def leave(ctx):
    if ctx.author.voice:
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("I am not currently in a voice channel :poop:")


@bot.command(brief="Pauses current audio", help="Just read the name holy")
async def pause(ctx):
    if ctx.author.voice:
        await ctx.guild.voice_client.pause()
    else:
        await ctx.send("I am not currently in a voice channel :poop:")


@bot.command(
    brief="Resume the current audio",
    help="Stop reading the help section and touch some grass",
)
async def resume(ctx):
    if ctx.author.voice:
        await ctx.guild.voice_client.resume()
    else:
        await ctx.send("I am not currently in a voice channel :poop:")


@bot.command(
    brief="Displays status of Minecraft server",
    help="Show the amount of players currently online as well as the ping",
)
async def status(ctx):
    status = mcserver.status()
    await ctx.send(
        f":poop: The MC-server has {status.players.online} player(s) online and replied in {status.latency} ms :poop:"
    )


@bot.command(
    brief="Displays players on Minecraft server",
    help="Show names of all players currently on the Minecraft server",
)
async def players(ctx):
    mc.postToChat("§8[§bPoopy§8]§a: I have fetched server data. beep boop.")
    query = mcserver.query()
    await ctx.send(
        f":poop: The MC-server has the following players online: {', '.join(query.players.names)} :poop:"
    )


@bot.command(
    brief="Show source code of this bot",
    help="Links to the GitHub repository of this bot",
)
async def code(ctx):
    await ctx.send("https://github.com/ybrenning/poopy")


@bot.command(
    brief="Lets PooPy speak",
    help="Sends the user's input to the MC-Server",
)
async def say(ctx, *, message=None):
    out_robot = [
        "beep boop.",
        "*robot noises*",
        "*laughs in robot*",
        "*gears rustling*",
        "zZz.. zZz..",
    ]

    msg_robot = random.choice(out_robot)
    msg = message or msg_robot
    mc.postToChat(f"§8[§bPoopy§8]§a: {msg}")
    await ctx.send(f"Poopy said: {msg}")


if __name__ == "__main__":
    bot.run(TOKEN)
