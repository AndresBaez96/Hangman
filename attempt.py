import random

class Attempt():
    lives = int

    def __init__(self) -> None:
        self.lives = 6

    def read(self):
        words = dict()
        with open('./File/data.txt','r',encoding='utf-8') as f:
            for number, word in enumerate(f, 1):
                words[number] = word.strip()
        return words

    def randomNumber(self, dict: dict):
        n = random.randint(1, len(dict))
        word = dict.get(n)
        return word

    def replaceChars(self, word: str):
        nword = word.maketrans('áéíóú', 'aeiou')
        newWord = word.translate(nword)
        return newWord

    def mysteryWord(self,word: str):
        dashWord = ['-' for i in range(len(word))]
        newWord = ''.join(dashWord)
        return newWord, dashWord

    def replaceChar(self, char: str, word: str, dashWord: list):
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

    def userLives(self, live: int, chance: int):
        live -= chance
        return live
        
        
        