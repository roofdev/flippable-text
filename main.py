import json
allowed_letters = ['b','p','d','q','o','i','l','m','u','s','w','n','z']
allowed_words = []

with open('words_dictionary.json') as word_file:
    wordlist = json.load(word_file)
    for word in wordlist:
        word_notallowed = 0
        for letter in word:
            if letter not in allowed_letters:
                word_notallowed = word_notallowed + 1
        if word_notallowed == 0:
            allowed_words.append(word)
out_file = open("allowedwords.json", "w") 
json.dump(allowed_words, out_file, indent = 6) 
out_file.close() 
def flip(flipw):
    flipped = ""
    for i in flipw:
        if i in allowed_letters:
            if i=='b':
                flipped = flipped + "q"
            if i=='d':
                flipped = flipped + "p"
            if i=='p':
                flipped = flipped + "b"
            if i=='q':
                flipped = flipped + "d"
            if i=='m':
                flipped = flipped + "w"
            if i=='w':
                flipped = flipped + "m"
            if i=='u':
                flipped = flipped + "n"
            if i=='n':
                flipped = flipped + "u"
            if i=='s':
                flipped = flipped + "s"
            if i=='z':
                flipped = flipped + "s"
            if i=='o':
                flipped = flipped + "o"
            if i=='i':
                flipped = flipped + "!"
            if i=='l':
                flipped = flipped + "l"
    return flipped[::-1]
def mirror(flipw):
    flipped = ""
    for i in flipw:
        if i in allowed_letters:
            if i=='b':
                flipped = flipped + "p"
            if i=='d':
                flipped = flipped + "q"
            if i=='p':
                flipped = flipped + "b"
            if i=='q':
                flipped = flipped + "d"
            if i=='m':
                flipped = flipped + "w"
            if i=='w':
                flipped = flipped + "m"
            if i=='u':
                flipped = flipped + "n"
            if i=='n':
                flipped = flipped + "u"
            if i=='s':
                flipped = flipped + "z"
            if i=='z':
                flipped = flipped + "s"
            if i=='s':
                flipped = flipped + "o"
            if i=='i':
                flipped = flipped + "!"
            if i=='l':
                flipped = flipped + "l"
    return flipped[::-1]