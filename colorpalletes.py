# The only purpose of this program is to store instructions on how 
# to draw colour palletes for a console program

# Nothing super fancy lol

from colorama import init, Fore, Back, Style

init()

palletes = {
    "None": [" "],
    "Basic": [
        [Fore.BLACK + "███", Fore.RED + "███", Fore.GREEN + "███", Fore.YELLOW + "███", Fore.BLUE + "███", Fore.MAGENTA + "███", Fore.CYAN + "███", Fore.WHITE + "███"],
        [Style.BRIGHT + Fore.BLACK + "███", Fore.RED + "███", Fore.GREEN + "███", Fore.YELLOW + "███", Fore.BLUE + "███", Fore.MAGENTA + "███", Fore.CYAN + "███", Fore.WHITE + "███"]
    ],
    "Gradient": [
        [Fore.BLACK + "░▒▓", Back.RED + "███▓▒░", Fore.RED + Back.GREEN + "███▓▒░", Fore.GREEN + Back.BLUE + "███▓▒░", Fore.BLUE + Back.MAGENTA + "███▓▒░", Fore.MAGENTA + Back.CYAN + "███▓▒░", Fore.CYAN + Back.WHITE + "███▓▒░   ", Fore.WHITE + Back.RESET + "▓▒░"],
        [Fore.BLACK + "░▒▓", Back.RED + "███▓▒░", Fore.RED + Back.GREEN + "███▓▒░", Fore.GREEN + Back.BLUE + "███▓▒░", Fore.BLUE + Back.MAGENTA + "███▓▒░", Fore.MAGENTA + Back.CYAN + "███▓▒░", Fore.CYAN + Back.WHITE + "███▓▒░   ", Fore.WHITE + Back.RESET + "▓▒░"]
    ]
}

def DrawPallete(type, space):
    for i in range(len(palletes[type])):
        print(Style.RESET_ALL + (" " * space) + ''.join(palletes[type][i]))