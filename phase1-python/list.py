spam = ['apples', 'bananas', 'oranges', 'cats']
name = ''
for i in range(len(spam)):
    if(i == (len(spam)-1)):
        name += ' and ' + spam[i]
    elif(i==0):
        name += spam[i]
    else:
        name += ', ' + spam[i]
print(name)