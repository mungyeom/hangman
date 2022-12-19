import random

class Hangman:
    def __init__(self, word_list,num_lives):
        self.word_list = word_list
        self.num_lives = num_lives
        num_lives = 5
        word = random.choice(word_list)
        word_guessed = list(len(word)* '_')
        num_letters = [len(word_guessed)]
        list_of_guesses = []
        print(num_letters)
        print(word_guessed)
        print(list_of_guesses)
    
        

