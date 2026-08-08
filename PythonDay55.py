# Example 5 : Snake, Water and Gun 

import random 

choices = ["snake", "water", "gun"]

user_choice = input("Enter snake, water, or gun: ").lower()

computer_choice=random.choice(choices)

print(f"\nYour Chose: {user_choice}")
print(f"Computer Chose: {computer_choice}\n")

if user_choice == computer_choice:
    print("It's a tie!")

elif user_choice == "snake":
    if computer_choice == "water":
        print("Snake drinks water! You Win!")
    else:
        print("Gun Shoots snake! You lose.")


elif user_choice == "water":
    if computer_choice == "gun":
        print("Gun sinks in water! You Win!")
    else:
        print("Snake drinks water! You lose.")


elif user_choice == "gun":
    if computer_choice == "snake":
        print("Gun shoots snake! You Win!")
    else:
        print("Gun sinks in water! You lose.")


else:
    print("Invalid choice! Pleae type snake, water of guns")















































