#
# ps8pr2.py  (Problem Set 8, Problem 2)
#
# Markov text generation     
#

import random

# function 1
def create_dictionary(filename):
    """ takes a string representing the name of a text file, and that returns 
    a dictionary of key-value pairs in which: each key is a word encountered 
    in the text file, and the corresponding value is a list of words that 
    follow the key word in the text file. 
    """
    file = open(filename, 'r')
    text = file.read()
    file.close()  
    words = text.split()
    d = {}
    currentword = '$'
    for nextword in words:
        if currentword not in d:
            d[currentword] = [nextword]
        else:
            d[currentword] += [nextword]
        if nextword[-1] == '.' or nextword[-1] == '!' or nextword[-1] == '?':
            currentword = '$'
        else:
            currentword = nextword
    return d

# function 2
def generate_text(word_dict, num_words):
    """ must use word_dict to generate and print num_words words, with a space
    after each word. The function must print the words that it generates. 
    It must not return a value. 
    """
    currentword = '$'
    for i in range(num_words):
        wordlist = word_dict[currentword]
        nextword = random.choice(wordlist)
        print(nextword, end=' ')
        if nextword[-1] == '.' or nextword[-1] == '!' or nextword[-1] == '?':
            currentword = '$'
        else:
            currentword = nextword
        
