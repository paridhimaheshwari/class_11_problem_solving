# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%
#a=int(input("enter a number"))
#b=int(input("enter another number"))
#print(a+b)

#%%
a2=2
u=50
print(a2*u)

#%%
for i in range(1, 10):
    time.sleep(1)
    print("\a")
    
    
#%%
sum=0
product=1
n=int(input("enter a number"))
for i in range(1,n+1):
    sum+=i
    product*=i
print("sum of n numbers",sum)
print("product of n numbers", product)

#%%
print("math is so fun dont be resistant \njust learn the rules, the rules are consistent \nand most important you must be persistent \n\nadding fraction get common denominators")


#%%
print("happy \rday")
print("happy \nday")
print("happy    day")

#%%
for i in range(1,100):
    time.sleep(2)
    if(i%4 == 0):
        print("\r|")
    elif(i%4 == 1):
        print("\r/")
    elif(i%4 == 2):
        print("\r-")
    else:
        print("\r\\")
        
#%%
n=int(input("enter a number"))       

#%%
x=40
y=x+1
x=20,y+x
print(x,y)


#%%
p,q=3,5
q,r=p-2,p+2
print(p,q,r)

#%%
x,x=20,30
y,y=x+10,x+20
print(x,y)

#%%
x=12.345
type(x)


#%%
na=input("enter your name")
y=input("enter age")

#%%
age=int(input("enter age"))

#%%
#%%
age=int(input("enter your age"))
gender=input("enter ur gender(M/F)")
marital_status=input("enter your status(Y/N)")
if gender=="M" and 20<=age<=40:
    print("you may work anywhere")
if gender=="F" and 20<=age<=60:
    print("you may only in urban areas")
if gender=="M" and 40<=age<=60:
    print("work only in urban areas")
if 0<=age<=20:
    print("ERROR")
    
#%%
sum=0
x=int(input("Enter first number-"))
y=int(input("Enter second number-"))
z=int(input("Enter third number"))
if x!=y and y!=z and x!=z:
    sum+=x+y+z
print(sum)

#%%
x=str(input("Enter a character:"))
if((x>='a' and x<='z') or (x>='A' and x<='Z')):
    print("this is an alphabet")
else:
    print("this is not an alphabet")
if((x=='a' or x=='A' or x=='e' or x=='E' or x=='I' or x=='i' or x=='o' or x=='O' or x=='u' or x=='U')):
    print(x,"is a vowel")
else:
    print(x,"is not a vowel")
    
#%%
x=int(input("Enter first,"))
y=int(input("Enter second,"))
z=int(input("Enter third,"))
if x>y and x>z:
    print(x, "is the greatest number")
if y>x and y>z:
    print(y, "is the greatest number")
if z>x and z>y:
    print(z, "is the greatest number")
if x<y and x<z:
    print(x, "is the smallest number")
if y<x and y<z:
    print(y, "is the smallest number")
if z<x and z<y:
    print(z, "is the smallest number")
    
#%%
x=int(input("Enter first,"))
y=int(input("Enter second,"))
z=int(input("Enter third,"))
if x>y and y>z:
    print(x,">",y,">",z)
if x>z and z>y:
    print(x,">",z,">",y)
if y>z and z>x:
    print(y,">",z,">",x)
if y>x and x>z:
    print(y,">",x,">",z)
if z>y and y>x:
    print(z,">",y,">",x)
if z>x and x>y:
    print(z,">",x,">",y)
    
#%%
num=int(input("Enter a number"))
for i in range(2,num):
    if (num%i)==0:
        print("the number is not a prime number")
        break
else:
   print("the number is a prime number")
   
#%%
n=int(input("Enter a number"))
o=len(str(n))
print(o)

#%%
n=int(input("Enter a number"))
a=n
sum=0
o=n%10
t=(n%100)//10
h=n//100
sum=o**3+t**2+h**1
if sum==a:
    print(a,"is diarium")
else:
    print(a, "is not disarium")
    
#%%
n=int(input("Enter a number"))
a=n
s=n
count=0
while n>0:
    count+=1
    n=n//10
    
sum=0
while a>n:
    o=a%10
    p=o**(count)
    sum+=p
    count-=1
    a//=10

if sum==s:
    print(s,"is diarium")
else:
    print(s, "is not disarium")

#%%
n=int(input("Enter a number"))
print("the prime factor/s are")
for i in range(2,n+1):
    if n%i==0:
        for j in range(2,i):
           if (i%j)==0:
             break
        else:
            print(i)

#%%
n=int(input("Number of rows"))            
for row in range(1,n+1):
    for col in range(1,row+1):
        print(row+1-col, end="")
    print()
    
#%%
n=int(input("Number of rows"))   
for row in range(1,n+1):
    if (row==1) or (row==n):
        print(n*"#")
    else:
        print("#", (n-4)*" ", "#")
              
#%%
n=int(input("Enter a no:"))
for i in range(n+1,1,-1):
    for j in range(0,i):
        print(j,end="")
    print()
    
