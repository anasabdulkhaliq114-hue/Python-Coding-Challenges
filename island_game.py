print("=== Welcome to the Mystery Island Game ===")
print("Your mission is to find the hidden treasure.\n")

x = input("You are standing in front of two doors: Red and Blue.\nWhich door do you choose? (red/blue): ").lower().strip()

if x == "red":
    print("\nGreat! You opened the red door and entered a secret room.")
    x1 = input("Inside the room, you see three boxes: Red, Green, and Black.\nWhich box do you open? (red/green/black): ").lower().strip()

    if x1 == "red":
        print("\nCongratulations! You found the treasure. You WIN!")
    elif x1 == "green":
        print("\nOh no! A snake was inside the box. Game Over!")
    elif x1 == "black":
        print("\nOh no! You fell into a trap. Game Over!")
    else:
        print(f"\nInvalid choice! '{x1}' is not one of the boxes.")

elif x == "blue":
    print("\nYou opened the blue door and fell into a deep river. Game Over!")

else:
    print(f"\nInvalid choice! '{x}' is not a valid door.")
