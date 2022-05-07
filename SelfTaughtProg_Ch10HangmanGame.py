# 'Self-taught Programmer Ch 10 Hangman Game
import random

def hangman(word):
    wrong = 0
    stages = ["",
              " _______        ",
              "|       |       ",
              "|       O       ",
              "|      /|\      ",
              "|      / \      ",
              "|               "]
    rletters = list(word)
    board = ["_"]*len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages)-1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char) #character index
            board[cind] = char
            rletters[cind] = '$' #each repeated letter treated independently
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e])) #print the slice of stages
        if "_" not in board:
            print("You win! It was {}.".format(word))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}.".format(word))

wordList = ["cat","dog","mouse","rat","hen"]
word = wordList[random.randint(0,len(wordList)-1)]
hangman(word)
        
        
