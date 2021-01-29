from time import sleep
import random
import hangman_words
import hangman_art

word_list = hangman_words.words
chosen_word = random.choice(word_list)
logo = hangman_art.logo_0
game_over = hangman_art.game_over_0
win = hangman_art.win_0

stages = hangman_art.stages_0

display = []
word_length = len(chosen_word)

# Intro
print(logo)
print("Welcome to hangman!\n")

# Clear function


# Show response or not
def show_answer():
    while True:
        show = input('Show answer? (yes/no)')
        if show == 'yes':
            print("The word is " + chosen_word + '.')
            break
        elif show == 'no':
            break
        else:
            print("That's not a valid answer!")

# Admin login
def admin_login():
    admin_user = True
    while admin_user:
        admin = input("To start a new game, enter n.\nFor admin access, enter the password.")
        if admin == 'password':
            show_answer()
            break
        elif admin == 'n':
            admin_user = False
        else:
            print("That's not a valid answer!")

admin_login()

# Making list of word length
for l in range(word_length):
    display += '_'

# Body of game

print("\nLOADING  ■■■■■■■■■■■□□□ ")
sleep(1)

end_of_game = False

while True:
    difficulty = input("Choose your difficulty (easy/medium/hard): ")
    if difficulty == 'easy':
        lives = 10
        break
    elif difficulty == 'medium':
        lives = 7
        break
    elif difficulty == 'hard':
        lives = 5
        break
    else:
        print("That's not a valid answer!")

print("\nLOADING  ■■■■■■■■■■■□□□ ")
sleep(1)
print(f"Alright! Your difficulty level is set to {difficulty}. You have {lives} lives.")


while not end_of_game:

    guess = input("\nGuess a letter: ")
    print("\n" * 100)

    if guess in display:
        print(stages[lives])
        print("You've already guessed " + guess + '!')
    else:
        if guess in chosen_word:
            print(stages[lives])
            print("Correct! " + guess + ' is in the word!')

    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    if guess not in chosen_word:
        print(guess + ' is not in in the word!')
        lives -= 1
        print(stages[lives])

    print(f"{' '.join(display)}")
    print("Lives left: " + str(lives) + '\n')

    if '_' not in display:
        print(win)
        print("Hooray! You win!")
        end_of_game = True
        sleep(10)
    elif lives == 0:
        print(game_over)
        print("The answer was " + chosen_word + ".")
        print("Better luck next time, loser!")
        end_of_game = True
        sleep(10)


