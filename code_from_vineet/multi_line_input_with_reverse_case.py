print("Please type lines or type q on new line to exit. I will give you all characters reverse cased.")

content = ''
while True:
    s = input("Continue typing..: ")
    if(s in "qQ"):
        break
    content += s

reverseCaseContent = ''
for c in content:
    if(c.isalpha()):
        if c.isupper():
            reverseCaseContent += c.lower()
        else:
            reverseCaseContent += c.upper()
    else:
        reverseCaseContent += c
print("Content: reverse cased: ", reverseCaseContent)