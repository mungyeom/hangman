while True:
    guess = input('enter a single letter ')
    if len(guess) == 1 and guess.isalpha() == True:
        break
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')


word = 'peach'
guess = input('enter a single letter ')
if guess in word:
   print("Good guess! {0} is in the word." .format(guess))
else:
    print("Sorry, {0} is not in the word. Try again." .format(guess))

word = 'apple'

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print("Good guess! {0} is in the word." .format(guess))
    else:
        print("Sorry, {0} is not in the word. Try again." .format(guess))

check_guess(guess)


def ask_for_input():
    while True:
        guess = input('enter a single letter ')
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)  

ask_for_input()