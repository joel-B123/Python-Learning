# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string
from typing import Union, Any

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"
# hand = {}
# word = ""
# n = 0
number_of_replays = 0
# letter_substituted = 0
# Total_Score = 0
# hand_score = 0


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#

# My function 1
def compare_values(word, n):
    '''
    word: string
    n: integer >= 0
    determines if the formula is greater than "1".
    returns: result of formula or "1', whichever is higher.
    '''
    # formula for scoring a word and checking whether the result of formula is higher than 1. Then return whichever is higher
    return max(1, (7 * len(word)) - (3 * (n - len(word))))


def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    comp1 = []
    # Local function to make all letters of word lowercase
    word = word.lower()
    # begin iterable loop to get dictionary values for lowercase version of word(lc)
    for element in word:
        comp1.append(SCRABBLE_LETTER_VALUES[element])
    # assign output of function "compare_values" to comp2
    comp2 = compare_values(word, n)
    # return product of local variables(final word score)
    return sum(comp1) * comp2


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    # Iterative loop for pulling keys out of dictionary and displaying as a string
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')
            # print all on the same line
    print()  # print an empty line


#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    # Set variables
    hand = {'*': 1}
    n = n - 1
    num_vowels = int(math.ceil(n / 3))
    # Iterative loop for choosing set number of vowels
    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    # Iterative loop for choosing set number of consonants
    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    # Returns dictionary created by the iterative loops above
    return hand


#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    word = word.lower()
    new_hand = get_frequency_dict(word)
    new_hand = {key: hand[key] - new_hand.get(key, 0) for key in hand.keys()}
    new_hand = {k: v for k, v in new_hand.items() if v != 0}
    return new_hand


# My function 2
def wildcard_check(VOWELS, other_word, word):
    '''
    VOWELS: string of vowels in the alphabet
    word: string
    other_word: string, from wordlist
    Checks the length of word, checks the letters of word against the letters of words in wordlist to confirm it is a
    valid word. Also compensates for a wildcard ('*'), only useable in place of a vowel.
    '''
    # returns false if word length doesn't match
    if len(word) != len(other_word):
        return False
    for element in range(0, len(word)):
        if word[element] != '*' and word[element] != other_word[element] or word[element] == '*' and other_word[
            element] not in VOWELS:
            return False
    return True


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word = word.lower()
    dict_word = get_frequency_dict(word)
    for element in word_list:
        if wildcard_check(VOWELS, element, word):
            shared_items = {k: dict_word[k] for k in dict_word if k in hand and hand[k] >= dict_word[k]}
            return shared_items == dict_word


#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # returns length of output from update_hand function
    return len(hand)


