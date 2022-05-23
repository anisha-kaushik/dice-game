#Author: Anisha Kaushik
#Date: November 25, 2019

print ("Anisha Kaushik, Dice Game")

import random

def getUserInput():

    # ask for the first time, if correct then return the output
    userInput = input()
    if userInput.upper() == 'YES':
      return True

    if userInput.upper() == 'NO':
      return False

    # keep asking until yes or no is given
    while userInput.upper() != 'YES' and userInput.upper() != 'NO':
        print('I am sorry, invalid choice, please input yes/no')
        userInput = input()

        if userInput.upper() == 'YES':
          return True

        if userInput.upper() == 'NO':
          return False


# checks if user input name is valid
def validateName(name):

    loopCounter = 0
    validInput = False
    length = len(inputName)

    while loopCounter < length:
            if inputName[loopCounter].isalpha():
                validInput = True
            else:
                validInput = False
                break
            loopCounter = loopCounter + 1
    
    return validInput


# check for pattern 1
def patternOne(diceOne, diceTwo, diceThree, diceFour, diceFive):
    isPatternOne = False
    if diceOne == diceTwo == diceThree == diceFour == diceFive:
        print("All dices are equal, user can earn 100 points")
        isPatternOne = True
    return isPatternOne


# checks if number is prime number
def patternTwo( n ):
    prime = True

    loop = 2
    while loop < n:
        if n % loop ==0:
            prime = False
        loop += 1

    if prime == True:
        print("All dices add up to a prime number, user can earn 50 points")
    return prime


# check if three out of 5 dice are same number
def patternThree(diceOne, diceTwo, diceThree, diceFour, diceFive):

    threeSame = False
    diceList = [diceOne, diceTwo, diceThree, diceFour, diceFive]

    for i in range(0, 5):
        for j in range(0,5):
            for k in range(0,5):
                if i != j and j != k and k != i:
                    if diceList[i] == diceList[j] and diceList[j] == diceList[k] and diceList[i] == diceList[k]:
                        threeSame = True
                        print("3 out of 5 dices have same value (30 points)")
                        return threeSame



# check if all numbers are unique
def patternFour(diceOne, diceTwo, diceThree, diceFour, diceFive):
    diceList = [diceOne, diceTwo, diceThree, diceFour, diceFive]

    for i in range(0, 5):
        for j in range(0,5):
            if i != j:
                if diceList[i] == diceList[j]:
                    return False

    print("all dices are different number, user can earn 25 points")
    return True

# Get user input and check if it is valid
validInput = False
inputName = input("Welcome to my game, what is your first name? ")
validInput = validateName(inputName)

while validInput == False:
    if validInput == False:
        inputName = input("I am sorry, names are only allowed to contain letters. Please re-enter: ")
        validInput = validateName(inputName)

print("\nThank you, ",inputName, ", you start with 0 points, lets play!")


# Game starts here
playerScore = 0 # counts the player score
gameCounter = 1 # counts how many turns the player has

