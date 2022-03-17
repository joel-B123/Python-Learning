
# Problem Set 4B
# Name: Joel Buehner

import string


### HELPER CODE ###
def load_words(file_name):
    """
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def is_word(word_list, word):
    """
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'


class Message(object):
    def __init__(self, text):
        """
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        self.message_text = text
        self.valid_words = list(load_words(WORDLIST_FILENAME))

    def get_message_text(self):
        """
        Used to safely access self.message_text outside the class

        Returns: self.message_text
        """
        return self.get_message_text

    def get_valid_words(self):
        """
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        """
        valid_words = self.valid_words
        return valid_words

    def build_shift_dict(self, shift):
        """
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        """
        result = {}
        for i in range(0, len(string.ascii_lowercase)):
            j = (i + shift) % len(string.ascii_lowercase)
            result[string.ascii_lowercase[i]] = string.ascii_lowercase[j]
            result[string.ascii_uppercase[i]] = string.ascii_uppercase[j]
        return result
        #
        # # declare temporary variables
        # # one for lowercase and one for uppercase
        # shifted = ""
        # shifted2 = ""
        # # loops for creating shifted strings
        # # first loop for creating lowercase string(values in shifted_dict)
        # for i in range(0, len(string.ascii_lowercase)):
        #     i = i + shift
        #     # when index out of range, resets to position 0
        #     if i > 25:
        #         j = i - 25
        #         j = j - 1
        #     else:
        #         j = i
        #     j = string.ascii_lowercase[j]
        #     shifted = shifted + j
        # # second loop for creating uppercase string(values for shifted_dict)
        # for i in range(0, len(string.ascii_uppercase)):
        #     i = i + shift
        #     # when index out of range, resets to position 0
        #     if i > 25:
        #         j = i - 25
        #         j = j - 1
        #     else:
        #         j = i
        #     j = string.ascii_uppercase[j]
        #     shifted2 = shifted2 + j
        # # combines two (value) strings to one string
        # shifted_ascii_letters = shifted + shifted2
        # # declare dictionary
        # shifted_dict = {}
        # # third loop to create shifted_dict(keys:string of letters(lower and upper), values:shifted string of letters(lower and upper))
        # for i in range(0, len(shifted_ascii_letters)):
        #     shifted_dict[string.ascii_letters[i]] = shifted_ascii_letters[i]
        # # returns dictionary used for encryption
        # return shifted_dict

    def apply_shift(self, shift):
        """
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        """
        # set variable for new ecrypted string
        encrypted_message = ""
        # pull in dictionary from method build_shift_dict
        encryption_key = self.build_shift_dict(shift)
        # loop to replace letters of message with values from shifted dictionary
        for i in self.message_text:
            # qualifier for i, if it's a symbol or whitespace then add that to the new encrypted string
            if i not in encryption_key:
                encrypted_message = encrypted_message + i
            else:
                j = encryption_key.get(i)
                encrypted_message = encrypted_message + j
        # returns encrypted string
        return encrypted_message


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        """
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        """
        Message.__init__(self, text)
        self.shift = shift

    def get_shift(self):
        """
        Used to safely access self.shift outside of the class

        Returns: self.shift
        """
        return self.shift

    def get_encryption_dict(self):
        """
        Used to safely access a copy self.encryption_dict outside of the class

        Returns: a COPY of self.encryption_dict
        """
        self.build_shift_dict(self.shift)

    def get_message_text_encrypted(self):
        """
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        """
        return self.apply_shift(self.shift)

    def change_shift(self, shift):
        """
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift.

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        """
        self.shift = shift % 26


class CiphertextMessage(Message):
    def __init__(self, text):
        """
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        Message.__init__(self, text)

    def decrypt_message(self):
        """
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create
        the maximum number of valid words, you may choose any of those shifts
        (and their corresponding decrypted messages) to return.

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        """
        # set variables for shift
        # loop for testing value of "s" is correct cypher shift
        shift = 25
        best_correct = 0
        best_shift = 0
        while shift >= 0:
            decrypted_message = self.apply_shift(shift)
            words = decrypted_message.split(" ")
            num_correct = 0
            for i in words:
                if is_word(self.get_valid_words(), i):
                    num_correct += 1
            if num_correct > best_correct:
                best_correct = num_correct
                best_shift = shift
                best_decrypted = decrypted_message
            shift -= 1
        return best_shift, best_decrypted


if __name__ == '__main__':
    # Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())

    # TODO: WRITE YOUR TEST CASES HERE
    # My example test case 1 (PlaintextMessage)
    plaintext = PlaintextMessage('Welcome tO My 53 worldS!', 12)
    print('Expected Output: iqxoayq fa yk iadxp!')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    # My example test case 1 (CiphertextMessage)
    ciphertext = CiphertextMessage('Iqxoayq fA Yk 53 iadxpE!')
    print('Expected Output:', (14, 'Welcome tO My 53 worldS!'))
    print('Actual Output:', ciphertext.decrypt_message())

    # My example test case 2 (PlaintextMessage)
    plaintext = PlaintextMessage('I rock at_ "ciphers!!"', 7)
    print('Expected Output: P yvjr ha_ "jpwolyz!!"')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    # My example test case 2 (CiphertextMessage)
    ciphertext = CiphertextMessage('P yvjr ha_ "jpwolyz!!"')
    print('Expected Output:', (19, 'I rock at_ "ciphers!!"'))
    print('Actual Output:', ciphertext.decrypt_message())

    # TODO: best shift value and unencrypted story

    # Story.txt decryption
    ciphertext = CiphertextMessage(get_story_string())
    print(ciphertext.decrypt_message())
