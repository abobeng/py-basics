count = 0
article = (['a','an','and'])
sentence = input('enter some text:')

for i in sentence:
    if article == sentence:
        count = count +1
print (count)