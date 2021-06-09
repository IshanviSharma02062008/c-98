f=open("C:/Users/my pc/OneDrive/Documents/python/C-98/test.txt")
fileLines=f.readlines()
for line in fileLines:
    print(line)

introString= "My name is Ishanvi. I am 13 yrs old" 
words= introString.split(",")   
print(words)

def greet(name):
    print("Hello, "+ name + ".How are you?")

greet("Ishanvi")
    