import random

print("""
Welcome to the Coin Guessing Game!
Choose the method to toss the coin:
1. Using random.randint()
2. Using random.random()
""")

choice = input("Enter your choice (1 or 2): ").strip()

if choice == "1":
    rand_num = random.randint(0, 1)
    if rand_num == 0:
        computer_result = "heads"
    else:
        computer_result = "tails"
elif choice == "2":
    if random.random() >= 0.5:
        computer_result = "heads"
    else:
        computer_result = "tails"
else:
    print("Error! Invalid choice.")
    exit()

user_guess = input("Enter your guess (heads or tails): ").lower().strip()

if user_guess == computer_result:
    print("You win!")
else:
    print("You lose!")

print(f"The computer chose: {computer_result}")
