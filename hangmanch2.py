import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word 
# and 'display' has no more blanks ("_"). Then you can tell the user they've won.

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#display = []
#for n in range(0,len(chosen_word)):
#   display.append("_")
#print(display)   
# Testing code

#print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display
display = ["_"] * len(chosen_word)
print(display)

chk = ""

while chk != chosen_word:
    guess = input("Guess a letter: ").lower()
    
    # Loop through each position in the chosen_word
    for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
            display[index] = guess
    
    # Update chk to be the string formed by joining display list
    chk = "".join(display)
    
    # Print 'display' to show the guessed letter in the correct position
    print(display)

print("Congratulations! You've won.")
