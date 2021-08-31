# Programmed by DigitDorian
import os
import platform
import distro
import json
import random

from colorama import init
from colorama import Fore, Back, Style
init()

import ASCIICanvas

# -- INITIALIZATION --

# Static Variables
FetchCanvas = ASCIICanvas.Canvas(80, 9)
FetchCanvas.Initialize()

files = []

for (dirpath, dirnames, filenames) in os.walk(os.path.dirname(__file__) + "/Quotes"):
	files.extend(filenames)

Quote = open(os.path.dirname(__file__) + "/Quotes/" + files[random.randint(-1, len(files) - 1)], "r")

ConfigFile = open(os.path.dirname(__file__) + "/config.json", "r")
Config = json.loads(ConfigFile.read())

# Is it a window manager?
EnvType = ""

if Config["UsesWindowManager"] == True:
    EnvType = " | WM: "
else:
    EnvType = " | DE: "

# Picking the Icon
ComputerDistro = distro.id()
OSColor = Fore.WHITE

if ComputerDistro == "debian":
    OSColor = Fore.RED
elif ComputerDistro == "linuxmint":
    OSColor = Fore.GREEN
else:
    ComputerDistro = "Unknown"
    OSColor = Fore.MAGENTA

Icon = open(os.path.dirname(__file__) + "/Icons/" + ComputerDistro + ".txt", "r")
IconText = Icon.read()

# -- DRAWING TO CANVAS --

# Icon
FetchCanvas.DrawString(IconText, 1, 0, Fore.RED + Style.NORMAL)

# Chat Box
FetchCanvas.ScreenData[0][18] = Fore.WHITE + Style.BRIGHT + "▛"
FetchCanvas.ScreenData[7][18] = Fore.WHITE + Style.BRIGHT + "▙"
for i in range(1, 7):
    FetchCanvas.ScreenData[i][18] = Fore.WHITE + Style.BRIGHT + "▌"
    FetchCanvas.ScreenData[i][79] = Fore.WHITE + Style.BRIGHT + "▐"
FetchCanvas.ScreenData[0][79] = Fore.WHITE + Style.BRIGHT + "▜"
FetchCanvas.ScreenData[7][79] = Fore.WHITE + Style.BRIGHT + "▟"

for i in range(19, 79):
    FetchCanvas.ScreenData[0][i] = Fore.WHITE + Style.BRIGHT + "▀"
    FetchCanvas.ScreenData[7][i] = Fore.WHITE + Style.BRIGHT + "▄"

# Quote
FetchCanvas.DrawString(Quote.read(), 19, 1, Fore.GREEN)

# -- PRESENTATION --
PCInfo = " | OS: " + distro.name(pretty=True) + EnvType + os.environ.get('DESKTOP_SESSION') + " | Shell: " + os.environ['SHELL'].split("/")[-1]

print("")
FetchCanvas.DrawCanvas()
print(Style.RESET_ALL + PCInfo + " |")
print("")
