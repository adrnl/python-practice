def getGuess(request, guesses)
    guess = input(request)
    guess = guess.lower()
    if len(guess) != 1:
        getGuess("Player 2, please guess a SINGLE LETTER: ")
    elif guess in guesses:
        getGuess("Player 2, you have already guessed that letter, try again: ")
    return guess

def Hangman():
    secret = input("Player 1, enter your word: ")
    secret = secret.lower()
    guesses = []
    failures = 0
    progress = "_" * len(secret)

    while failures <= 6 and progress != secret:
        print(f'Current status: {progress}')
        guess = getGuess("Player 2, guess a letter: ", guesses)
        guesses.append(guess)

        if guess not in secret:
            failures += 1
        else:





