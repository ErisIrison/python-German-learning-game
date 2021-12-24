import random
finished = False
numm = 0
prenumm = 0
while not finished:
    if numm != 0:
        prenumm = numm
    numm = random.randint(1, 6)
    while prenumm == numm:
        numm = random.randint(1, 6)
    if numm == 1:
        answer = input("Tail of verbs for Ich: ")
        if answer == "e":
            print("Correct!")
        else:
            print("The answer is e")
            
    elif numm == 2:
        answer = input("Tail of verbs for du: ")
        if answer == "st":
            print("Correct!")
        else:
            print("The answer is st")

    elif numm == 3:
        answer = input("Tail of verbs for er/sie/es: ")
        if answer == "t":
            print("Correct!")
        else:
            print("The answer is t")

    elif numm == 4:
        answer = input("Tail of verbs for wir: ")
        if answer == "en":
            print("Correct!")
        else:
            print("The answer is en")

    elif numm == 5:
        answer = input("Tail of verbs for ihr: ")
        if answer == "t":
            print("Correct!")
        else:
            print("The answer is t")

    elif numm == 6:
        answer = input("Tail of verbs for Sie/ sie: ")
        if answer == "en":
            print("Correct!")
        else:
            print("The answer is en")