def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    # Keep track of the total score
    # Bring in current score and run get_word_score function after each word play of the hand.
    # Then add the output of that function to the current score after each word play.
    hand_copy = hand
    first_play_score = 0
    current_score = 0
    global number_of_replays
    n = calculate_handlen(hand)
    yes = ['yes', 'y', 'yeah', 'yep', 'yup']
    # Create while loop to continue until the hand is empty.
    while len(hand) > 0:
        print()
        # Print message 'current hand' and run display_hand function on the same line.
        print("Current Hand: ", end=''),
        display_hand(hand)
        # Ask user for input
        # Create variable 'word' to accept and store user input.
        word = input('Enter word, or "!!" to indicate that you are finished: ')
        # If the input is two exclamation points:
        if word == '!!':
            print('Total score for this hand: ', current_score, 'points.')
            # check 'number_of_replays' to see if that option has already been used.
            if number_of_replays < 1:
                # assign value to variable from user input.
                replay = input('Would you like to replay the hand? ')
                if replay in yes:
                    # check if the user wants to use the "replay hand" option from variable 'replay'.
                    # add 1 to global 'number_of_replays' so the user can't use this option again.
                    # replace the hand with all the original letters of hand from the beginning of the hand.
                    # save the current hand score by assigning it to another variable.
                    # reset current score for the replay.
                    # reset to beginning of loop.
                    number_of_replays += 1
                    hand = hand_copy
                    first_play_score = current_score
                    current_score = 0
                    continue
            # end hand if user chooses not to use the "replay" option or if they no longer have the option available.
                break
            break
        # if the input is not two exclamation points:
        # run is_valid_word function.
        # for valid or invalid word:
        # run update_word function
        # blank line
        # if the word is valid:
        if is_valid_word(word, hand, word_list):
            # Update current score.
            # run 'update_hand' function.
            # Tell the user how many points the word earned,
            # and the updated total score.
            hand_score = get_word_score(word, calculate_handlen(hand))
            current_score = current_score + hand_score
            print(f'\"{word}\" earned {hand_score} points. Total: {current_score} points.')
            print()

            hand = update_hand(hand, word)
        # if the word is not valid:
        else:
            # run 'update_hand' function
            # Reject invalid word (print a message that it is not valid)
            # print a message asking the user to choose another word
            hand = update_hand(hand, word)
            print('That is not a valid word. Please choose another word.')
            print()
    # if user ran out of letters:
    # print message ('Ran out of letters.')
    # Return the total score of hand
        if len(hand) == 0:
            print('ran out of letters. Total score for this hand: ', end=''),\
            print(current_score)
            print()
            # check 'number_of_replays' to see if that option has already been used.
            if number_of_replays < 1:
                # assign value to variable from user input.
                replay = input('Would you like to replay the hand? ')
                # check if the user wants to use the "replay hand" option from variable 'replay'.
                # add 1 to global 'number_of_replays' so the user can't use this option again.
                # replace the hand with all the original letters of hand from the beginning of the hand.
                # save the current hand score by assigning it to another variable.
                # reset current score for the replay.
                # reset to beginning of loop.
                if replay in yes:
                    number_of_replays += 1
                    hand = hand_copy
                    first_play_score = current_score
                    current_score = 0
                    continue
            # end hand if user chooses not to use the "replay" option or if they no longer have the option available.
            break
    # return the highest score between both plays of the same hand.
    return max(current_score, first_play_score)


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    VOWELS: string
    """
    if letter not in hand:
        # * not specified to print anything, only to return the hand with no changes, but I thought it was better to let *
        # * the user know they made an invalid choice. *
        print('That choice is not in your hand.')
        # return the same hand with no modifications.
        return hand
    # set local variables for letters to choose from, minus the ones already in dict 'hand'.
    edited_VOWELS = VOWELS
    edited_CONSONANTS = CONSONANTS
    # iterative loop for creating variables with the letters already in dict 'hand' removed:
    # use replace function to remove corresponding values from variables and replace them with whitespace.
    for key in hand:
        if key in VOWELS or key in CONSONANTS:
            edited_VOWELS = edited_VOWELS.replace(key, '')
            edited_CONSONANTS = edited_CONSONANTS.replace(key, '')
    # if the user choice is a vowel:
    # choose a letter at random from vowels, not already in hand.
    # replace user choice 'letter' with random choice 'x', but keep the same value in dict 'hand'.
    # Use 'pop()' method to replace keys without affecting values in dict 'hand'.
    if letter in VOWELS:
        x = random.choice(edited_VOWELS)
        hand[x] = hand.pop(letter)
    # if the user choice is a consonant:
    # choose a letter at random from vowels, not already in hand.
    # replace user choice 'letter' with random choice 'x', but keep the same value in dict 'hand'.
    # Use 'pop()' method to replace keys without affecting values in dict 'hand'.
    elif letter in CONSONANTS:
        x = random.choice(edited_CONSONANTS)
        hand[x] = hand.pop(letter)
    # if the user chooses wildcard:
    # * it was not specified to do anything or print anything in instructions, but I thought it was better to *
    # * compensate for other possible choices from the user. *
    else:
        print('You cannot replace wildcard.')
    # return modified 'hand'
    return hand


def yes_substitute_hand():
    '''
    yes_no: string
    returns: boolean based on inout
    '''
    # set variable list for acceptable iterations of yes.
    yes = ['yes', 'y', 'yeah', 'yep', 'yup']
    # assign value to variable 'yes_no' from user input.
    yes_no = input('Would you like to substitute a letter: ')
    # check if user input was a 'yes' or a 'no'.
    if yes_no not in yes:
        return False
    return True


def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    # assign values to variables 'n' and 'hand'.
    n = HAND_SIZE
    total_score = 0
    substitution_used=False
    # ask user to input how many rounds they would like to play.
    rounds = int(input('Enter total number of hands: '))
    # create loop for playing the hands.
    # set loop to repeat based on the user input variable 'rounds'
    while rounds > 0:
        hand = deal_hand(n)
        print('Current Hand:', end=''),
        display_hand(hand)
        # function for checking if a letter has already been substituted on a previous hand and if the user wants to do so.
        # assign value to variable 'letter' from user input.
        # run function "substitute_hand":
        # letter substitution can only occur once per game.
        # must substitute vowel for vowel, consonant for consonant.
        if not substitution_used and yes_substitute_hand():
            substitution_used = True
            letter = input('Which letter would you like to replace: ')
            hand = substitute_hand(hand, letter)

        # assign return of function "play_hand" to the variable 'hand_score'.
        # it will run withing the assignment operation so need to run it beforehand.
        # assign the combined value of variables 'Total_Score' and 'hand_score' to variable 'Total_Score'.
        # variable 'Total_Score' will become the total of all hands played at the end of the loop.
        # can only use the "replay hand" option once.
        hand_score = play_hand(hand, word_list)
        total_score = total_score + hand_score
        rounds -= 1
    # run function to give total score to the user at the end of the game.
    print(f'Total score over all hands: {total_score}')


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
