import itertools 


stack = []
def dog_breed():
    x = []
    print("Type Quit to exit")
    user = "" 
    while user != quit :
        x.append(user)

def my_push(data): 
    stack.append(data)
def my_pop():
    return stack.pop()

def my_top(): 
    return stack[len(stack) - 1]


def stack_demo():
    my_push("test")
    my_push("test2")
    print(my_top())
    print(my_pop())
    print(my_pop())

def permute_num(num): 
    if num == 0 or num == 1:
        return ['0']
    elif num == 2:
        return ['A','B','C']
    elif num == 3:
        return ['D','E','F']
    elif num == 4:
        return ['G','H','I']
    elif num == 5: 
        return ['J','K','L']
    elif num == 6: 
        return ['M','N','O']
    elif num == 7:
        return ['P','R','S']
    elif num == 8:
        return ['T','U','V']
    elif num == 9:
        return ['W','X','Y']

def prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True    

def median(vals):
    vals.sort()
    median = len(vals) // 2
    return vals[median] 

def friends_list_reverse():
    friends = []
    print("Enter Names. Type quit to exit")
    data = ""
    while data != 'quit':
        data = input('>')
        if data!= 'quit':
            friends.append(data)
    friends.reverse()
    return friends

def friends_set_reverse():
    x =  set(friends_list_reverse())
    return x

def is_friend(name, data):
    for curr in data:
        if curr == name:
            return True
    return False

def phone_word(word):
    possibilities = [] 
    for c in range(1,4):
        possibilities += permute_num(int(word[c]))
    for r in itertools.permutations(possibilities, 4):
        print(r)
print("1. Dog Breeds ")
print("2. Prime ")
print("3. Middle" )
print("4. friends list reverse")
print("5. Stack Demo")
print("6. Friend set")
print("7. Is Friend")
print("8. Phone Word")
choice = int(input(">"))
if choice == 1:
    dog_breed()
elif choice == 2: 
    print(prime(int(input("n?:"))))
elif choice == 3: 
    print(median(list([1,9,3,1,6,3,5])))
elif choice == 4:
    print(friends_list_reverse())
elif choice == 5: 
    stack_demo()
elif choice == 6:
    print(friends_set_reverse())
elif choice == 7:
    name = input("enter the name you want: ")
    print(is_friend(name, friends_set_reverse()))
elif choice == 8:
    phone_word(input("enter 4 digits > "))
