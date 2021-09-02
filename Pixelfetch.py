# Programmed by DigitDorian
import os, platform, json, random

try:
    import distro
except:
    print("pip3 install distro")
    exit(1)
try:
    from colorama import init, Fore, Back, Style
except:
    print("pip3 install colorama")
    exit(1)

import ASCIICanvas


## Initialization ##
init()

# Static Variables
Canvas = ASCIICanvas.Canvas(80, 9)
Canvas.Initialize()
ExePath = os.path.dirname(__file__) 
QuotesPath = os.path.join(ExePath, "Quotes")
IconsPath = os.path.join(ExePath, "Icons")
ConfigPath = os.path.join(ExePath, "config.json")


Quotes = os.listdir(QuotesPath)
with open(os.path.join(QuotesPath, random.choice(Quotes)), 'r') as QuoteFile:
    Quote = QuoteFile.read()


## Read Config File ##
try:
    with open(ConfigPath, 'r', encoding='utf8') as ConfigFile:
        Config = json.load(ConfigFile)
except FileNotFoundError:
    raise FileNotFoundError("Could not found file \"config.json\"")


## Get Distro Icon ##
try:
    with open(os.path.join(IconsPath, distro.id()), 'r') as IconFile:
        Icon = IconFile.read()
except FileNotFoundError:
    with open(os.path.join(IconsPath, "unknown"), 'r') as IconFile:
        Icon = IconFile.read()
 

## GUI ENV ##
EnvType = ""

if Config["UsesWindowManager"] == True:
    EnvType = " | WM: "
else:
    EnvType = " | DE: "


## DRAWING TO CANVAS ##
# Icon
Canvas.DrawString(Icon, 1, 0, Fore.RED + Style.NORMAL)

# Text Box
Canvas.ScreenData[0][18] = Fore.WHITE + Style.BRIGHT + "▛"
Canvas.ScreenData[7][18] = Fore.WHITE + Style.BRIGHT + "▙"
for i in range(1, 7):
    Canvas.ScreenData[i][18] = Fore.WHITE + Style.BRIGHT + "▌"
    Canvas.ScreenData[i][79] = Fore.WHITE + Style.BRIGHT + "▐"
Canvas.ScreenData[0][79] = Fore.WHITE + Style.BRIGHT + "▜"
Canvas.ScreenData[7][79] = Fore.WHITE + Style.BRIGHT + "▟"

for i in range(19, 79):
    Canvas.ScreenData[0][i] = Fore.WHITE + Style.BRIGHT + "▀"
    Canvas.ScreenData[7][i] = Fore.WHITE + Style.BRIGHT + "▄"

# Quote
Canvas.DrawString(Quote, 19, 1, Fore.GREEN)


## PRESENTATION ##
PCInfo = " | OS: " + distro.name(pretty=True) +  " | Shell: " + os.environ['SHELL'].split("/")[-1]

print("")
Canvas.DrawCanvas()
print(Style.RESET_ALL + PCInfo + " |")
print("")
