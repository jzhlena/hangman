import random
import hangman_words

print("Welcome to Hangman!")

givenWord = random.choice((hangman_words.word_list))
temp = ''
currWord = givenWord
unchangingWord = givenWord
numLives = 6

for i in givenWord:
    temp += '_'
print(temp)

currGuess = ''
while(currWord != '' and numLives > 0):
    currGuess = input("Please guess a letter: ")
    if len(currGuess) != 1:
        print("That was not a letter!")
        continue
    else:
        count = 0
        print("")
        print(f"+++++ {numLives} LIVES REMAINING +++++")
        for i in range(len(givenWord)):
            if givenWord[i] == currGuess:
                temp = temp[:i] + currGuess + temp[i + 1:]
                givenWord = givenWord[:i] + "_" + givenWord[i+1:]
                currWord = currWord.replace(currGuess, '')
                print(temp)
                print(currGuess + " was in the word!")
                break
            else:
                count+=1
        if count == len(givenWord):
            print(currGuess + " was not in the word!")
            numLives -= 1
        print("+++++                   +++++")
        print("")

if numLives == 0:
    print("You have lost!")
    print("The word was " + unchangingWord)
else:
    print("You have won!")