#%%
n=int(input("Number of rows"))
for row in range(1,n+1):
    for col in range(row,n+1):
        print(col, end=" ")
        
    for col in range(row-1,0,-1):
            print(col, end=" ")
    print()   
        
        
#%%
n=int(input("enter number of terms:"))
prev=0
current=1
print(prev, end=" ")
if(n > 1):
    print(current, end=" ")
if(n > 2):
    for row in range(2,n):
        temp = prev
        prev = current
        current += temp
        print(current, end=" ")
        
#%%number's reverse

sum=0
count=0
n=int(input("Enter a number"))
s=n
m=n
while n>0:
    d=n%10
    n//=10
    sum+=d
    count+=1
print(sum,count)
rev=0

for i in range(count-1, -1,-1):
    d=s%10
    rev+=d * (10**i)
    s//=10
    
print(rev)

#%%
number=0
for number in range(10):
    number+=1
    
    if number==5:
      break
print('number is', number)

for i in range(10):
    if i==2:
        continue
    print(i)
print("bye")
print(i)

#%%
for i in range (5,0,-1):
    for j in range(i,0,-1):
        print("#", end='')
    print()
    
    #%%
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end='')
    print()
    #%%
for i in range(1,6):
    for j in range(1,i+1):
        print(i, end='')
    print()
    
    #%%
n=int(input("enter a number"))
a=str(n)
print("the number of digits are", len(a))

#%%      ?
x=int(input("enter a number"))
n=int(input("enter a number"))
sum=0
factorial=1
for i in range(1,n+1):
    factorial*=i
    print("Factorial now: ",factorial)
    print("Term:", x**i / factorial)
    sum+=x**i/factorial
    print("Sum:", sum)
    print()

print()
print()
print("Finally: ", sum)

#%%

num = int(input("Enter an odd number: "))
midPoint = num//2 +1
for row in range(1,midPoint+1):
    for col in range(1, midPoint - (row-1)):
        print(" ", end="")
    for col in range(1,  row+1):
        print("*", end=" ")
    print()

for row in range(midPoint+1,num+1):
    for col in range(1, row - midPoint + 1):
        print(" ", end="")
    for col in range(1, num+1 - row + 1):
        print("*", end=" ")
    print()
    
#%%
n=str(input("enter"))
m=''
v=0
c=0
d=0
sC=0
a=0
allc=0
for i in range(-1,-len(n)-1,-1):
    m+=n[i]
    allc+=1
    if "aieouAIEOU".find(n[i]) >= 0:
        v+=1
        
    elif "qwrtypsdfghjklmnbvcxzQWRTYPSDFGHJKLZMNXBCV".find(n[i]) >= 0:
        c+=1
    elif n[i].isdigit():
        d+=1
    else:
        sC+=1
print("char",allc,"the number of consonents are", c, "the number of digit are",d, "the number of vowels are", v, "the number of sC are",sC, "alphabets",a)
print(m, end='')
if m==n:
    print("   its a palendrome")
else:
    print("   its not")
    
#%%
n=str(input("Enter a sentence"))   
char=len(n) 
alphnum=0
words=1
for i in range(0, len(n)):
    if n[i].isalnum():
        alphnum+=1
    if n[i].isspace():
        words+=1
print("the alpha charcter are", alphnum, "the number of words are", words)        
per=(alphnum/char)*100
print("percentage is", per)




#%%
phoneNumber=input("Enter a number")
digit=0
for i in phoneNumber:
    if i.isdigit():
       digit+=1
#print(digit)
if len(phoneNumber)>12:
    print("not valid")
elif digit==10 and phoneNumber[3]=='-' and phoneNumber[7]=='-':
    print("Its a valid number")
else:
    print("Its not valid")
    
    
#%%
rubbish=input("enter rubbish word")  
digit=''
sum=0
for i in rubbish:
    if i.isdigit():
        digit+=i
        sum+=int(i)
if digit=='':
    print("there's no number")
else:
    print("the number of digits are", digit, "the sum of the digits is", sum)

#%%
sentence=input("Enter a string")
words=1
alphanum=0
for i in sentence:
    if i.isspace():
        words+=1
print("the number of words are", words)
a=len(sentence)
print("The number of character are",a)
for i in sentence:
    if i.isalnum():
        alphanum+=1
print("the alphanumeric part is", (alphanum/a)*100)

#%%
print("please enter a sentence or 'q' to quit")
n=input("Enter a string")
og=''
if n=='q':
    print("Sorry to disturb you busy PERSON")
else:
    for i in n:
        if i.isupper():
            og+=i.lower()
        if i.islower():
            og+=i.upper()
        else:
            og+=i
    print(og)
    
#%%
num=int(input("Enter a number"))
word=str(input("Enter a string"))
digit=''
for i in word:
    if i.isdigit():
        digit+=i
if digit == '':
    digit=0
print(digit)
print("the integer_input + string_digits= sum", num+int(digit))
    

#%%






        
    

    

