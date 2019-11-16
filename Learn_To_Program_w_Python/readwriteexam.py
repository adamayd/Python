import os

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:

    myFile.write("Some random text\nMore random text\nAnd some more")

with open("mydata.txt", encoding="utf-8") as myFile:

    lineNum = 1

    while True:

        line = myFile.readline()

        if not line:
            break

        print("Line", lineNum)

        # split
        wordList = line.split()

        # len()
        print("Number of Words: ", len(wordList))

        # loop count characters in the word list
        charCount = 0

        for word in wordList:
            for char in word:
                charCount += 1

        # Divide character count / len word list
        avgNumChars = charCount / len(wordList)

        print("Avg Word Length : {:.2}".format(avgNumChars))

        lineNum += 1