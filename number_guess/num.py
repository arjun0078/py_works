import random
icon=''' _____ _     _____ ____  ____    _____  _     _____   _      _     _      ____  _____ ____ 
/  __// \ /\/  __// ___\/ ___\  /__ __\/ \ /|/  __/  / \  /|/ \ /\/ \__/|/  _ \/  __//  __\
| |  _| | |||  \  |    \|    \    / \  | |_|||  \    | |\ ||| | ||| |\/||| | //|  \  |  \/|
| |_//| \_/||  /_ \___ |\___ |    | |  | | |||  /_   | | \||| \_/|| |  ||| |_\\|  /_ |    /
\____\\____/\____\\____/\____/    \_/  \_/ \|\____\  \_/  \|\____/\_/  \|\____/\____\\_/\_\
                                                                                           '''
print(icon)

global guess

def guess1():#this is used to guess the number............
    guess=int(input("guess again! "))
    return guess

def easy():
    num=random.randint(1,100)
    count=10
    print("you have 10 attempts remaining ")
    guess=int(input("make a guess: "))
    for i in range(1,10):
        if guess==num:
            print("you won!!")
            break
        elif guess>num:
            count=count-1
            print("too high")
            print(f"you have only {count} attempts left")
            guess=guess1()
        elif guess<num:
            count=count-1
            print("too low")
            print(f"you have only {count} attempts left")
            guess=guess1()

def hard():# this is hard mode .............
    num=random.randint(1,100)
    count=5
    print("you have only five attempts remaining\n")
    guess=int(input("make a guess:"))
    for i in range(1,5):       
        if guess==num:
            print("you won!!")
            break
        elif guess>num:
            count=count-1
            print("too high")
            print(f"you have only {count} attempts left")
            guess=guess1()
        elif guess<num:
            count=count-1
            print("too low")
            print(f"you have only {count} attempts left")
            guess=guess1()
print("welcome to the number guessing game\n")
print("im guessing a number between 1 and 100,give the right answer an you win!\n")
choice=input("choose the difficulty level : ")
if choice=="hard":
    hard()
elif choice=="easy":
    easy()
else:
    raise Exception("incorrect mode!!")   