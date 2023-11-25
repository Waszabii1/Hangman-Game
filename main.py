# import random
# from word import word_list

# def get_word():
#     word=random.choice(word_list)
#     print(word)
#     return word.upper()


# def play(word):
#     word_completion ="_" *len(word)
#     guessed= False
#     guessed_letters= []
#     gussed_words = []
#     tries= 6
#     print(" Lets play Hangman")
#     print(display_hangman(tries))
#     print(word_completion)
#     print("\n")
#     while not guessed and tries >0:
#         guess =input("Please guess a letter  or word :").upper()
#         if len(guess) == 1 and guess.isalpha():
#             if guess in guessed_letters:
#                 print("You already guessed the letter",guess)
#             elif guess not in word:
#                 print(guess , "is not in the word .")
#                 tries -=1
#                 guessed_letters.append(guess)
#             else:
#                 print("Good job ",guess," is in the word" )
#                 guessed_letters.append(guess)
#                 word_as_list =list(word_completion)
#                 indices =[i for i, letter in enumerate(word) if letter== guess]
#                 for index in indices:
#                     word_as_list[index]=guess
#                 word_completion ="".join(word_as_list)
#                 if "_" not in word_completion:
#                     guessed=True

#         elif len(guess) ==len(word) and guess.isalpha():
#             if guess in gussed_words:
#                 print(" You have already guessed the word.",guess)
#             elif guess !=word:
#                 print(guess ," is not the word.")
#                 tries-=1
#                 gussed_words.append(guess)
#             else:
#                 guessed =True
#                 word_completion = word    
#         else:
#             print("Not a valid guess.")
#         print(display_hangman(tries))
#         print(word_completion)
#         print("\n")  
#     if guessed:
#         print("CONGRATS you guess the word correctly.")  
#     else:
#         print("SORRY you ran out of tries. The word was "+word)

# def display_hangman(tries):
#     stages = [  # final state: head, torso, both arms, and both legs
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |     \\|/
#                    |      |
#                    |     / \\
#                    -
#                 """,
#                 # head, torso, both arms, and one leg
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |     \\|/
#                    |      |
#                    |     / 
#                    -
#                 """,
#                 # head, torso, and both arms
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |     \\|/
#                    |      |
#                    |      
#                    -
#                 """,
#                 # head, torso, and one arm
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |     \\|
#                    |      |
#                    |     
#                    -
#                 """,
#                 # head and torso
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |      |
#                    |      |
#                    |     
#                    -
#                 """,
#                 # head
#                 """
#                    --------
#                    |      |
#                    |      O
#                    |    
#                    |      
#                    |     
#                    -
#                 """,
#                 # initial empty state
#                 """  
#                    --------
#                    |      |
#                    |      
#                    |    
#                    |      
#                    |     
#                    -
#                 """
#     ]
#     return stages[tries]

# def main():
#         word=get_word()
#         play(word)
#         while input("Play again ?").upper()=="Y":
#             wrod= get_word()
#             play(word)

# if __name__ == "__main__":
#     main()                


# game

import pygame
import math

# pygame.init()

clock = pygame.time.Clock()
FPS =60

SCREEN_WIDTH = 1200 
SCREEN_HEIGHT = 600


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("My frame")

bg= pygame.image.load("flappy.jpg").convert()
bg_width= bg.get_width()
bg_rect =bg.get_rect()
scroll =0 
tiles = math.ceil(SCREEN_WIDTH/bg_width) + 1

print(tiles)
run = True
while run:
    clock.tick(FPS)

    for i in range(0,tiles):
     screen.blit(bg,( i * bg_width + scroll,0))
     bg_rect.x = i* bg_width  +  scroll
    #  pygame.draw.rect(screen,(255,0,0),bg_rect,1)


    #  scrool background
    scroll-=5 
    if abs(scroll) > bg_width:
       scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()         
    # reset scrool
   

  

          

pygame.quit()            