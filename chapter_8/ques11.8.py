 from random import choice
word = input('Enter a word: ')
letter_list = list(word)
choice(letter_list)
anagram = ''.join(letter_list)
print(anagram)