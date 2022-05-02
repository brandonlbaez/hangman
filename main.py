import random
import copy
attempts = 5
wordlist = ["banana", "apple", "orange"]
chosen_word = list(random.choice(wordlist))
reference_word = copy.deepcopy(chosen_word)
print(reference_word)
for i in range(len(chosen_word)):
    chosen_word[i] = '*'
    hidden_word = chosen_word[i]
print("this is hangman. guess a letter and hit enter.")
while attempts > 0:
    guess = input()
    if guess == reference_word[0:]:
        for i in range(len(reference_word)):
            if reference_word[i] == guess:
                hidden_word = list(map(lambda item: item.replace("*",input()), hidden_word))
                print(hidden_word)
    else:
        attempts = attempts - 1
        print(False)
        print(attempts)
    if guess == chosen_word:
        print("you win.")
        break
if attempts == 0:
    print("you lose.")
