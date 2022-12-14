# Hangman Attempt 2, Multiwords

import random    # import the random function
import myColours  # import my colours
import myTuple  # import my tuple wordlist

wordlist = myTuple.wordlist  # make it easier to access my tuple
print(chr(27)+"[2J")
# clear console

myColours.myGreen()
print("We are going to play hangman ")
myColours.myLightPurple()
print("I will be picking one of these words for you to guess ")

for word in wordlist:
    myColours.myPurple()  # change to purple colour
    print("It could be", end=" ")  # display all word in mytuple
    print(word, " ", end=" ")
myColours.myYellow()

input("\nPress Enter to continue...")
print(chr(27)+"[2J")
# clear console

word = random.choice(wordlist)  # choose random word from tuple
word = word.lower()
attempts = 0  # attempts number
starprint = str("")  # create new string called starprint
usedchar = []
addone = 1
pos = 0  # used to iterate through the chars of the selected word from mytuple

for char in word:
    if char == "_":
        # now this and adds a _ for each space to starprint string
        starprint = starprint + "_"

    else:
        # now this and adds a * for each letter to starprint string
        starprint = starprint + "*"

while attempts <= 9:  # give user 10 attempts to guess word

    myColours.myRed()  # change to red from imported module
    print(starprint)  # print the string starprint
    myColours.myCyan()  # change to cyan from imported module

    print("Used letters: ", usedchar)
    print("\nAttempt number:", attempts+1, "out of 10")
    guess = input("Take a guess : ")[0]  # user takes a guess
    for i in usedchar:

        if i == guess:
            print("You have already guessed ", guess, "try again")
            addone = 0
        else:
            print()
            addone = 1

    usedchar += guess

    pos = 0  # used to iterate through the chars of the selected word from mytuple

    for x in word:  # iterate through the choosen word

        if guess == x:  # and check if guess is valid

            # print("The letter " + guess + " is used in position ",pos+1)  # if valid display position in word

            # change char in string to the guess
            starprint = starprint[:pos] + guess + starprint[pos+1:]

            if starprint == word:
                myColours.myPurple()  # change colours to red
                print("Game over, You Win!")  # print victory message
                print("The word was " + word)
                print("\033[m  ")     # change back to default colours
                # wait for user to press enter before clearing the screen
                input("press Enter to exit")
                print(chr(27)+"[2J")  # clear screen
                quit()  # end program
            else:
                # print("The letter " + guess + " is not used in position",pos+1)  # starprint not equal word, continue
                print()

        pos = pos + 1  # increse position in word by 1

    if addone == 1:
        attempts = attempts + 1  # increse number of attempts by 1
    else:
        print()

myColours.myRed()  # change colour to red
print("Game Over , You Loose!")  # print defeat message
print("The word was " + word)
print("\033[m  ")  # change back to default colours
# wait for user to press enter before clearing the screen
input("press Enter to exit")
print(chr(27)+"[2J")  # clear screen
