content = ''

#Ask for number of lines
numberOfLines = int(input("Enter number of lines to read: "))
#Take user input
for i in range(0, numberOfLines):
    inp = str(input("Enter line - "+str(i+1)+": "))
    content += inp + " "
print("Content provided by you: ", content)

#Initialise counters and flags
if content[0] == ' ':
    hasSpaceStarted = True
else:
    hasSpaceStarted = False
wordCount = 0
totalCount = 0
totalAlnum = 0

for c in content:
    totalCount+=1
    if c.isalnum():
        totalAlnum+=1
    if c.isalpha():
        if(hasSpaceStarted == True):
            hasSpaceStarted = False
    elif hasSpaceStarted == False and c.isspace():
        hasSpaceStarted = True
        wordCount += 1

print ("Total words:", wordCount)
print ("Total Characters: ", totalCount)
print ("Total Alpha Numbers: ", totalAlnum)
print ("Percentage AlphaNums: ", totalAlnum/totalCount*100)