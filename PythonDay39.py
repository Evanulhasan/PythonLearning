# Kaun Banga Corepati : xercise 2 

# question = [
#     ["1. The enzyme pepsin convert?","(A) Carbohydrates to sugars) ","(B) Proteins to amino acids","(C) Protein to peptones","(D) Fats to !atty acids and", "A",1000],
#     ["2. The language of Lakshadweep","(A)Tamil","(B) Proteins to amino acids","(C) Malayalam","(D) Fats to !atty acids and", "C",2000],
#     ["1. The enzyme pepsin convert?","(A) Carbohydrates to sugars) ","(B) Proteins to amino acids","(C) Protein to peptones","(D) Fats to !atty acids and", "D",4000],

# ]

# for i in question:
#     print(i[0])
#     print(f"{i[1]} {i[1]}")
#     print(f"{i[3]} {i[4]}")
    
#     ans = input("Enter the and A/B/C/D: ").upper()
#     if ans == i[5]:
#         print(f"Correct! You have won ₹{i[6]}")
#     else:
#         print("Your ans is Wrong!")
#         break





# KBC Game 
question = [
    ["1. The enzyme pepsin convert?","(A) Carbohydrates to sugars) ","(B) Proteins to amino acids","(C) Protein to peptones","(D) Fats to !atty acids and", "A"],
    ["2. The language of Lakshadweep","(A) Tamil","(B) Proteins to amino acids","(C) Malayalam","(D) Fats to !atty acids", "C"],
    ["3. The enzyme pepsin convert?","(A) Carbohydrates to sugars) ","(B) Proteins to amino acids","(C) Protein to peptones","(D) Fats to !atty acids and", "D"],
    ["4. The enzyme pepsin convert?","(A) Carbohydrates to sugars) ","(B) Proteins to amino acids","(C) Protein to peptones","(D) Fats to !atty acids and", "A"],
    ["5. The language of Lakshadweep","(A)Tamil","(B) Proteins to amino acids","(C) Malayalam","(D) Fats to !atty acids and", "C"],
    ["6. The enzyme pepsin convert?","(A) Carbohydrates to sugars) ","(B) Proteins to amino acids","(C) Protein to peptones","(D) Fats to !atty acids and", "D"],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000]
money = 0

for i in range(len(question)):
    q = question[i]
    print(f"Question for tk {levels[i]}")
    print(q[0])
    print(f"{q[1]}    {q[2]}")
    print(f"{q[3]}    {q[4]}")

    ans = input("Enter the answer A/B/C/D: ").upper()
    if ans == q[5]:
        print(f"Correct! You have won {levels[i]}")
        money += levels[i]
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 1000000
    else:
        print("Wrong Answer!")
        break

print(f"Game over. You won tk : {money}")  
        
        