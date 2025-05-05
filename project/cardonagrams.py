from newest5 import base
from survival_mode3 import survival
from diff_time_mode import time_mode
from xtreme_mode import xtreme_mode

print('Welcome to Anagrams!\nThis is a CS 32 Final Project\nMade by Leo, Tim and Ana')
choice = input("Please choose which cardonagram game you want to play! \nYour options are: basic, survival, time, xtreme: ")
if choice == "basic":
    base()
if choice == "survival":
    survival()
if choice == "time":
    time_mode()
if choice == "xtreme":
    xtreme_mode()
else:
    print("Input a valid gamemode to start")