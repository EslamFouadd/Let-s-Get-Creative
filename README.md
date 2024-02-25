# Let-s-Get-Creative

import time

def introduction():
    print("Welcome to the Adventure Game!")
    print("You find yourself standing at the entrance of a dark cave.")
    print("Do you want to enter the cave? (yes/no)")
    choice = input().lower()
    if choice == "yes":
        cave()
    elif choice == "no":
        print("You decide not to enter the cave. The end.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        introduction()

def cave():
    print("\nYou enter the cave and walk deeper into its depths.")
    print("After some time, you come to a fork in the path.")
    print("Do you want to go left or right? (left/right)")
    choice = input().lower()
    if choice == "left":
        print("\nYou chose to go left. You encounter a sleeping dragon!")
        time.sleep(1)
        print("The dragon wakes up and breathes fire at you. Game over!")
    elif choice == "right":
        print("\nYou chose to go right. You find a treasure chest!")
        time.sleep(1)
        print("You open the chest and find it filled with gold coins. Congratulations, you win!")
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")
        cave()

# Start the game
introduction()
