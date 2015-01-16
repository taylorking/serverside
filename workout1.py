# // Does integer division and throws away the remaining decimal
# / Does traditional float division
# % is the mod operator like java
# ** is the equivalent to Math.pow in java
#
#
#
def miles_to_kilometers():
    miles = input("Miles?")
    return miles / .62137

def fibonacci_param(n):
    i = 0
    while(i<n):
        print(fibonacci_seq(i))
        i+=1

def fibonacci():
    n = int(input("n?"))
    i = 0
    while(i < n):
        print(fibonacci_seq(i))
        i+=1    

def fibonacci_seq(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_seq(n-1) + fibonacci_seq(n-2)

def smallest(n):    
    smallest = -1 
    for v in n:
        if smallest == -1:
            smallest = v
        elif v < smallest:
            smallest = v
    return smallest

def contains_vowel(n):
    n = n.lower()
    for j in n:
        if j == 'a' or j=='e' or j=='i' or j =='o' or j =='u' or j=='y':
            return True
    return False
def calories():
    weight = int(input("Weight in Lbs: "))
    miles = int(input("Miles ran: "))
    return (.75 * weight) * miles

print("1. Convert Miles to Kilometers")
print("2. Fibonacci sequence")
print("3. Fibonnaci number as a parameter")
print("4. Nth Fibonacci number")
print("5. Smallest value")
print("6. Calories burned while running")
print("7. Vowel String")
toDo = input("?")
if toDo == "1":
    print (miles_to_kilometers())
elif toDo == "2":
   fibonacci()
elif toDo == "3":
    n = input("n?")
    fibonacci_param(int(n))
elif toDo == "4":
    n = int(input("n?"))
    print(fibonacci_seq(n))
elif toDo == "5":
    n = [3, 5, 2, 1]
    print(smallest(n))
elif toDo == "6":
    print(calories())
elif toDo == "7":
    print(contains_vowel("Hello Dr. Russell"))
