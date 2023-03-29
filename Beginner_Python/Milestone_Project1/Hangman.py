import random
from ascii_code import stages, logo
import List_of_words
from replit import clear

print(logo)
print("Welcome to Hangman")
chosen_word = random.choice(List_of_words.word_list)

display = []
for char in chosen_word:
    display.append("_")

lives = 6

end_of_game = False
while end_of_game == False:
    guess = input("Guess a Letter: ").lower()
    clear()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You Lose')
   
    print(f"{''.join(display)}")
  
    if "_" not in display:
        end_of_game = True
        print("You win")
    print(stages[lives])
