# version 1.0.0
# -*- coding: utf-8 -*-
import os
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame  # it is important to import pygame after that
# need pygame installed - pip install pygame
import time
from pygame import mixer

from gtts import gTTS

def clear_console():
    os.system('clear')

pound = u'\u00A3'
clear_console()

import os.path
directory_exists = os.path.exists('.\Audio')
# directory_exists = os.listdir(r'.\Audio')
# print(directory_exists) # checks if the Audio folder is there or not, if not tries to create it.
if directory_exists == False:
    os.mkdir('Audio')

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

# put the sellings in the answerList below!
answerList = ["one","once","ask","friend","school","put","push","pull","full","house","our"]
###############
wordList = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh"]
wrongAnsList = ["WRONG ANSWERS...", "\n"]
numAns = len(answerList)

#startSpell = input(f"\nPress Enter to start...\n").lower()

def makefiles():
    global i, answerList, numAns
    while i < numAns:
        tts = gTTS(answerList[i])
        tts.save(f'.\Audio\{answerList[i]}.mp3')
        i += 1

# Checking if mp3 files exist...
file_exists = os.path.exists(f'.\Audio\{answerList[0]}.mp3')
if file_exists == True:
    input("\nAudio files found. \n\nPress Enter to start...\n")
else:
    print("\nNo audio files found. Creating audio files...")
    makefiles()
    input("Audio files created! \n\nPress Enter to start...\n")
    i = 0

def play_1():
    clear_console()
    print(f"The {wordList[i]} word is...")
    mixer.init()
    mixer.music.load(f".\Audio\{answerList[i]}.mp3")
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
    global i, wordList, rightAnswers, wrongAnswers, wrongAnsList
    while i < numAns:
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
            wrongAnsList.append(wordGuess + " " + answerList[i] + "\n")
            wrongAnswers += 1
            i += 1

questions()

# End of test
if wrongAnswers == 0:
    clear_console()
    f = open("PASSED.txt", "a") # output a text file for results
    f.write(f"PASSED! {answerList}\n")
    winner = input(f"You got {rightAnswers} right and {wrongAnswers} wrong!\n")
else:
    clear_console()
    f = open("ATTEMPTS.txt", "a") # output a text file for results
    f.write(f"ATTEMPTS! {wrongAnsList}\n")
    print(f"You got {rightAnswers} right and {wrongAnswers} wrong!\n")
    print(*wrongAnsList)
    loser = input("\nBetter luck next time!\n")
    