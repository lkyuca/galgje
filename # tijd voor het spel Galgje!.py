# Tijd voor het spel Galgje!
from datetime import date, datetime
import random
word_list = ["luca is de beste", "luca", "python", "programmeren", "appel", "banaan", "peer","jazz","score","etui","cactus","liquidatie","oase""junior","curry","acryl","quinoa","woorden","presentatie","de bomen zijn groen","appeltaart"]

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Laten we Galgje spelen!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Raad een letter of woord: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Je hebt dit al geprobeerd: ", guess, "!")
            elif guess not in word:
                print(guess, "is niet in het woord :(")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Goed zo,", guess, "is in het woord!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Je hebt dit al geprobeerd: ", guess, "!")
            elif guess != word:
                print(guess, " is niet het woord :(")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("ongeldige input")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Goed zo, je hebt het woord geraden!")
    else:
        print("Het spijt me, maar je hebt geen gokken meer. Het woord was " + word + ". Misschien heb je volgende keer meer geluk!")

nu = datetime.now ()
huidige_tijd = nu.strftime("%H:%M:%S")

with open("score.txt", "a") as f:
            f.write(str(date.today()) + " " + str(huidige_tijd) + "        Gefeliciteerd! U heeft het woord geraden!\n\n")

def display_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[tries]


def main():
    word = get_word(word_list)
    play(word)
    while input("Opnieuw? (J/N) ").upper() == "J":
        word = get_word(word_list)
        play(word)


if __name__ == "__main__":
    main()