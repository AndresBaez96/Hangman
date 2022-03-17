import random
import os

def read():
    words = dict()
    with open('./File/data.txt','r',encoding='utf-8') as f:
        for number, word in enumerate(f, 1):
            words[number] = word.strip()
    return words

def randomNumber(dict: dict):
    n = random.randint(1, len(dict))
    word = dict.get(n)
    return word

def replaceChars(word: str):
    nword = word.maketrans('áéíóú', 'aeiou')
    newWord = word.translate(nword)
    return newWord

def mysteryWord(word: str):
    dashWord = ['-' for i in range(len(word))]
    newWord = ''.join(dashWord)
    return newWord, dashWord

def replaceChar(char: str, word: str, dashWord: list):
    start = 0
    for i in word:
        if i == char:
            index = word.index(char, start)
            start = index + 1
            dashWord[index] = char
    dashWord = ''.join(dashWord)
    if word.find(char) == -1: life = 1
    else: life = 0
    return dashWord, life

def lives(live: int, chance: int):
    live -= chance
    return live

def run():
    words = read()
    word = randomNumber(words)
    word = replaceChars(word)
    word2Find, list_word = mysteryWord(word)
    live = 5
    
    while True:
        os.system('clear')
        print(word2Find)
        if live == 0:
            print('You lose, the word was {}'.format(word))
            break
        elif word == word2Find:
            print('You won')
            break
        else:
            print('{} lives left'.format(live))
        char = input('Enter a letter: ')
        char = char.lower()
        word2Find, chance = replaceChar(char, word, list_word)
        live = lives(live, chance)
        
        
   
if __name__ == '__main__':
    run()