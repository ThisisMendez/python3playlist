from random import shuffle

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram) #the seperator

words = ['beetroot', 'carrots', 'potatoes']
anagrams = []

# 1. 
# for word in words: 
#     anagrams.append(jumble(word))
# print(anagrams)

# 2. 
# print(list(map(jumble,words)))

print([jumble(word) for word in words])

# those are 3 different ways of doing it 
# Some people don't like using maps and would rather use loops 
# Easy way to convert one list into another
