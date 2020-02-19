import dice
ansYes = ["Yes", "YES", "Y", "y", "yes"]
ansYN = ["Yes", "YES", "Y", "y", "yes", "No", "NO", "N", "n","no"]
ansNo = ["No", "NO", "N", "n","no"]


def roll():
    print("Dice one rolls", dice.dice()[0])
    print("Dice two rolls", dice.dice()[1])
    
    ans = input("Do you want to roll again?")
    while ans in ansYes:
        roll()
    while ans not in ansYN:
        ans = input("Please input a yes or no answer...")
        if ans in ansYes:
            roll()
        elif ans in ansNo:
            print("Bye")
            break
    if ans in ansNo:
        print("Bye")
        exit()

print("Dice roller")
ans = input("Do you want to roll the 2 dice?")

while ans in ansYes:
    roll()
    ans = input("Do you want to roll again?")
    
while ans not in ansYN:
        ans = input("Please input a yes or no answer...")
        if ans in ansYes:
            roll()
        elif ans in ansNo:
            print("Bye")
            break
if ans in ansNo:
    print("Bye")
    exit()
    

elif ans not in ansYN:
    ans = input("Please input a yes or no answer...")
    if ans in ansYes:
            roll()
    elif ans in ansNo:
        print("Bye")
