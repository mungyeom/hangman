# while True:
#     guess = input('enter a single letter ')
#     if len(guess) == 1 and guess.isalpha() == True:
#         break
#     else:
#         print('Invalid letter. Please, enter a single alphabetical character.')


word = 'peach'
guess = input('enter a single letter ')
if  guess in word:
    print("Good guess! {0} is in the word." .format(guess))
else:
    print("Sorry, {0} is not in the word. Try again." .format(guess))



