HANGMAN_ASCII_ART = r"""
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""
MAX_TRIES = 6
HANGMAN_PHOTOS = {
0: """
x-------x""",
1: """
x-------x
|
|
|
|
|""",
2: """
x-------x
|       |
|       0
|
|
|""",
3: """
x-------x
|       |
|       0
|       |
|
|""",
4: """
x-------x
|       |
|       0
|      /|\ 
|
|""",
5: """
x-------x
|       |
|       0
|      /|\ 
|      /
|""",
6: """
x-------x
|       |
|       0
|      /|\ 
|      / \ 
|"""}


def open_screen():
    print(f'{HANGMAN_ASCII_ART}\nMax Tries: {MAX_TRIES}')
    return None


def choose_word(file_path, index):
    """Choosing word from a text file.
    :param file_path: file's path location
    :param index: selected word's index
    :type file_path: string
    :type index: int
    :return: The selected word
    :rtype: string
    """
    with open(file_path, 'r') as words:
        words_data = words.read()
        words_list = words_data.split(' ')
        if index > len(words_list):
            index = 1
        chosen_word = words_list[index - 1].replace('\n', '')
        return chosen_word


def check_valid_input(letter_guessed, old_letters_guessed):
    """this function get a string param and list of letter that the user alredy guessed
    and check's if the the letter is from alphabet
    and also check's if the letter is not a sign and return treu if the letter is good
    and also check's if the user already guessed this letter.
    and false if its not.
    :param letter_guessed: guessed letter from the user
    :type letter_guessed: string
    :return: true if the letter is correct false if it's not
    :rtype:bool"""
    if letter_guessed.isalpha() and len(letter_guessed) == 1 and letter_guessed.lower() not in old_letters_guessed:
        return True
    else:
        return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word):
    global num_of_tries
    """this function get a letter from the user and a list of letter that the user already guessed,
    and check's if the letter is new it will append the letter to the list of the letter allredy guessed and print 'X' and under the list of letter that guessed with -> between them
    :param letter_guessed: letter from the user
    :param old_letter_guessed: list of letter allredy guessed
    :type letter_guessed: string
    :type old_letter_guessed: list
    :return: true or false
    :rtype: bool"""
    if not check_valid_input(letter_guessed, old_letters_guessed):
        print('X')
        old_letters_guessed.sort()
        print(" -> ".join(old_letters_guessed))
    else:
        if letter_guessed.lower() not in secret_word:
            old_letters_guessed.append(letter_guessed.lower())
            num_of_tries += 1
            print(':(')
            print(print_status(num_of_tries))
            print(show_hidden_word(secret_word, old_letters_guessed))
        else:
            old_letters_guessed.append(letter_guessed.lower())
            print(show_hidden_word(secret_word, old_letters_guessed))


def show_hidden_word(secret_word, old_letters_guessed):
    '''show the status of the hiiden word.
    :param secret_word: user's chosen word
    :param old_letters_guessed: List of guessed letters
    :type secret_word: String
    :type old_letters_guessed:list
    :return: variable 'result' which contain the status of the letter allready gussed
     :rtype: str'''
    currect_guess = ['']
    for letter in secret_word:
        if letter in old_letters_guessed:
            currect_guess.append(letter + " ")
        else:
            currect_guess.append("_ ")
        result = ''.join(currect_guess)
    return result


def check_win(secret_word, old_letters_guessed):
    """check if the user win the game or not
    :param secret_word: user's chosen word
    :param old_letters_guessed: List of guessed letters
    :type secret_word: String
    :type old_letters_guessed:list
    :return:true if the user guessed all the leter in the word of false if not
    :rtype:bool"""
    if ''.join(show_hidden_word(secret_word, old_letters_guessed).split()) in secret_word:
        print('YOU WIN!\nGOOD JOB!!!')
        return True
    return False


def word_len(secret_word):
    return '_ ' * len(secret_word)


def print_status(num_of_tries):
    return (HANGMAN_PHOTOS[num_of_tries])


num_of_tries = 0


def main():
    open_screen()
    global num_of_tries
    secret_word = input(r"Please enter word: ").lower()
    old_letters_guessed = []
    print('Lets start!')
    print(HANGMAN_PHOTOS[num_of_tries])
    print(word_len(secret_word))
    while num_of_tries < MAX_TRIES:
        try_update_letter_guessed(input('Enter a letter: '), old_letters_guessed, secret_word)
        show_hidden_word(secret_word, old_letters_guessed)
        game_status = check_win(secret_word, old_letters_guessed)
        if game_status:
            break
    if not game_status:
        print('GAME OVER!')


if __name__ == "__main__":
    main()
