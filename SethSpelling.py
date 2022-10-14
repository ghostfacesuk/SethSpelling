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

print("   _____      _   _     _        _____            _ _ _               _______        _   ")
print("  / ____|    | | | |   ( )      / ____|          | | (_)             |__   __|      | |  ")
print(" | (___   ___| |_| |__ |/ ___  | (___  _ __   ___| | |_ _ __   __ _     | | ___  ___| |_ ")
print("  \___ \ / _ \ __| '_ \  / __|  \___ \| '_ \ / _ \ | | | '_ \ / _` |    | |/ _ \/ __| __|")
print("  ____) |  __/ |_| | | | \__ \  ____) | |_) |  __/ | | | | | | (_| |    | |  __/\__ \ |_ ")
print(" |_____/ \___|\__|_| |_| |___/ |_____/| .__/ \___|_|_|_|_| |_|\__, |    |_|\___||___/\__|")
print("                                      | |                      __/ |                     ")
print("                                      |_|                     |___/                      ")

rightAnswers = 0
wrongAnswers = 0
i = 0

# put the selling answerList below!
answerList = ["one","two","three","four","five","six","seven","eight","nine","ten"]
wordList = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

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
        hearAgain = input("\nWould you like to hear it again?\n")
        if hearAgain == str("yes"):
            play_1()
        else:
            repNum = 0
            print("\n")

#### Questions ####
def questions():
    global i, wordList, rightAnswers, wrongAnswers
    while i < 10:
        startSpell = input(f"\nPress any key for the {wordList[i]} word...\n")
        if startSpell == str("exit"):
            exit()
        else:
            play_1()
            repeatWord()
        clear_console()
        wordGuess = input(f"Spell the {wordList[i]} word...\n")
        if wordGuess == answerList[i]:
            print("\nCorrect, well done!")
            rightAnswers += 1
            i += 1
        else:
            print(f'\nIncorrect! You put "{wordGuess}", the answer is "{answerList[i]}".')
            wrongAnswers += 1
            i += 1

questions()
#### Questions ####


# End of test
if wrongAnswers == 0:
    winner = input(f"\nYou got {rightAnswers} right and {wrongAnswers} wrong!\n")
else:
    loser = input(f"\nYou got {rightAnswers} right and {wrongAnswers} wrong! Better luck next time!\n")

