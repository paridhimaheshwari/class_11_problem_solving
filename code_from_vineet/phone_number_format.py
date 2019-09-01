phoneNumber = str(input("Enter phone number: "))
print("Phone number you entered is: ", phoneNumber)

numDigits = 0
for i in range(0,len(phoneNumber)):
    if(i == 3 or i == 7):
        if(phoneNumber[i] == '-'):
            continue
        else:
            print("You have not entered - at right place. Location: ", i)
            break
    if(phoneNumber[i].isdigit()):
        numDigits +=1
        continue
    else:
        print("You have entered wrong number. Location: ", i)
        break
else:
   if(numDigits == 10):
        print("Your phone is valid")
   else:
       print("Your phone is not 10 digits")
