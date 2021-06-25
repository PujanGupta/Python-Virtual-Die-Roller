import random, time

timesRolled = 0

def rollDie(DieSides=int(), delay=0):
    options = []
    for n in range(1, DieSides + 1):
        options.append(n)
        
    if delay:
        time.sleep(delay)
    else:
        pass
    
    return(
        random.choice(options)
    )
    
print("Creating a virtual die....")

while True:
    userInput = int(input("Number of sides die should have: "))
    print("Rolling Die..")
    time.sleep(0.65)
    print(f"The number shown on the die is {rollDie(userInput, 0.75)}")       