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
    G = 0
    B = 0

    if w1 == w2:
        print("correct")
    else:
        for i in range(len(w1)):
            if w1[i] == w2[i]:
                G += 1
            elif w1[i] in w2:
                B += 1
            elif G == 0 and B == 0:
                print("Good Match: %s" % G)
                print("Bad Match: %s" % B)
                w2 = raw_input ("Improve your guess: ")

    print("Good Match: %s" % G)
    print("Bad Match: %s" % B)



if __name__ == "__main__":
    for j in range(10):
        word = get_random_word()
        user = get_user_input()
        match_words(word, user)
