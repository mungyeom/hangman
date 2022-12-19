import random

class Hangman:
    def __init__(self, word_list,num_lives):
        self.word_list = word_list
        self.num_lives = 5
        self.word = random.choice(word_list)
        self.word_guessed = list(len(self.word)* '_')
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print("Good guess! {0} is in the word." .format(guess))
            for i in range(0,len(self.word)):
                letter = self.word[i]
                if letter == guess:
                    guess = self.word_guessed[i]
        # else:
        #     self.num_lives -= 1
        #     print(f"Sorry, {letter} is not in the word.")
        #     print(f"You have {self.num_lives} lives left.")
        else:
            self.num_lives -= 1
        self.list_of_guesses.append(guess)

    def ask_for_input(self):
        while True:
            guess = input('enter a single letter ')
            if len(guess) != 1 or guess.isalpha() != True:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break


