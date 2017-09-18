print("Guess a number")
values = range(101)
def guesser (guess):
    guess = int(guess)
    if guess < 50:
    return "Nice try, but the number is too low, try again"
    elif guess > 50:
    return "Nice try, but the number is too high, try again"
    else:
        return "Congratulations you have guessed the right number"