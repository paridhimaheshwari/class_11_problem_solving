numberedString = str(input("Enter the string with numbers: "))
print("String you entered: ", numberedString)
total = 0
digits = ''
for c in numberedString:
    if c.isdigit() :
        total += int(c)
        digits = digits + c

if(digits == ''):
    print("There are no digits")
else:
    print("Total of digits:", digits, " is ", total)