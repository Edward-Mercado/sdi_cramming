import random, time

target = random.randint(1, 10)
found = False
while found == False:
    try:
        number = int(input("guess a number mothafucka: "))
    except ValueError:
        print('wtf man')
        number = -10000
        
    if number == target:
        found = True
    else:
        print("ya wrong lmfao")
        time.sleep(3)
        
print('damn, ya got me')