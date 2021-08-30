# Programmed by DigitDorian
import os
import platform
import distro
import json

from colorama import init
from colorama import Fore, Back, Style
init()

import ASCIICanvas

DebianIcon = open(os.path.dirname(__file__) + "/Characters/Debian.txt", "r")
DebianIconText = Fore.RED + DebianIcon.read()

FetchCanvas = ASCIICanvas.Canvas(32, 9)
FetchCanvas.Initialize()

FetchCanvas.DrawString(DebianIconText, 1, 0)


print("")
FetchCanvas.DrawCanvas()
print(Style.RESET_ALL + " | OS: " + distro.name() + " " + distro.version() + " | DE: " + os.environ.get('DESKTOP_SESSION'))
print("")