from pynput.keyboard import Key, Controller
import time, sys

if(len(sys.argv) < 2):
    print("Please provide a source file!")
    quit(1)

sourceFileName = sys.argv[1]

print("Reading from file: " + sourceFileName)

wordsToType = []

with open(sourceFileName, "r") as sourceFile:
    for line in sourceFile:
        if len(line.strip()) == 0 or line.strip() == " ":
            continue
        words = line.split(" ")
        for w in words:
            wordsToType.append(w)
    sourceFile.close()

print("The bombardment begins in 2s")
time.sleep(2)

keyboard = Controller()

for word in wordsToType:
    keyboard.type(word)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1.2)