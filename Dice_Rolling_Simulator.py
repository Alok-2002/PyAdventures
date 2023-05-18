import random
import time

def roll():

    dice = ["1","2","3","4","5","6"]
    roll_dice = random.choice(dice)
    # print(roll_dice)
    time.sleep(0.5)
    if roll_dice == "1":
        print("[-------]")
        print("[---0---]")
        print("[-------]")
        
    elif roll_dice == "2":
        print("[0------]")
        print("[-------]")
        print("[------0]")
    
    elif roll_dice == "3":
        print("[0------]")
        print("[---0---]")
        print("[------0]")
    
    elif roll_dice == "4":
        print("[0-----0]")
        print("[-------]")
        print("[0-----0]")
    
    elif roll_dice == "5":
        print("[0-----0]")
        print("[---0---]")
        print("[0-----0]")
    
    elif roll_dice == "6":
        print("[0-----0]")
        print("[0-----0]")
        print("[0-----0]")
    
    else:
        
        print("Invalid Input")

def dice_game():
    flag = True
    while flag:
        print(" ")
        print("----------Welcome To The Dice Rolling Game-------------")
        print(" ")
        print(" ")
        print("-----Want To Roll The Dice: ")
        user_input = input('''Enter Y To Roll The Dice
Enter E To Exit ''').lower()
        if user_input == 'y':
            roll()
        else:
            print("Exiting.........")
            break
            
dice_game()