while gameCounter <= 10:
    print("\n\nTurn", gameCounter, ": ")
    print("You rolled 5 dice.")

    diceOne = random.randint(1,6)
    diceTwo = random.randint(1,6)
    diceThree = random.randint(1,6)
    diceFour = random.randint(1,6)
    diceFive = random.randint(1,6)

    # found total of dice
    totalDiceScore = diceOne + diceTwo + diceThree + diceFour + diceFive
    print("Their values are ", diceOne, diceTwo, diceThree, diceFour, diceFive, "\n")

    # check for pattern 1
    isPatternOne = False
    isPatternOne = patternOne(diceOne, diceTwo, diceThree, diceFour, diceFive)

    # check for pattern 2
    isPatternTwo = False
    isPatternTwo = patternTwo(totalDiceScore)

    # check for pattern 3
    isPatternThree = False
    isPatternThree = patternThree(diceOne, diceTwo, diceThree, diceFour, diceFive)

    # check for pattern 4
    isPatternFour = False
    isPatternFour = patternFour(diceOne, diceTwo, diceThree, diceFour, diceFive)
        
    # All the patterns are checked, now we need to give the user which option to choose
    if isPatternOne == True:
        if 100 > totalDiceScore:
            print("Would you like to score the pattern points for all 5 dice having the same value? (100 points) [yes/no]")
            userInput = getUserInput()

            if userInput == True:
                playerScore = playerScore + 100
                print("You score is now", playerScore, ", end of turn ", gameCounter)
                gameCounter = gameCounter + 1
                continue

    if isPatternTwo == True:
        if 50 > totalDiceScore:
            print("Would you like to score the pattern points for all 5 dice add up to prime number? (50 points) [yes/no]")
            userInput = getUserInput()

            if userInput == True:
                playerScore = playerScore + 50
                print("You score is now", playerScore, ", end of turn ", gameCounter)
                gameCounter = gameCounter + 1
                continue

    if isPatternThree == True:
        if 30 > totalDiceScore:
            print("Would you like to score the pattern points for 3 of the 5 dice have same value? (30 points) [y/n]")
            userInput = getUserInput()

            if userInput == True:
                playerScore = playerScore + 30
                print("You score is now", playerScore, ", end of turn ", gameCounter)
                gameCounter = gameCounter + 1
                continue

    if isPatternFour == True:
        if 25 > totalDiceScore:
            print("Would you like to score the pattern points for all 5 dice have different value? (25 points) [y/n]")
            userInput = getUserInput()

            if userInput == True:
                playerScore = playerScore + 25
                print("You score is now", playerScore, ", end of turn ", gameCounter)
                gameCounter = gameCounter + 1
                continue

    print("Would you like to score the sum of the dices? (", totalDiceScore ," points) [y/n]" )
    userInput = getUserInput()

    if userInput == True:
        playerScore = playerScore + totalDiceScore
        print("You score is now", playerScore, ", end of turn ", gameCounter)
        gameCounter = gameCounter + 1
        continue


    # user selected none of the options, now we need to ask him to reroll the dice and see which options he chooses
    # then based on the new outcomes, we will ask him again which options he chooses

    reroll = False
    rerollCount = 0
    while rerollCount < 2:
        print("Would you like to reroll dice 1? [yes/no]" )
        userInput = getUserInput()
        if userInput == True:
            diceOne = random.randint(1,6)
            reroll = True

        print("Would you like to reroll dice 2? [yes/no]" )
        userInput = getUserInput()
        if userInput == True:
            diceTwo = random.randint(1,6)
            reroll = True

        print("Would you like to reroll dice 3? [yes/no]" )
        userInput = getUserInput()
        if userInput == True:
            diceThree = random.randint(1,6)
            reroll = True

        print("Would you like to reroll dice 4? [yes/no]" )
        userInput = getUserInput()
        if userInput == True:
            diceFour = random.randint(1,6)
            reroll = True

        print("Would you like to reroll dice 5? [yes/no]" )
        userInput = getUserInput()
        if userInput == True:
            diceFive = random.randint(1,6)
            reroll = True

        # check for the patterns again
        totalDiceScore = diceOne + diceTwo + diceThree + diceFour + diceFive
        isPatternOne = patternOne(diceOne, diceTwo, diceThree, diceFour, diceFive)
        isPatternTwo = patternTwo(totalDiceScore)
        isPatternThree = patternThree(diceOne, diceTwo, diceThree, diceFour, diceFive)
        isPatternFour = patternFour(diceOne, diceTwo, diceThree, diceFour, diceFive)


        if rerollCount == 1:
            reroll = False
            if isPatternOne == True:
                if 100 > totalDiceScore:
                  print("Value of all dice is the same, therefore you get 100 points.")
                  playerScore = playerScore + 100

            if isPatternTwo == True:
                if 50 > totalDiceScore:
                  print ("Value of all 5 dice add up to a prime number, therefore you get 50 points.") 
                  playerScore = playerScore + 50

            if isPatternThree == True:
                if 30 > totalDiceScore:
                  print ("Value of 3 of 5 dice are the same, therefore you get 30 points.")
                  playerScore = playerScore + 30

            if isPatternFour == True:
                if 25 > totalDiceScore:
                  print ("Value of all 5 dice are the same, therefore you get 25 points.")
                  playerScore = playerScore + 25


            if isPatternOne == False and isPatternTwo == False and isPatternThree == False and isPatternFour == False:
                playerScore = playerScore + totalDiceScore

        if reroll == True:
            print("You rerolled some dice values are ", diceOne, diceTwo, diceThree, diceFour, diceFive, "\n")

            # check for patterns again
            if isPatternOne == True:
                if 100 > totalDiceScore:
                    print("Would you like to score the pattern points for all 5 dice having the same value? (100 points) [yes/no]")
                    userInput = getUserInput()

                    if userInput == True:
                        playerScore = playerScore + 100
                        break

            if isPatternTwo == True:
                if 50 > totalDiceScore:
                    print("Would you like to score the pattern points for all 5 dice add up to prime number? (50 points) [yes/no]")
                    userInput = getUserInput()

                    if userInput == True:
                        playerScore = playerScore + 50
                        break

            if isPatternThree == True:
                if 30 > totalDiceScore:
                    print("Would you like to score the pattern points for 3 of the 5 dice have same value? (30 points) [y/n]")
                    userInput = getUserInput()

                    if userInput == True:
                        playerScore = playerScore + 30
                        break
                    
            if isPatternFour == True:
                if 25 > totalDiceScore:
                    print("Would you like to score the pattern points for all 5 dice have different value? (25 points) [y/n]")
                    userInput = getUserInput()

                    if userInput == True:
                        playerScore = playerScore + 25
                        break

            print("Would you like to score the sum of the dices? (", totalDiceScore ," points) [y/n]" )
            userInput = getUserInput()

            if userInput == True:
                playerScore = playerScore + totalDiceScore
                gameCounter = gameCounter + 1
                break

        else:
            print("You didn't reroll any of the dice, please try again")
            reroll = False
            rerollCount = rerollCount + 1

    gameCounter = gameCounter + 1


print("Player Score after 10 turns are: ", playerScore)

if playerScore > 400:
    print("Good Score!")
elif playerScore > 200 and playerScore < 400:
    print("Average Score!")
else:
    print("Below average score, please try again!")
