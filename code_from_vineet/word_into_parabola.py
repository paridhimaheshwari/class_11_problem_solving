#Take the input
print ("Type two words. I will compare the two. Write the larger one in V Shape")
word1 = input("Give me first word: ")
word2 = input("Give me second word: ")

print ("You gave me words: ", word1, word2)

#Find the larger number
v_word = word2
if(len(word1) > len(word2)):
    v_word = word1
print("Larger word is: ", v_word)

#Find number of rows that will be required
numRows = len(v_word)//2
if(len(v_word) % 2):
    numRows +=1
print("Number of rows: ", numRows)

for i in range(0,numRows):
    for j in range(0, len(v_word)):
        if(j == i or (i+j) == (len(v_word)-1)):
            print(v_word[j], end=' ')
        else:
            print(" ", end=" ")
    print()