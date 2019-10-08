#!/usr/bin/env python

def get_random_word():
    import random
    word_dict = ["dear", "near", "neat", "feat"]
    return word_dict[random.randint(0, len(word_dict)-1)]

def get_user_input():
    w = raw_input ("Enter your guess: ")
    if len(w) != 4:
        print "You must enter a word that is 4 letters long"
        import sys
        sys.exit()
    return w

def match_words(w1, w2):
    """implementation to be done here"""
    print "Random word: %s" % w1
    print "User's guess: %s" % w2
    G = 0
    B = 0
    if w1 == w2:
        print("correct")
    else:
        for i in range(len(word)):

            if w1[i] == w2[i]:
                G += 1

            elif w1[i] in w2:
                B += 1



        print("Good Match: %s" % G)
        print("Bad Match: %s" % B)

if __name__ == "__main__":
    word = get_random_word()
    user = get_user_input()
    match_words(word, user)
