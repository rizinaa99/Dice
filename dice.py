import random
min = 1
max = 7
N = int(input("enter the number of dice you want to roll?"))
roll_again = "yes"

for i in range(1,3):
    print (random.randint(min, max))
