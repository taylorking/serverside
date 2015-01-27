#!/usr/bin/env python3.4

def read_backwards(path):
    f = open(path) 
    objects = []
    for data in f:
        objects.append(data)
    for i in range(0,len(objects)):
        print(objects.pop())

def print_or_input(path):
    f = open(path) 
    for data in f:
        if "print" in data or "input" in data:
            print(data)

def numbered_output(path): 
    f = open(path)
    count = 1 
    output = open(path + ".numbered", "w") 
    for data in f:
        data = str.rstrip(("%04d " % count) + data)
        count+=1
        print(data)
        output.write(data + "\n")
    print(path + ".numbered written in current directory")
def strip_numbers(path): 
    f = open(path) 
    for data in f:
        print(str.rstrip(data[5:]))

def text_codes(path):
    f = open(path) 
    text_codes = {"LOL":"Laugh out loud", "ROFL":"Rolling on the floor laughing", "BRB":"Be right back", "TBH": "To Be honest."} # You get the picture here.. I don't wanna waste too much time putting in a bunch of obscure text message acronyms
    for data in f: 
        for key in list(text_codes.keys()):
            data = data.replace(key, text_codes[key])
        print(str.rstrip(data))

print("Choose a function: ")
print("1. Read Backwards ")
print("2. Print or Input ")
print("3. Numbered output ")
print("4. Strip Numbered ")
print("5. Text Codes")
choice = int(input(">"))
if choice == 1:
    read_backwards(input("filename > "))
elif choice == 2: 
   print_or_input(input("filename > "))  
elif choice == 3:
    numbered_output(input("filename > "))
elif choice == 4:
    strip_numbers(input("filename > "))
elif choice == 5:
    text_codes(input("filename > ")) 

