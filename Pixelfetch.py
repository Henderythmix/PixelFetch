# Programmed by DigitDorian
import os
import platform
import distro
import json

from colorama import init
from colorama import Fore, Back, Style
init()

import ASCIICanvas

# Canvas Creation
FetchCanvas = ASCIICanvas.Canvas(32, 9)
FetchCanvas.Initialize()

# Picking the Icon
ComputerDistro = distro.name()
OSColor = Fore.WHITE

if ComputerDistro == "Debian GNU/Linux":
    ComputerDistro = "Debian"
    OSColor = Fore.RED
elif ComputerDistro == "Linux Mint":
    OSColor = Fore.GREEN
else:
    ComputerDistro = "Unknown"
    OSColor = Fore.MAGENTA

Icon = open(os.path.dirname(__file__) + "/Icons/" + ComputerDistro + ".txt", "r")
IconText = OSColor + Icon.read()

# Drawing to Canvas
FetchCanvas.DrawString(IconText, 1, 0)

# Presenting Information
print("")
FetchCanvas.DrawCanvas()
print(Style.RESET_ALL + " | OS: " + distro.name() + " " + distro.version() + " | DE: " + os.environ.get('DESKTOP_SESSION'))
print("")