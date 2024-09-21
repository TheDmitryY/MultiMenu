from art import *
from colorama import Fore,Style
from colorama import init
import os
import time
import webbrowser
webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))

def Text_Menu():
    print(Fore.LIGHTMAGENTA_EX + "[1] Virus Total      [8] Youtube"),
    print("[2] Gamma            [9] Gmail" + Fore.LIGHTMAGENTA_EX),
    print("[3] GitHub           [10] Google Disk" + Fore.LIGHTMAGENTA_EX),
    print("[4] Stack Overflow   [11] LeetCode" + Fore.LIGHTMAGENTA_EX),
    print("[5] Canva            [12] CodeWars" + Fore.LIGHTMAGENTA_EX),
    print("[6] Jutsu            [13] Habr" + Fore.LIGHTMAGENTA_EX)
    print("[7] Roblox           [14] TikTok" + Fore.LIGHTMAGENTA_EX)
    print(Fore.LIGHTCYAN_EX)
    chose = int(input("\n [$] Choose operation -->  "))
    if chose == 1:
        site = 'https://www.virustotal.com'
        webbrowser.open(site)
    elif chose == 2:
        site = 'https://gamma.app/'
        webbrowser.open(site)

    elif chose == 3:
        site = 'https://github.com/'
        webbrowser.open(site)

    elif chose == 4:
        site = 'https://stackoverflow.com/'
        webbrowser.open(site)

    elif chose == 5:
        site = 'https://www.canva.com/uk_ua/'
        webbrowser.open(site)

    elif chose == 6:
        site = 'https://jut.su/'
        webbrowser.open(site)

    elif chose == 7:
        site = 'roblox.com/home'
        webbrowser.get('Chrome').open(site)

    elif chose == 8:
        site = 'https://www.youtube.com/'
        webbrowser.get('Chrome').open(site)

    elif chose == 9:
        site = 'https://mail.google.com/mail/'
        webbrowser.open(site)


    elif chose == 10:
        site = 'https://drive.google.com/'
        webbrowser.open(site)

    elif chose == 11:
        site = 'https://leetcode.com/'
        webbrowser.open(site)

    elif chose == 12:
        site = 'https://www.codewars.com/'
        webbrowser.open(site)

    elif chose == 13:
        site = 'https://habr.com/ru/articles/'
        webbrowser.open(site)

    elif chose == 14:
        site = 'https://www.tiktok.com/uk-UA/'
        webbrowser.open(site)

def Logo():
    Clear()
    tprint("Multi Menu")
    print(Fore.LIGHTCYAN_EX + "Author:     [ HorekiSun ]")
    print(Fore.LIGHTYELLOW_EX + "Version:     [ 1.0.0 ]")
    print(Fore.LIGHTGREEN_EX + "Time:     " + " [ " + time.asctime() + " ] ")
    print(Fore.LIGHTWHITE_EX + "GitHub:     [ @TheDmitryY  ]")
    print(Style.RESET_ALL + "\n")

def Clear():
    os.system('cls')