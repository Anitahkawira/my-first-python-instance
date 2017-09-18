import random
number_of_guesses =10
number = random.randint(1,100)
print("Guess the number i have")

while number_of_guesses <=10:
    print("you have "+str(number_of_guesses)+ "chances left")
    guess = input()
    guess = int(guess)
    
    number_of_guesses = number_of_guesses -1
    if guess <number:
        print("your guess is too low. keep trying.")
        
    if guess > number:
        break
    
    if guess == number:
        number_of_guesses = 10- number_of_guesses
        number_of_guesses = str(number_of_guesses)
        print("congratulation you have guessed the right number. Thank you for playing." + "you guessed my number in" + number_of_guesses + "guesses!")
    
    if guess !=number:
        number = str(number)
        print("No. The number i was thinking of was" + number)