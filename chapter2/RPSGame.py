import random
import sys

# while True:
#     userInput = input()
#     if userInput == 'q':
#         print("q")

def RPSGame():
    while True:
        userInput = input()
        if userInput == 'q':
            sys.exit()
        if userInput != 'r' and userInput != 'p' and userInput != 's':
            print("input error")
            continue
        randomInt = random.randint(1, 3)
        match randomInt:
            case 1:
                print(userInput + " vs r")
                match userInput:
                    case 'r':
                        print("Tie")
                    case 'p':
                        print("Lose")
                    case 's':
                        print("Win")
            case 2:
                print(userInput + " vs p")
                match userInput:
                    case 'r':
                        print("Win")
                    case 'p':
                        print("Tie")
                    case 's':
                        print("Lose")
            case 3:
                print(userInput + " vs s")
                match userInput:
                    case 'r':
                        print("Lose")
                    case 'p':
                        print("Win")
                    case 's':
                        print("Tie")
            case _:
                print("error")
        
        
        


if __name__ == "__main__":
    RPSGame()