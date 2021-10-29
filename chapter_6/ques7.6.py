x = input('enter word to check if it is a palindrome:')

w = ""
for i in x:
    w = i + w

if (x == w):
    print("Yes, word is  palindrome")
else:
    print("No, the word is not a palindrome")
