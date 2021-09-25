print("Your BFFs would say you're [(1) Confident or (2) Fearless]")
response = input("Your Response > ")
if int(response) == 1:
    print("You chose confident!")
    print("Help - a villian is destroying the city! You [ (1) Start by coming up with a plan! or (2) Have already smashed their kneecaps. Next? ]")
    response = input("Your response > ")
    if int(response) == 1:
        print("You chose Start by coming up with a plan!")
        print("You're BLOSSOM.......")
        exit(0)
    elif int(response) == 2:
        print("You chose...")
elif int(response) == 2:
    print("you chose Fearless")

else:
    print("You submitted an invalid response, exiting...")
    exit(1)

