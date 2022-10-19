# version 1.0.0
# -*- coding: utf-8 -*-
import os
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame  # it is important to import pygame after that

# need pygame installed - pip install pygame
import time
from pygame import mixer

def clear_console():
    os.system('cls')

pound = u'\u00A3'
clear_console()
print("Seth's spelling test v1.0.0")

print('''   _____      _   _     _        _____            _ _ _               _______        _   
  / ____|    | | | |   ( )      / ____|          | | (_)             |__   __|      | |  
 | (___   ___| |_| |__ |/ ___  | (___  _ __   ___| | |_ _ __   __ _     | | ___  ___| |_ 
  \___ \ / _ \ __| '_ \  / __|  \___ \| '_ \ / _ \ | | | '_ \ / _` |    | |/ _ \/ __| __|
  ____) |  __/ |_| | | | \__ \  ____) | |_) |  __/ | | | | | | (_| |    | |  __/\__ \ |_ 
 |_____/ \___|\__|_| |_| |___/ |_____/| .__/ \___|_|_|_|_| |_|\__, |    |_|\___||___/\__|
                                      | |                      __/ |                     
                                      |_|                     |___/                      ''')

rightAnswers = 0
wrongAnswers = 0
i = 0

# put the selling answerList below!
answerList = ["one","once","ask","friend","school","put","push","pull","full","house","our"]
wordList = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh"]

startSpell = input(f"\nPress Enter to start...\n").lower()

if startSpell == "makefiles":
    f = open("makefiles.bat", "a") # make a bin file for mp3 files
    f.write(":: https://pypi.org/project/gTTS/ \n")
    f.write(f"gtts-cli '{answerList[0]}' --output C:\Audio\{answerList[0]}.mp3 \n")
    f.write(f"gtts-cli '{answerList[1]}' --output C:\Audio\{answerList[1]}.mp3 \n")
    f.write(f"gtts-cli '{answerList[2]}' --output C:\Audio\{answerList[2]}.mp3 \n")
    f.write(f"gtts-cli '{answerList[3]}' --output C:\Audio\{answerList[3]}.mp3 \n")
    f.write(f"gtts-cli '{answerList[4]}' --output C:\Audio\{answerList[4]}.mp3 \n")
    f.write(f"gtts-cli '{answerList[5]}' --output C:\Audio\{answerList[5]}.mp3 \n")
    f.write(f"gtts-cli '{answerList[6]}' --output C:\Audio\{answerList[6]}.mp3 \n")
    f.write(f"gtts-cli '{answerList[7]}' --output C:\Audio\{answerList[7]}.mp3 \n")
    f.write(f"gtts-cli '{answerList[8]}' --output C:\Audio\{answerList[8]}.mp3 \n")
    f.write(f"gtts-cli '{answerList[9]}' --output C:\Audio\{answerList[9]}.mp3 \n")
    f.write(f"gtts-cli '{answerList[10]}' --output C:\Audio\{answerList[10]}.mp3 \n")
    input("makefiles.bat saved! Press Enter to exit...")
    exit()

def play_1():
    clear_console()
    print(f"The {wordList[i]} word is...")
    mixer.init()
    mixer.music.load(f"C:\Audio\{answerList[i]}.mp3")
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)

def repeatWord():
    repNum = 1
    while repNum >= 1:
        hearAgain = input("\nWould you like to hear it again?\n").lower()
        if hearAgain == str("yes"):
            play_1()
        else:
            repNum = 0
            print("\n")

#### Questions ####
def questions():
    global i, wordList, rightAnswers, wrongAnswers
    while i < 11:
        #startSpell = input(f"\nPress any key for the {wordList[i]} word...\n")
        #if startSpell == str("exit"):
        #    exit()
        #else:
        #    play_1()
        #    repeatWord()
        play_1()
        clear_console()
        wordGuess = input(f"Spell the {wordList[i]} word...\n").lower()
        if wordGuess == answerList[i]:
            input("\nCorrect, well done!")
            rightAnswers += 1
            i += 1
        elif wordGuess == str(""):
 #           play_1()
            print("\nPlaying again...\n")      
        else:
            input(f'\nIncorrect! You put "{wordGuess}", the answer is "{answerList[i]}".')
            wrongAnswers += 1
            i += 1

questions()
#### Questions ####


# End of test
if wrongAnswers == 0:
    winner = input(f"\nYou got {rightAnswers} right and {wrongAnswers} wrong!\n")
else:
    loser = input(f"\nYou got {rightAnswers} right and {wrongAnswers} wrong!\n \nBetter luck next time!\n")