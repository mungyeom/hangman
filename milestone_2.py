import random
word_list = ['Banana', 'kiwi', 'Grape', 'Peach', 'Orange']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input('enter a single letter ')
if len(guess) == 1 and guess.isalpha() == True:
    print( "Good guess!")
else:
    print("Oops! That is not a valid input.")