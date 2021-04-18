import random #importing the necessary module
person=input("Enter your name : ")
print("Good Luck "+ person + "!")
file = open("C:/Users/hanis/names.txt")
names=file.readlines() #to read
name=random.choice(names) # for random choice
name=name.lower()
name=str(name).strip('\n') # to neglect this charcater
name=str(name).strip('\r')
print("Guess the characters !")
guesses= str() #string tyecasting
if ' ' in name:
    guesses+=' '
turns=6 # setting constrains  
while turns>0 :
    failed=0 #declaration of flag
    for char in name:
        if char in guesses:  # if the correct character is guessed print the charcter wherever it's present till the end
         print(char,end=' ')  
        else:
            print('_',end=' ')#else print the blanks and change the value of flag
            failed+=1
    if failed ==0:
        print("\nYou Win!")
        exit()   
    guess= input("\n\nGuess a charcter: ") 
    guesses+=guess 
    if guess not in name:
        turns-=1
        print("Wrong")
        print("You have "+ str(turns)+ " more guesses")
    if turns==0:
        print("You Lose")   
        print("The move was: ",name)

