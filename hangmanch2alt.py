import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display
display = ["_"] * len(chosen_word)
print(display)

while "_" in display:
    guess = input("Guess a letter: ").lower()
    
    # Loop through each position in the chosen_word
    for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
            display[index] = guess
    
    # Print 'display' to show the guessed letter in the correct position
    print(display)

print("Congratulations! You've won.")
