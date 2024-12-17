command='y'
while command=="y":
    import random
    num=random.randint(0,10)
    # while (command=="y"):
    #     num=int(7)
        
    # name=input("Enter your name: ")
    print(f"Welcome ...\nFrom 0 to 10, I am thinking of a number...\nCan you guess the number... ")
    
    count =0
    guess=0
    while (guess!=num):
        count=count+1
        guess_str=input("Please guess the number = ")
        guess =int(guess_str)
        if (guess<num):
            print("The number you guessed is LOW")
        elif(guess>num):
            print("The number you guessed is HIGH")
        else:
            print("Congrats! Your guess is Right!!")
            print(f"You took {count} guesses")
    command=input('Do you want to play again (y/n): ')