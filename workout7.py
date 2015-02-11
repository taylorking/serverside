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


def problem_1():
    import sys
    if(len(sys.argv) < 2):
        print("Invalid arguments")
        return
    for i in sys.argv[1:]:
        print("Filename: " + i) 
        f = open(i) 
        for data in f:
            print(str.rstrip(data))
        print("\n")

def problem_2():
    if(len(sys.argv) < 2): 
        print("Invalid arguments") 
        return
    for i in sys.argv[1:]: 
        print(i)
        f = open(i)
        nums = []
        for data in f: 
            if not '**' in data: 
                nums.append(int(data))
        print("File name: " + i)
        import my_stats
        print("Sum: " + str(my_stats.sum(*nums)))
        print("Mean: " + str(my_stats.mean(*nums)))
        print("Median: " + str(my_stats.median(*nums)))
        print("Standard Deviation: " + str(my_stats.standard_deviation(*nums)))
        print("\n")

def problem_3():
    if(len(sys.argv) < 2):
        print("Invalid arguments")
        return
    header = "\t1\t\t2\t\t3\t\t4\t\t5\n"
    for i in range(1,6):
        header+="-----------\t"
    for i in sys.argv[1:]:
        print("File name: " + i)
        print(header)
        f = open(i)
        count = 0 
        for data in f:
            line=str(count) + " | "
            splat = data.split(",") 
            for j in range(0, len(splat)): 
                line += "%06d " % int(splat[j]) + ( "\t" if j==0 else "\t\t")
            print(str.rstrip(line))
            count+=1
import sys
print(sys.argv[0])       
print("What do you want to do: ")
print("1. use arguments as a way to read files") 
print("2. run my_stats on a list of files passed")
print("3. run on csv's")
choice = int(input("> "))
if choice == 1:
    problem_1()
elif choice == 2:
    problem_2()
elif choice == 3: 
    problem_3()
