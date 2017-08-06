import MusicNotes
import Songs

import winsound

from colorama import Fore, Back, Style, init

init(autoreset=True)

def cen():
    #\t\t\t\t\t
    return "\t\t"
def cl(color):
    if color == "g":
        return Style.BRIGHT + Fore.GREEN
    elif color == "r":
        return Style.BRIGHT + Fore.RED
    elif color == "b":
        return Style.BRIGHT + Fore.BLUE
    elif color == "y":
        return Style.BRIGHT + Fore.YELLOW
    elif color == "m":
        return Style.BRIGHT + Fore.MAGENTA
    elif color == "c":
        return Style.BRIGHT + Fore.CYAN
    elif color == "w":
        return Style.BRIGHT + Fore.WHITE
def mainmenu():
    print()
    print(cen() + cl("w") + "Hello. Welcome to this fancy music program\n")
    print(cen() + cl("w") + "We hope you will enjoy your time here.\n")
    print(cen() + cl("w") + "Please enter your choice of song:\n")
    return menucomponents()
def menu():
    print()
    print(cen() + cl("w") + "Select another option:\n")
    return menucomponents()
def menucomponents():
    print(cen() + cl("m") + "1. Eminor Study\n")
    print(cen() + cl("b") + "2. Mary had a little lamb\n")
    print(cen() + cl("c") + "3. Mario Theme Song\n")

    print(cen() + cl("w") + "(Enter the number\n")
    print(cen() + cl("w") + "q to exit the program\n")
    return input()


# Program Starts here
loop = 1
userinput = mainmenu()
bl = 0
if userinput != "q":
    bl = 1

while(loop == 1):
    if bl == 0:
        userinput = menu()
    if userinput == "1":
        Songs.Song1()
        bl = 0
    elif userinput == "2":
        Songs.Song2()
        bl = 0
    elif userinput == "3":
        Songs.Mario()
        bl = 0
    elif userinput == "4":
        MusicNotes.lowcnote()
        bl = 0
    else:
        loop = 0

print(Style.RESET_ALL)
