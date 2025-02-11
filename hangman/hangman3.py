# hangman.py
import random
from wordlist import word_list
from art import logo, stages

def get_hint(word):
    vowels = 'aeiou'
    hint = []
    for letter in word:
        if letter in vowels:
            hint.append(letter)
        else:
            hint.append('_')
    return ''.join(hint)

def display_hints(word):
    indices = random.sample(range(len(word)), 2)
    hint = ['_' if i not in indices else word[i] for i in range(len(word))]
    return ''.join(hint)

def hangman():
    print(logo)
    word = random.choice(word_list)
    word_length = len(word)
    end_of_game = False
    lives = 6

    display = ['_'] * word_length
    guessed_letters = []

    print(f"The word has {word_length} letters: {' '.join(display)}")
    print(f"Hint: {display_hints(word)}")

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print(f"You've already guessed {guess}")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for position in range(word_length):
                if word[position] == guess:
                    display[position] = guess
            print(f"Good guess! {' '.join(display)}")
        else:
            lives -= 1
            print(f"{guess} is not in the word. You lose a life.")
            print(stages[lives])

        if lives == 0:
            end_of_game = True
            print(f"You lost! The word was: {word}")
        elif '_' not in display:
            end_of_game = True
            print("Congratulations, you won!")

if __name__ == "__main__":
    hangman()
