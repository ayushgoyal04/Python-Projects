import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter snake, gun, water: ")
youDict = { "snake": 1,
            "gun"  : 0,
           "water" : -1}
reverseDict = {1: "snake",
                0: "gun",
                -1: "water"}
you = youDict[youstr]
print(f"You chose {youstr} and computer chose {reverseDict[computer]}")

if computer == you:
    print("It's a tie")
else:
    if(computer == -1 and you == 1):
        print("You won")

    elif(computer == -1 and you == 0):
        print("You lost")

    elif(computer == 1 and you == -1):
        print("You lost")

    elif(computer == 1 and you == 0):
        print("You won")
        
    elif(computer == 0 and you == 1):
        print("You lost")
        
    elif(computer == 0 and you == -1):
        print("You won")

    else:
        print("Something went wrong")
        
