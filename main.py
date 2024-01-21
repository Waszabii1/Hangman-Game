from random_word import RandomWords

def get_word():
    r = RandomWords()
    word = r.get_random_word()
    return word.upper()


def play(word):
    word_completion ="_" *len(word)
    guessed= False
    guessed_letters= []
    gussed_words = []
    tries= 6
    print(" Lets play Hangman")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries >0:
        print(f"Letters gussed: {guessed_letters}")
        print(f"Amount of tries left: {tries}")
        guess = input("Please guess a letter  or word. (Type Stop to end) ").upper()
        if guess == "STOP":
            break
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}")
            elif guess not in word:
                print(f"{guess} is not in the word .")
                tries -=1
                guessed_letters.append(guess)
            else:
                print(f"Good job , {guess}, is in the word" )
                guessed_letters.append(guess)
                word_as_list =list(word_completion)
                indices =[i for i, letter in enumerate(word) if letter== guess]
                for index in indices:
                    word_as_list[index]=guess
                word_completion ="".join(word_as_list)
                if "_" not in word_completion:
                    guessed=True

        elif len(guess) ==len(word) and guess.isalpha():
            if guess in gussed_words:
                print(f" You have already guessed the word {guess}.")
            elif guess !=word:
                print(f"{guess}, is not the word.")
                tries-=1
                gussed_words.append(guess)
            else:
                guessed =True
                word_completion = word    
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")  
    if guessed:
        print("CONGRATS you guess the word correctly.")  
    else:
        print(f"SORRY you ran out of tries. The word was {word}")

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
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
        word=get_word()
        play(word)
        while input("Play again? (Y/N) ").upper()=="Y":
            wrod= get_word()
            play(word)

if __name__ == "__main__":
    main()                






   

  

          

# pygame.quit()            
