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
    ]
}

def DrawPallete(type, space):
    for i in range(len(palletes[type])):
        print((" " * space) + ''.join(palletes[type][i]))