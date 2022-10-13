# version 1.0.0
# -*- coding: utf-8 -*-

pound = u'\u00A3'

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

# put the selling items below!
answerOne = str("one")
answerTwo = str("two")
answerThree = str("three")
answerFour = str("four")
answerFive = str("five")
answerSix = str("six")
answerSeven = str("seven")
answerEight = str("eight")
answerNine = str("nine")
answerTen = str("ten")

wordOne = input("Spell the first word...\n")

if wordOne == answerOne:
    print("\nCorrect, well done!")
    rightAnswers += 1
else:
    print(f'\nIncorrect! You put "{wordOne}", the answer is "{answerOne}"')
    wrongAnswers += 1

# End of test
if wrongAnswers == 0:
    print("\nWell done! Here is your vbucks code XXXX-XXXX-XXXX-XXXX\n")
else:
    print(f"\nYou got {rightAnswers} right and {wrongAnswers} wrong!\n")