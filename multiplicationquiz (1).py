
#Multiplication Quiz

#init
import random

#function

def quiz():
    print("Welcome to the Multiplication Quiz!")
    level = str(input("Want to play easy mode or hard mode?"))
    if level == "easy":
        score = 0
        for i in range(5):
            num1 = random.randint(0,5)
            num2 = random.randint(0,5)
            playerans = input("What is " +str(num1) +" x " +str(num2) +"?" )
            print("Your answer is " +str(playerans))
            ans = num1*num2
            if str(ans) == str(playerans):
                print("You are correct")
                score = score +1
                print("Your score is now " +str(score))
            else:
                print("You are wrong")
                print("The correct answer is " +str(ans))
                score = score + 0
                print("Your score is now " +str(score))
    if level == "hard":
        score = 0
        for i in range(5):
            num1 = random.randint(5,10)
            num2 = random.randint(5,10)
            playerans = input("What is " +str(num1) +" x " +str(num2) +"?" )
            print("Your answer is " +str(playerans))
            ans = num1*num2
            if str(ans) == str(playerans):
                print("You are correct")
                score = score +1
                print("Your score is now " +str(score))
            else:
                print("You are wrong")
                print("The correct answer is " +str(ans))
                score = score + 0
                print("Your score is now " +str(score))

#main

quiz()
