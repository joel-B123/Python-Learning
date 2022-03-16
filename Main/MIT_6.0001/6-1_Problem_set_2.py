# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

# Set variables for defining functions
wordlist = load_words()
letters_guessed=[]
alphabet=("abcdefghijklmnopqrstuvwxyz")
# secret_word = choose_word(wordlist)

# Lines for testing
# letter_guessed=[]
# secret_word=str("dialect")


def is_word_guessed(letters_guessed, secret_word):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # Set local variables
    guess=[]
    # Loop to iterate through letters of a variable
    for element in secret_word:
        if element in letters_guessed:
            guess.append(element)
        else:
            pass
    guess=''.join(guess)
    if guess==secret_word:
    # boolean return of function completing
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # Set local variables
    # Local variable to output desired return without altering the arguments
    my_word=[]
    # Loop to iterate through the letters of variable
    for element in secret_word:
        if element in letters_guessed:
            my_word.append(element)
        else:
            my_word.append("_")
    my_word=''.join(my_word)
    # Output result of function completing
    return my_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # Set local variable
    remaining_letters="abcdefghijklmnopqrstuvwxyz"
    # Conversion so the variable can be iterated
    remaining_letters=list(remaining_letters)
    # Loop to iterate through the letters of variable
    for element in letters_guessed:
        if element in remaining_letters:
            remaining_letters.remove(element)
    remaining_letters=''.join(remaining_letters)
    # Output result of function completing
    return remaining_letters


def is_guess_repeated(letters_guessed, letter):
    '''
    letters_guessed: String, composed of user guesses.
    
    letter: User guess.
    
    returns: boolean, dependant on whether letter is already contained in letters_guessed.
    '''
    # Check if the users guess has already been guessed
    if letter in letters_guessed:
    # Boolean returns
        return True
    else:
        return False


def is_guess_a_letter(letter, alphabet):
    '''
    letter: User guess.
    
    alphabet: String of all letters of the alphabet.
    
    returns: boolean, dependant on whether the letter is contained in the alphabet.
    '''
    # Check if user guess is a letter
    if letter not in alphabet:
    # Boolean returns
        return True
    else:
        return False


def score(secret_word, n):
    '''
    secret_word: string, the secret word to guess.
    
    n: number of remaining guesses.
    
    returns: product of n and number of unique letters in secret_word.
    '''
    # Creates set of unique letters in variable secret_word
    S=set(secret_word)
    # calculates and outputs users score if game is won
    return n*len(S)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''    
    # Set invalid and Incorrect guess counters
    w=3
    n=6
    # Introduction to the Game
    print("Welcome to the game Hangman!")
    # Gives length of word to user
    print("I am thinking of a word that is",len(secret_word), "letters long.")
    # Gives how many warnings the user has to start the game
    print("You have", w, "warnings left: ")
    # Loop for user input and gameplay reliant on counter
    while n>0:     
        # print('_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_')
        print("You have", n, "guesses left")
        alphabet=("abcdefghijklmnopqrstuvwxyz")
    # Lets user know how many guesses they have left
    # Calls function for letters not yet guessed
        print(get_available_letters(letters_guessed))
    # User defined variable
        letter=input("Please guess a letter: ")
    # function for validity check of guess 1
        is_guess_repeated(letters_guessed, letter)
        if is_guess_repeated(letters_guessed, letter):
            if w>0:
                w-=1
                print("Oops! You have already guessed that letter. You have", w, "warnings left:")
                print(get_guessed_word(secret_word, letters_guessed))
                print('_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_')
                continue
            else:
                n-=1
                print("Oops! You have already guessed that letter. You have no warnings left")
                print("so you lose one guess: ")
                print(get_guessed_word(secret_word, letters_guessed))
                print('_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_')
                continue
        else:
            pass
        # function for validity check of guess 2
        is_guess_a_letter(letter, alphabet)
        if is_guess_a_letter(letter, alphabet):
            if w>0:
                w-=1
                print("Oops! That is not a valid letter. You have", w, "warnings left:")
                print(get_guessed_word(secret_word, letters_guessed))
                print('_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_')
                continue
            else:
                n-=1
                print("Oops! That is not a valid letter. You have no warnings left")
                print("so you lose one guess: ")
                print(get_guessed_word(secret_word, letters_guessed))
                print('_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_')
                continue
        else:
            pass
    # Adding user defined variable to list
        letters_guessed.append(letter)
    # Check if user defined variable is correct for each time through the loop
        if (letter) in (secret_word):
    # Lets the user know they guessed correctly
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            print('_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_')
    # Calls function to check if all the letters of the word have been guessed, returns a boolean
            is_word_guessed(secret_word, letters_guessed)
    # Checks if boolean from function is true
            if is_word_guessed(letters_guessed, secret_word):
    # Lets user know the word they guessed the word and won the game of hangman
                print("Congratulations, You won!")
                print("Your total score for this game is", score(secret_word, n))
    # Ends loop early
                break
    # instructions if boolean from function is false
            else:
    # Continue loop
                pass
    # instructions if "letter" variable check is false
        else:
    # Counter decreases
            n-=1
            print("Oops! That letter is not in my word.")
            print("Please guess a letter: ", get_guessed_word(secret_word, letters_guessed))
            print('_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_')
            continue
    # calls function for showing word with unguessed letters missing
    #     get_guessed_word(secret_word, letters_guessed)
    # Prints return from above function
        # print(get_guessed_word(secret_word, letters_guessed))
    if n==0:
    # Lets user know they used all their incorrect guesses so the game is over
        print("Sorry, you ran out of guesses. The word was", secret_word)


