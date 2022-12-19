import random

class Hangman:
    def __init__(self, word_list,num_lives):
        self.word_list = word_list
        self.num_lives = num_lives
        num_lives = 5
        self.word = random.choice(word_list)
        self.word_guessed = list(len(self.word)* '_')
        print(self.word_guessed)
        self.num_letters = len(set(self.word))
        print(self.num_letters)
        self.list_of_guesses = []


    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            self.num_letters -=1
            print("Good guess! {0} is in the word." .format(guess))
            for i in range(0,len(self.word)):
                letter = self.word[i]
                if guess == letter:
                    self.word_guessed[i] = guess
                    print(self.word_guessed)
        else:
            self.num_lives -= 1
            print("Sorry, {letter} is not in the word." .format(letter = guess))
            print(f"You have {self.num_lives} lives left.")
        
           

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


def play_game(word_list):
    game = Hangman(word_list,5)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        if game.num_letters >= 0:
            game.ask_for_input()
        if game.num_lives > 0 and game.num_letters <= 0:
            print('Congratulations. You won the game!')
            break

word_list = ['kiwi','banana', 'watermelon', 'orange','apple']
play_game(word_list)

