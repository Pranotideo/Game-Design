#!/usr/bin/env python

def get_random_word():
    import random
    word_dict = ["dear", "near", "neat", "feat"]
    return word_dict[random.randint(0, len(word_dict)-1)]

def play_game(random_word):
    """implementation to be done here"""
    # take input here
    # use a do-while like condition to resume the game
    user_guess = raw_input ("Enter your guess: ")
    if len(user_guess) != 4:
        print "You must enter a word that is 4 letters long"
    game_counter = 1
    while game_counter <= 10 and len(user_guess) == 4:
        if len(user_guess) != 4:
            print "Error. Please enter only 4 lettered words"

        if random_word == user_guess:
            print("correct")
            break
        elif game_counter == 10:
            print "Random word: %s" % random_word
            print "User's guess: %s" % user_guess
            break
        else:
            good_match = 0
            bad_match = 0
            for i in range(len(random_word)):
                if random_word[i] == user_guess[i]:
                    good_match += 1
                elif random_word[i] in user_guess:
                    bad_match += 1
            print("Good Match: %s" % good_match)
            print("Bad Match: %s" % bad_match)
        user_guess = raw_input ("Improve your guess: ")
        if len(user_guess) != 4:
            print "You must enter a word that is 4 letters long"
            continue
        game_counter += 1

if __name__ == "__main__":
    word = get_random_word()
    play_game(word)
