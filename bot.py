# bot.py
import os
import time

import discord
from dotenv import load_dotenv
import pyautogui
import pydirectinput

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('Connected as {0.user}'.format(client))

@client.event
async def on_message(message):
    keyboard_input = message.content.lower()
    if keyboard_input == 'a':
        print('pressing a')
        pydirectinput.press('z')
    if keyboard_input == 'b':
        print('pressing b')
        pydirectinput.press('x')
    if keyboard_input == 'l':
        print('pressing l')
        pydirectinput.press('a')
    if keyboard_input == 'r':
        print('pressing r')
        pydirectinput.press('s')
    if keyboard_input == 'select':
        print('pressing select')
        pydirectinput.press('backspace')
    if keyboard_input == 'start':
        print('pressing start')
        pydirectinput.press('enter')
    if keyboard_input == 'up':
        print('pressing up')
        pydirectinput.keyDown('up')
        time.sleep(0.1)
        pydirectinput.keyUp('up')
    if keyboard_input == 'down':
        print('pressing down')
        pydirectinput.keyDown('down')
        time.sleep(0.1)
        pydirectinput.keyUp('down')
    if keyboard_input == 'left':
        print('pressing left')
        pydirectinput.keyDown('left')
        time.sleep(0.1)
        pydirectinput.keyUp('left')
    if keyboard_input == 'right':
        print('pressing right')
        pydirectinput.keyDown('right')
        time.sleep(0.1)
        pydirectinput.keyUp('right')


client.run(os.getenv('TOKEN'))
