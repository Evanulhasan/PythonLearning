# Exercise 3 : Kaun Banega CrorePati(KBC)

# We use list data type to store the   question and their correct and  Answers. 
# Display the final ammount the person it taking home after playing the game


# List of questions: [Question, A, B, C, D, Correct_Option, Prize]
questions = [
    ["What is the capital of India?", "A. Mumbai", "B. Delhi", "C. Pune", "D. Chennai", "B", 1000],
    ["Which planet is known as the Red Planet?", "A. Earth", "B. Venus", "C. Mars", "D. Jupiter", "C", 2000],
    ["Which is the largest animal on Earth?", "A. Elephant", "B. Blue Whale", "C. Giraffe", "D. African Rhino", "B",4000],
    ["Which festival is known as the 'Festival of Lights'?", "A. Holi", "B. Eid", "C. Diwali", "D. Christmas", "C", 8000]
]

total_winnings = 0

for q in questions:
    print(f"\n{q[0]}")
    print(f"{q[1]}  {q[2]}")
    print(f"{q[3]}  {q[4]}")
    
    ans = input("Enter your answer (A/B/C/D): ").upper()
    
    if ans == q[5]:
        total_winnings +=  q[6]
        print(f"Correct! You have won ₹{total_winnings}")
    else:
        print("Wrong answer!")
        break


print(f"\nFinal amount you are taking home: ₹{total_winnings}")





































































