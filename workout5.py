#!/usr/bin/env python3.4
def person_info(*args):
    if len(args) < 1: 
        print("You at least need to give me a last name")
        return
    # This kind of implies that the last argument is left off
    # It would be impossible for me to do that without a dictionary
    for i in range(0, len(args)):
        if i == 0:
            print("Last Name: " + args[i])
        elif i == 1:
            print("First Name: " + args[i]) 
        elif i == 2: 
            print("Phone Number: " + args[i]) 
        elif i == 3:
            print("Street address: " + args[i]) 
        elif i == 4: 
            print("City: " + args[i])
        elif i == 5: 
            print("State: " + args[i]) 
        elif i == 6: 
            print("Zip: " + args[i]) 
def even(n):
    my_ran = range(0, n) 
    it_me = my_ran.__iter__()
    for i in it_me:
        if i % 2 == 0:
            print(i)

print("Pick a function: ")
print("1. Run person_info")
print("2. Celcius to farenheit") 
print("3. Do the iterator thing")
print("4. Run decorator") 
choice = int(input("> ")) 
if choice == 1:
    print("Enter arguments to pass to person_info") 
    print("Enter quit when you are done entering parameters") 
    query = ""
    args = [] 
    while query != "quit":
        query = input("> ")
        if query != "quit":
            args.append(query)
    person_info(*args)
elif choice == 2:
    g = lambda c: c * 1.8000
    print(g(int(input("celcius > "))))
elif choice == 3: 
    even(int(input("n > ")))
elif choice == 4:
    import decorator    
