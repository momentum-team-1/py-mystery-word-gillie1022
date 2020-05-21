import random
import string

file = open("words.txt")
text = file.read().split()
file.close()

easy_list = [
    word.upper()
    for word in text
    if 4 <= len(word) <= 6
]

normal_list = [
    word.upper()
    for word in text
    if 6 <= len(word) <= 8
]

hard_list = [
    word.upper()
    for word in text
    if 8 <= len(word)
]

def get_difficulty():
    difficulty = input("Please select a difficulty (e - Easy, n - Normal, h - Hard): ") 
    if difficulty == "e":
        word = random.choice(easy_list)
    elif difficulty == "n":
        word = random.choice(normal_list)
    elif difficulty == "h":
        word = random.choice(hard_list)
    else:
        return get_difficulty()
    return word

if __name__ == "__main__":
    word = (get_difficulty())
    print(f"The mystery word is {len(word)} characters long.")
    