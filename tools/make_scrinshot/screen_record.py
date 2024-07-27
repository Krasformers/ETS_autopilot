#!/usr/bin/python3

# -*- coding:utf-8 -*-

# script for recording screenshot
# 
# default folder for save screenshot `screens`


from PIL import ImageGrab
import time
import os


ABSOLUTE_SCREENSHOT_FOLDER_PATH = 'screens'
FPS = 1

if not os.path.isdir(ABSOLUTE_SCREENSHOT_FOLDER_PATH):
    os.mkdir(ABSOLUTE_SCREENSHOT_FOLDER_PATH)

start_num = 0
screens_list = os.listdir(ABSOLUTE_SCREENSHOT_FOLDER_PATH)
if len(screens_list) != 0:
    screens_list = [int(i.replace('.png','')) for i in screens_list]
    start_num = max(screens_list) + 1

if FPS <= 0:
    raise ValueError("FPS should have been greater than zero")

while True:
    screenshot = ImageGrab.grab()
    screenshot.save(os.path.join(ABSOLUTE_SCREENSHOT_FOLDER_PATH, f'{start_num}.png'))
    start_num += 1
    time.sleep(1 / FPS)
