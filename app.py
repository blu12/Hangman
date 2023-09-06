HANGMAN_ASCII_ART = """ Welcome to The game Hangman
   _    _ 
  | |  | | 
  | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
  |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
  | |  | | (_| | | | | (_| | | | | | | (_| | | | |
  |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                       __/ |
                       |___/ """

MAX_TRIES = 6

old_letters_guessed = []

num_of_tries = 0

HANGMAN_ART0 = "x-------x"

HANGMAN_ART1 = """
x-------x
|       
|       
|
|
|"""

HANGMAN_ART2 = """
x-------x
|       |
|       0
|       
|
|"""

HANGMAN_ART3 = """
x-------x
|       |
|       0
|       |
|
|"""

HANGMAN_ART4 = """
x-------x
|       |
|       0
|      /|\\
|
|"""

HANGMAN_ART5 = """
x-------x
|       |
|       0
|      /|\\
|      /
|
|
|"""

HANGMAN_ART6 = """
x-------x
|       |
|       0
|      /|\\
|      / \\
|
|
|
|"""


HANGMAN_PHOTOS = {1: HANGMAN_ART1, 2: HANGMAN_ART2, 3: HANGMAN_ART3, 4: HANGMAN_ART4, 5: HANGMAN_ART5, 6: HANGMAN_ART6}


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Checks if the input is a letter and if only one letter was typed in
    :param letter_guessed: One letter typed by the user
    :param old_letters_guessed: A list of all the letters guessed by the user
    :return: True or False
    """
    if not letter_guessed.isalpha() and len(letter_guessed) > 1:
        return False
    elif letter_guessed in old_letters_guessed:
        return False
    elif not letter_guessed.isalpha():
        return False
    elif len(letter_guessed) > 1:
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Used the check_valid_input method to check if the letter was already guessed by the user
    or if the input is invalid.
    :param letter_guessed: One letter typed by the user
    :param old_letters_guessed: A list of all the letters guessed by the user
    :return: True or False
    """
    check_valid_input(letter_guessed, old_letters_guessed)
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    elif not check_valid_input(letter_guessed, old_letters_guessed):
        print("X")
        print(" -> ".join(old_letters_guessed))
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    """
    Returns a list composed of underscores and letters guessed by the user via the old_letters_guessed list
    :param secret_word: The word the user needs to find out
    :param old_letters_guessed: A list of all the letters guessed by the user
    :return: List of underscores and letters guessed by the user
    """
    str = ""
    word = list(secret_word)
    for i in word:
        if i in old_letters_guessed:
            str = str + i + " "
        else:
            str = str + "_ "
    return str


def check_win(secret_word, old_letters_guessed):
    """
    Checks if all the letters in the old_letters_guessed list are in the secret word
    :param secret_word: The word the user needs to find out
    :param old_letters_guessed: A list of all the letters guessed by the user
    :return: True or False
    """
    cnt = 0

    for letter in secret_word:
        if letter in old_letters_guessed:
            cnt = cnt + 1
    if cnt == len(secret_word):
        return True
    else:
        return False


def choose_word(file_path, index):
    """
    Returns a word from a file that the user chooses by typing in a number between 1
    and 5
    :param file_path: Contains a list of words for the user to guess
    :param index: Input for the user, types in a number between 1 and five
    :return: Worto guess
    """
    readText = open(file_path, "r")
    readText1 = readText.readline()
    readText2 = readText1.split()
    wordChosen = readText2[index - 1]
    readText.close()
    return wordChosen


def print_hangman(num_of_tries):
    # Prints an image of hangman depending on the number of tries
    print(HANGMAN_PHOTOS[num_of_tries])


def print_welcome():
    print(HANGMAN_ASCII_ART)
    print("You have " + str(MAX_TRIES) + " tries")


def main():
    global old_letters_guessed
    global num_of_tries
    global MAX_TRIES
    print_welcome()
    num = int(input("Please enter a random number between 1 to 5 to select a word to guess: "))
    word_chosen = choose_word("words.txt", num)
    print()
    print("Let's start!")
    print()
    print(HANGMAN_ART0)
    print()
    print(show_hidden_word(word_chosen, old_letters_guessed))
    print()
    while num_of_tries != MAX_TRIES and check_win(word_chosen, old_letters_guessed) is False:
        letter = input("Guess a letter: ")
        if try_update_letter_guessed(letter, old_letters_guessed) is False:
            0
        elif letter not in show_hidden_word(word_chosen, old_letters_guessed):
            print(":(")
            print(show_hidden_word(word_chosen, old_letters_guessed))
            num_of_tries = num_of_tries + 1
            print_hangman(num_of_tries)
        else:
            print(show_hidden_word(word_chosen, old_letters_guessed))

    if check_win(word_chosen, old_letters_guessed) is True:
        print("WIN")
    else:
        print("LOSE")


if __name__ == "__main__":
    main()
