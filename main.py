import os
from interface import Interface
from user import User
from attempt import Attempt

def play():
    #Player
    name = input('Write your name: ')
    name = str(name)
    user = User(name)

    #Game
    game = Attempt()
    words = game.read()
    word = game.randomNumber(words)
    word = game.replaceChars(word)
    word2Find, list_word = game.mysteryWord(word)
    live = getattr(game, 'lives')

    #Interface
    interface = Interface()
    
    while True:
        os.system('clear')
        print('{} is playing'.format(getattr(user, 'name')))
        print(word2Find)
        interface.hangman(live)

        if live == 0:
            print('{}, the word was {}'.format(getattr(user, 'name') ,word))
            break
        elif word == word2Find:
            print('{} won!'.format(getattr(user, 'name')))
            break
        else:
            print('{} lives left'.format(live))
        char = input('Enter a letter: ')
        char = char.lower()
        word2Find, chance = game.replaceChar(char, word, list_word)
        live = game.userLives(live,chance)
         
if __name__ == '__main__':
    play()