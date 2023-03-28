# Step 1
import random
import ascii_code
# Step 4
# Create a list of stages in ASCII code


# Delete this
word_list = ["ardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variablr called chosen_word

chosen_word = random.choice(word_list)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# guess = input("Guess a Letter: ").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word

# for char in chosen_word:
#     if guess == char:
#         print("True")
#     else:
#         print("False")

# Step 2

# TODO-1 - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess
display = []
for char in chosen_word:
    display.append("_")


# TODO-2 - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen_word was "apple", then display should be ["_", "p", "p", "_", "_"].

# for position in range(len(chosen_word)):
#     letter = chosen_word[position]
#     if letter == guess:
#         display[position] = letter

# TODO-3 - Print 'display and you shpuld see the guessed letter in the correct position and every other letter replsce with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3
# print(display)

# Step 4
# TODO-1: - Create a variable called 'lives to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6

# Step 3
# TODO-1 - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False
while end_of_game == False:
    guess = input("Guess a Letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
# Step 4
# TODO-2: - iF Guess is not a letter in the chosen_word,
# Then reduce 'lives' by 1.
# If lives goes down to 0 then the game should stop and it should print "You Lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You Lose')
    # Join all the elements in the list and turn it into a String
    print(f"{''.join(display)}")
    # Check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win")
    print(ascii_code.stages[lives])
