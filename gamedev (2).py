

#init
import random
#function
guess = int(input("Enter Guess")) #integer
secret = random.randint(0,10) #integer

def game():
        if guess == secret:
            print("You have guessed correctly")
        else:
            ans = input("Wrong, want to try again?")
            if ans == "no":
                print("Thank you for playing")
            elif ans == "yes":
                if guess == secret:
                    print("You have guessed correctly")
                else:
                    ans = input("Wrong, want to try again?")
                    if ans == "no":
                        print("Thank you for playing")
                    elif ans == "yes":
                        if guess == secret:
                            print("You have guessed correctly")
                        else:
                            print("Game over")












#main
game()
