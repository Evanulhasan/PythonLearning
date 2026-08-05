# Execercise 4 Solution


st = input("Enter a string: ")
words = st.split(" ")

# If coding is true, Than go to the if block and add "dfs" at the 
# start and "uyr" at the end of the word. Also, move the first 
# character of the word to the end of the word.

# If coding is false, Than go to the else block and remove the 
# first 3 and last 3 characters from the word.
coding = False
if(coding):
    newword = []
    for word in words:        
        if(len(word) >= 3):
            r1 = "dfs"
            r2 = "uyr"
            stnew = r1 + word[1:] + word[0] + r2
            newword.append(stnew)
        else:
            newword.append(word[::-1])
    print(" ".join(newword))


else:
    newword = []
    for word in words:        
        if(len(word) >= 3):
            stnew =  word[3:-3] 
            stnew = stnew[-1] + stnew[:-1]
            newword.append(stnew)
        else:
            newword.append(word[::-1])
    print(" ".join(newword))


