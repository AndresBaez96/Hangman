import random

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

def run():
    words = read()
    word = randomNumber(words)
    print(word)

if __name__ == '__main__':
    run()