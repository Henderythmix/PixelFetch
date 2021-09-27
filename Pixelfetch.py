import os, platform, json, random

try:
    import distro
except:
    print("pip3 install distro")
    exit(1)
try:
    from colorama import init, Fore, Back, Style
    init() # this function belongs to the colorama module so I'm putting it here
except:
    print("pip3 install colorama")
    exit(1)

import ASCIICanvas
import colorpalletes

# Static Variables
FetchCanvas = ASCIICanvas.Canvas(80, 9)
FetchCanvas.Initialize()
ExePath = os.path.dirname(__file__)
QuotesPath = os.path.join(ExePath, "Quotes")
IconsPath = os.path.join(ExePath, "Icons")
ConfigPath = os.path.join(ExePath, "config.json")

# -- File Reading --
# Quotes
Quotes = os.listdir(QuotesPath)
with open(os.path.join(QuotesPath, random.choice(Quotes)), 'r') as QuoteFile:
    Quote = QuoteFile.read()

# Config File
try:
    with open(ConfigPath, 'r', encoding='utf8') as ConfigFile:
        Config = json.load(ConfigFile)
except FileNotFoundError:
    raise FileNotFoundError("Could not found file \"config.json\"")

# Icon
try:
    with open(os.path.join(IconsPath, f"{distro.id()}.txt"), 'r') as IconFile:
        Icon = IconFile.read()
        KnownDis = {
                "arch": Fore.LIGHTCYAN_EX,
                "debian": Fore.RED,
                "linuxmint": Fore.GREEN,
                "ubuntu": Fore.YELLOW
        }
        OSColor = KnownDis[distro.id()]
except FileNotFoundError:
    with open(os.path.join(IconsPath, "unknown.txt"), 'r') as IconFile:
        Icon = IconFile.read()
        OSColor = Fore.WHITE

# Other PC Info
EnvType = " | WM: " if Config["UsesWindowManager"] == True else "| DE:"

Shell = os.getenv("SHELL").split('/')[-1] # Get the name of the shell
OsFullName = distro.name(pretty=True)     # Get the full name of the distro

# -- DRAWING TO CANVAS --

# Icon
FetchCanvas.DrawString(Icon, 1, 0, OSColor + Style.NORMAL)

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
FetchCanvas.DrawString(Quote, 19, 1, Fore.GREEN)

# -- PRESENTATION --

# Fetch Data
print("")
FetchCanvas.DrawCanvas()
print(f"{Style.RESET_ALL} OS: {OsFullName} {EnvType} {os.environ.get('DESKTOP_SESSION')} | Shell: {Shell}")
# I know he got rid of the DE but I'm still doing that as the owner of the project for now. We can find a variable alternative when we do.
print("")

# Color Pallete - All the work for this is in colorpalletes.py
colorpalletes.DrawPallete(Config["Shell"], 5)
print("")