# PooPy

Contains source code for the current version of the **PooPy** Discord bot.
This bot can take various commands via a Discord server's text channel and perform simple tasks. \
An overview of the different possible commands can be displayed by typing `$help` in one of the server's
text channels.

> Note: In order to use the bot, you must connect it with your Guild using the 
> [Discord Developer Portal](https://discord.com/developers/docs/intro) in order to
> obtain a corresponding `TOKEN`.

## Instructions

First, clone this repository locally:

```bash
$ git clone https://github.com/ybrenning/poopy.git
$ cd poopy
```

Install the requirements

```bash
$ pip install -r requirements.txt
```

Open `.env` and edit the `DISCORD_TOKEN` variable. \
_If you want to connect a Minecraft Server of your choice, change the `MC_SERVER_IP`
variable as well._

```bash
$ code .env

# Or, on Linux CSH:
$ setenv DISCORD_TOKEN [your-discord-token]
```

Run the Python script

```bash
# On Linux
$ ./poo.py

# On Windows/Mac OS
$ python poo.py
```

## References

[Discord Developer Portal](https://discord.com/developers/docs/intro) \
[DiscordPy](https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html) \
[MC-Status](https://github.com/py-mine/mcstatus)
