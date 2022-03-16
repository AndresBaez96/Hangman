import random
import os

def read():
    words = dict()
    with open('./File/data.txt','r',encoding='utf-8') as f:
        for number, word in enumerate(f, 1):
            words[number] = word.strip()
    return words

def randomNumber(dict : dict):
    n = random.randint(1, len(dict))
    word = dict.get(n)
    return word

def mysteryWord(word : str):
    dashWord = ['-' for i in range(len(word))]
    newWord = ''.join(dashWord)
    return newWord, dashWord

def replaceChar(char : str, word : str, dashWord : list):
    for i in word:
        if i == char:
            index = word.index(char)
            dashWord[index] = char
    dashWord = ''.join(dashWord)
    return dashWord

def run():
    words = read()
    word = randomNumber(words)
    word2Find, list_word = mysteryWord(word)
    
    while True:
        os.system('clear')
        print(word, word2Find)
        char = input('Enter a letter: ')
        char = char.lower()
        word2Find = replaceChar(char, word, list_word)

        
        
    
    
    
if __name__ == '__main__':
    run()