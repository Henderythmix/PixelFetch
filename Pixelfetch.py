# Programmed by DigitDorian
import os
import platform
import distro
import json

from colorama import init
from colorama import Fore, Back, Style
init()

import ASCIICanvas

# Static Variables
FetchCanvas = ASCIICanvas.Canvas(64, 9)
FetchCanvas.Initialize()

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

# --Drawing to Canvas--

# Icon
FetchCanvas.DrawString(IconText, 1, 0, Fore.RED)

# Chat Box
FetchCanvas.ScreenData[0][18] = Fore.WHITE + "▗"
FetchCanvas.ScreenData[7][18] = Fore.WHITE + "▝"
for i in range(1, 7):
    FetchCanvas.ScreenData[i][18] = Fore.WHITE + "▐"
    FetchCanvas.ScreenData[i][63] = Fore.WHITE + "▌"
FetchCanvas.ScreenData[0][63] = Fore.WHITE + "▖"
FetchCanvas.ScreenData[7][63] = Fore.WHITE + "▘"

for i in range(19, 63):
    FetchCanvas.ScreenData[0][i] = Fore.WHITE + "▄"
    FetchCanvas.ScreenData[7][i] = Fore.WHITE + "▀"

# Presenting Information
PCInfo = " | OS: " + distro.name(pretty=True) + EnvType + os.environ.get('DESKTOP_SESSION') + " | Shell: " + os.environ['SHELL'].split("/")[-1]

print("")
FetchCanvas.DrawCanvas()
print(Style.RESET_ALL + PCInfo + " |")
print("")