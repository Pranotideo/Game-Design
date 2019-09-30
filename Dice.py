import sys
import random

def Player():
    if N > 6:
        print("Players should be less than 6")
    elif N < 2:
        print("Players should be greater than 2")
    else:
        list = []
        for i in range(N):
            s = str(input("Enter Name: "))
            list.append(s)
        list.sort()
        print(list)

        for i in range(N):
            print("It's your turn: "+list[i])
            Opt = input("Roll Exit Pass ")
            list2 = []
            if Opt == "Exit":
                print("Ok")
            elif Opt == "Pass":
                print(Score)
            elif Opt == "Roll":
                Score = random.randrange(1,7)
                if Score == 6:
                    Score1 = random.randrange(1,7)
                    Score = Score1+Score
                    if Score1 == 6:
                        Score2 = random.randrange(1,7)
                        Score = Score2+Score
                        if Score2 == 6:
                            Score = 0
                print(list[i],Score)
                list2.append(Score)
    dict1 = dict.fromkeys(list[i],list2[i])
    print(dict1)



N = int(input("Enter Number of players: "))

Player()
#M = str(input("Enter their Names: "))
