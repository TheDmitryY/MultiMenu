from art import *
from colorama import Fore,Style
from colorama import init
import os
import time
from func import Logo, Text_Menu, Clear
import webbrowser

init()

if __name__ == '__main__':
    while True:
        Logo()
        Text_Menu()
        repeat = input(Fore.LIGHTBLUE_EX + "\n[$] Your wanna repeat? [ Yes/No] :  ")
        if repeat != "Yes":
            Clear()
            break