import random
attempts = 5
wordlist = ["banana", "apple", "orange"]
chosen_word = list(random.choice(wordlist))
hidden_word = ["*"] * len(chosen_word)
print("this is hangman. guess a letter and hit enter.")
while attempts > 0:
    guess = input()
    if guess in chosen_word:
        for i in range(len(hidden_word)):
            if chosen_word[i] == guess:
                hidden_word[i] = guess
        print(hidden_word)
    else:
        attempts = attempts - 1
        print(False)
        print(attempts)
    if hidden_word == chosen_word:
        print("you win.")
        break
if attempts == 0:
    print("you lose.")
