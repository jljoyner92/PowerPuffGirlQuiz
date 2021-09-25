print("Would you ever befriend a monster? [(1) Not a chance! or (2) If they were nice, sure!]")
response = input("Your Response > ")
if int(response) == 1:
    print(" You chose Not a chance!")
    print("When you find out that one of your pals is being bullied, you: [(1) Break out your color-coded anti-bullying presentation! or (2) Show her you have her back by confronting the bully yourself]")
    response = input("Your Response >")
    if int(response) == 1:
        print("YOu chose break out your color coded antibullying presentation!")
        print("Help - a villian is destroying the city! You: [(1) Start by coming up with a plan! or (2) Have already smashed their kneecaps. Next?")
        response = input("Your Response >")
        if int(response) == 1:
            print("You chose Start by coming up with a plan!")
            print("You're BLOSSOM")
        elif int(response) == 2:
            print("You chose have already smashed their kneecaps. Next?")
            print("Be honest do you think before you act? [ (1) Most of the time, yes or (2) No, I just go for it")
            response = input("Your response >")
            if int(response) == 1:
                print("You chose Most of the time, yes")
                print("You're BLOSSOM")
            elif int(response) == 2:
                print("You chose No, I just go for it")
                print(" You're BUTTERCUP")
    elif int(response) == 2:
        print("You chose show you have her back by confronting the bull yourself")
        print("Which superpower do you wish you had [(1) Freezing objects with your breath or (2) Communicating with animals")
        response = input("Your Response >")
        if int(response) == 1:
            print("You chose Freezing objects with your breath")
            print("Be honest do you think before you act? [(1) Most of the time yes or (2) No, I just go for it")
            reponse = input("Your Response >")
            if int(response) == 1:
                print("Your chose Most of the time yes")
                print("Your BLOSSOM")
            elif int(response) == 2:
                print("You chose No, I just go for it")
                print("You're BUTTERCUP")
        elif int(response) == 2:
            print("You chose Communicating with animals")
            print("Do you instantly become BFFs with everyone you meet? [(1) No, it takes me a while to warm up to someone new or (2) We're hugging right now aren't we?")
            response = input("Your Response >")
            if int(response) == 1:
                print("You chose No, it takes me a while to warm up to someone new")
                print ("You're BUTTERCUP")
            elif int(response) == 2:
                print("You chose we're hugging right now, aren't we")
                print("You're BUBBLES")
elif int(response)  == 2:
    print(" You chose If they were nice, sure!")
    print("What's your favorite color? [(1) Blue or (2) Team Green all the way")
    response = input("Your Response >")
    if int(response) == 1:
        print("You chose Blue")
        print('"Which superpower do you wish you had [(1) Freezing objects with your breath or (2) Communicating with animals')
        response = input("Your Response >")
        if int(response) == 1:
            print("You chose Freezing objects with your breath")
            print("Be honest, do you think before you act? [ (1) Most of the time, yes or (2) No, I just go for it")
            response = input("Your Response >")
            if int(response) == 1:
                print("You chose Most of the time yes")
                print("You're BLOSSOM")
            elif int(response) == 2:
                print("You chose No, I just go for it")
                print("You're BUTTERCUP")
        elif int(response) == 2:
            print("You chose Communicating with animals")
            print ("Do you instantly become BFFs with everyone you meet? [ (1) No, it takes me awhile to warm up to someone new or (2) We're hugging right now aren't we")
            response = input("Your Response >")
            if int(response) == 1:
                print("You chose Not, it takes me awhile to warm up to someone")
                print("You're BUTTERCUP")
            elif int(response) == 2:
                print("You chose We're hugging right now aren't we")
                print("You're BUBBLES")
    elif int(response) == 2:
        print("You chose Team Green all the way")
        print("Do you instantly become BFFs with everyone you meet? [ (1) No, it takes me awhile to warm up to someone new or (2) We're hugging right now aren't we ")
        response = input("Your Response >")
        if int(response) == 1:
            print("You chose No, it takes me awhile to warm up to someone")
            print("You're BUTTERCUP")
        elif int(response) == 2:
            print("You chose We're hugging right now aren't we")
            print("You're BUBBLES")