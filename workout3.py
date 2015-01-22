import random

# Rock Paper Scissors 

def num_to_string(num):
    if num == 1:
        return "rock"
    elif num == 2:
        return "paper"
    elif num == 3: 
        return "scissors"

def roshambo():
    human_score = 0
    computer_score = 0
    while(human_score < 11 and computer_score < 11):
        human_choice = 0
        computer_choice = 0 
        print("computer score: " + str(computer_score) + "\tplayer score: " + str(human_score))
        print("choose one: (r)ock (p)aper (s)cissors (e)xit")
        choice = input(">")
        if choice == "e":
            return
        elif choice == "r": 
            human_choice == 1
        elif choice == "p":
            human_choice = 2
        elif choice == "s":
            human_choice = 3
        else: 
            return
        computer_choice = computer_play()
        if(computer_choice == 1 and human_choice == 1):
            print("you chose: " + num_to_string(human_choice) + "\t computer chose: " + num_to_string(computer_choice))
            print("It's a draw!")
        elif(computer_choice == 1 and human_choice == 2):
            print("you chose: " + num_to_string(human_choice) + "\t computer chose: " + num_to_string(computer_choice))
            print("You win!")
            human_score += 1
        elif(computer_choice == 1 and human_choice == 3): 
            print("you chose: " + num_to_string(human_choice) + "\t computer chose: " + num_to_string(computer_choice))
            print("You loose!")
            computer_score += 1
        elif(computer_choice == 2 and human_choice == 1):
            print("you chose: " + num_to_string(human_choice) + "\t computer chose: " + num_to_string(computer_choice))
            print("You loose!")
            computer_score += 1
        elif(computer_choice == 2 and human_choice == 2):
            print("you chose: " + num_to_string(human_choice) + "\t computer chose: " + num_to_string(computer_choice))
            print("It's a draw")
        elif(computer_choice == 2 and human_choice == 3):
            print("you chose: " + num_to_string(human_choice) + "\t computer chose: " + num_to_string(computer_choice))
            print("You win!")
            human_score += 1 
        elif(computer_choice == 3 and human_choice == 1):
            print("you chose: " + num_to_string(human_choice) + "\t computer chose: " + num_to_string(computer_choice))
            print("You win!")
            human_score += 1
        elif(computer_choice == 3 and human_choice == 2):
            print("you chose: " + num_to_string(human_choice) + "\t computer chose: " + num_to_string(computer_choice))
            print("You loose!")
            computer_score += 1
        elif(computer_choice == 3 and human_choice == 3): 
            print("you chose: " + num_to_string(human_choice) + "\t computer chose: " + num_to_string(computer_choice))
            print("It's a draw")
            print("\n\n")

def computer_play():
    choice = random.randint(1,3)
    return choice

# End Rock Paper scissors

# begin powerball
def powerball():
    sets = int(input("How many sets do you want?:")) 
    for x in range(1,sets):
        bucketA = list(range(1,53)) 
        bucketB = list(range(1,42))
        selection = ""
        for y in range(1,6):
            my_choice = random.randint(0, len(bucketA) - 1) 
            selection += str(bucketA[my_choice]) + " "
            del bucketA[my_choice]
        selection += "\tpowerball: " + str(bucketB[random.randint(0, len(bucketB) - 1)])
        print(selection)
print("Which game would you like to play? ")
print("1. Rock Paper Scissors")
print("2. PowerBall Generator")
game = int(input(">"))
if game == 1:
    print("Welcome to Rock Paper Scissors!")
    roshambo()
elif game == 2:
    print( "Welcome to the powerball machine!") 
    powerball()