# secret_word = choose_word(wordlist)
# hangman(secret_word)        

# For Game with hints


# my_word=get_guessed_word(secret_word, letters_guessed)



def word_length_match(my_word, other_word):
    '''
    my_word : Variable output from get_guessed_word function.
    other_word : variable from wordlist
    returns: boolenan, true if same length, false otherwise
    '''
    if len(other_word) == len(my_word):
        return True
    else:
        return False         


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    m=0
    for element in range(0,len(my_word)):
        if my_word[element] == "_" and other_word[element] not in letters_guessed or my_word[element] == other_word[element]:
            m+=1
        if m==len(my_word):
            return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
              Keep in mind that in hangman when a letter is guessed, all the positions
              at which that letter occurs in the secret word are revealed.
              Therefore, the hidden letter(_ ) cannot be one of the letters in the word
              that has already been revealed.
    '''
    wordlist_reduced=[]
    possible_matches=[]
    for element in wordlist:
        other_word=element
        word_length_match(my_word, other_word)
        if word_length_match(my_word, other_word):
            wordlist_reduced.append(element)
    for element in wordlist_reduced:
        other_word=element
        match_with_gaps(my_word, other_word)
        if match_with_gaps(my_word, other_word):
            possible_matches.append(other_word)
        else:
            continue
    print("Possible word matches are: ")
    print(possible_matches)


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # Set invalid and Incorrect guess counters
    w=3
    n=6
    # Introduction to the Game
    print("Welcome to the game Hangman!")
    # Gives length of word to user
    print("I am thinking of a word that is",len(secret_word), "letters long.")
    # Gives how many warnings the user has to start the game
    print("You have", w, "warnings left: ")
    # Loop for user input and gameplay reliant on counter
    while n>0:     
        # print('_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_')
        print("You have", n, "guesses left")
        alphabet=("abcdefghijklmnopqrstuvwxyz")
    # Lets user know how many guesses they have left
    # Calls function for letters not yet guessed
        print(get_available_letters(letters_guessed))
    # User defined variable
        letter=input("Please guess a letter: ")
        # function to create variable
        get_guessed_word(secret_word, letters_guessed)
        # set variable
        my_word=get_guessed_word(secret_word, letters_guessed)
        if letter == "*":
            # function for giving hints
            show_possible_matches(my_word)
            continue
        else:
            pass
        is_guess_repeated(letters_guessed, letter)
        if is_guess_repeated(letters_guessed, letter):
            if w>0:
                w-=1
                print("Oops! You have already guessed that letter. You have", w, "warnings left:")
                print(get_guessed_word(secret_word, letters_guessed))
                print('_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_')
                continue
            else:
                n-=1
                print("Oops! You have already guessed that letter. You have no warnings left")
                print("so you lose one guess: ")
                print(get_guessed_word(secret_word, letters_guessed))
                print('_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_')
                continue
        else:
            pass
        is_guess_a_letter(letter, alphabet)
        if is_guess_a_letter(letter, alphabet):
            if w>0:
                w-=1
                print("Oops! That is not a valid letter. You have", w, "warnings left:")
                print(get_guessed_word(secret_word, letters_guessed))
                print('_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_')
                continue
            else:
                n-=1
                print("Oops! That is not a valid letter. You have no warnings left")
                print("so you lose one guess: ")
                print(get_guessed_word(secret_word, letters_guessed))
                print('_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_')
                continue
        else:
            pass
        # Adding user defined variable to list
        letters_guessed.append(letter)
        # Check if user defined variable is correct for each time through the loop
        if (letter) in (secret_word):
        # Lets the user know they guessed correctly
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            print('_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_')
        # Calls function to check if all the letters of the word have been guessed, returns a boolean
            is_word_guessed(secret_word, letters_guessed)
        # Checks if boolean from function is true
            if is_word_guessed(letters_guessed, secret_word):
        # Lets user know the word they guessed the word and won the game of hangman
                print("Congratulations, You won!")
                print("Your total score for this game is", score(secret_word, n))
        # Ends loop early
                break
        # instructions if boolean from function is false
            else:
        # Continue loop
                pass
        # instructions if "letter" variable check is false
        else:
        # Counter decreases
            n-=1
            print("Oops! That letter is not in my word.")
            print("Please guess a letter: ", get_guessed_word(secret_word, letters_guessed))
            print('_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_')
            continue
    if n==0:
        # Lets user know they used all their incorrect guesses so the game is over
        print("Sorry, you ran out of guesses. The word was", secret_word)


secret_word = choose_word(wordlist)
# my_word=get_guessed_word(secret_word, letters_guessed)
hangman_with_hints(secret_word)
