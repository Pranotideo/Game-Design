def match():
    if w[0] != nlis[0] and w[1] != nlis[1] and w[2] != nlis[2] and w[3] != nlis[3]:
        if w[0] != nlis[0] and w[1] != nlis[1] and w[2] != nlis[2] and w[3] != nlis[3]:
            q = list(input("improve your guess: "))
        elif q[0] == nlis[0] and q[1] != nlis[1] and q[2] != nlis[2] and q[3] != nlis[3]:
            print("1 GoodMatch and 3 BadMatch")
        elif q[0] != nlis[0] and q[1] == nlis[1] and q[2] != nlis[2] and q[3] != nlis[3]:
            print("1 GoodMatch and 3 BadMatch")
        elif q[0] != nlis[0] and q[1] != nlis[1] and q[2] == nlis[2] and q[3] != nlis[3]:
            print("1 GoodMatch and 3 BadMatch")
        elif q[0] == nlis[0] and q[1] != nlis[1] and q[2] != nlis[2] and q[3] == nlis[3]:
            print("1 GoodMatch and 3 BadMatch")

        elif q[0] == nlis[0] and q[1] == nlis[1] and q[2] != nlis[2] and q[3] != nlis[3]:
            print("2 GoodMatch and 2 BadMatch")
        elif q[0] != nlis[0] and q[1] == nlis[1] and q[2] == nlis[2] and q[3] != nlis[3]:
            print("2 GoodMatch and 2 BadMatch")
        elif q[0] != nlis[0] and q[1] == nlis[1] and q[2] != nlis[2] and q[3] == nlis[3]:
            print("2 GoodMatch and 2 BadMatch")
        elif q[0] != nlis[0] and q[1] != nlis[1] and q[2] == nlis[2] and q[3] == nlis[3]:
            print("2 GoodMatch and 2 BadMatch")
        elif q[0] == nlis[0] and q[1] != nlis[1] and q[2] == nlis[2] and q[3] != nlis[3]:
            print("2 GoodMatch and 2 BadMatch")
        elif q[0] == nlis[0] and q[1] != nlis[1] and q[2] != nlis[2] and q[3] == nlis[3]:
            print("2 GoodMatch and 2 BadMatch")

        elif q[0] != nlis[0] and q[1] == nlis[1] and q[2] == nlis[2] and q[3] == nlis[3]:
            print("3 GoodMatch and 1 BadMatch")
        elif q[0] == nlis[0] and q[1] != nlis[1] and q[2] == nlis[2] and q[3] == nlis[3]:
            print("3 GoodMatch and 1 BadMatch")
        elif q[0] == nlis[0] and q[1] == nlis[1] and q[2] != nlis[2] and q[3] == nlis[3]:
            print("3 GoodMatch and 1 BadMatch")
        elif q[0] == nlis[0] and q[1] == nlis[1] and q[2] == nlis[2] and q[3] != nlis[3]:
            print("3 GoodMatch and 1 BadMatch")

        elif q[0] == nlis[0] and q[1] == nlis[1] and q[2] == nlis[2] and q[3] == nlis[3]:
            print("4 GoodMatch and 0 BadMatch")

    elif w[0] == nlis[0] and w[1] != nlis[1] and w[2] != nlis[2] and w[3] != nlis[3]:
        print("1 GoodMatch and 3 BadMatch")
    elif w[0] != nlis[0] and w[1] == nlis[1] and w[2] != nlis[2] and w[3] != nlis[3]:
        print("1 GoodMatch and 3 BadMatch")
    elif w[0] != nlis[0] and w[1] != nlis[1] and w[2] == nlis[2] and w[3] != nlis[3]:
        print("1 GoodMatch and 3 BadMatch")
    elif w[0] == nlis[0] and w[1] != nlis[1] and w[2] != nlis[2] and w[3] == nlis[3]:
        print("1 GoodMatch and 3 BadMatch")

    elif w[0] == nlis[0] and w[1] == nlis[1] and w[2] != nlis[2] and w[3] != nlis[3]:
        print("2 GoodMatch and 2 BadMatch")
    elif w[0] != nlis[0] and w[1] == nlis[1] and w[2] == nlis[2] and w[3] != nlis[3]:
        print("2 GoodMatch and 2 BadMatch")
    elif w[0] != nlis[0] and w[1] == nlis[1] and w[2] != nlis[2] and w[3] == nlis[3]:
        print("2 GoodMatch and 2 BadMatch")
    elif w[0] != nlis[0] and w[1] != nlis[1] and w[2] == nlis[2] and w[3] == nlis[3]:
        print("2 GoodMatch and 2 BadMatch")
    elif w[0] == nlis[0] and w[1] != nlis[1] and w[2] == nlis[2] and w[3] != nlis[3]:
        print("2 GoodMatch and 2 BadMatch")
    elif w[0] == nlis[0] and w[1] != nlis[1] and w[2] != nlis[2] and w[3] == nlis[3]:
        print("2 GoodMatch and 2 BadMatch")

    elif w[0] != nlis[0] and w[1] == nlis[1] and w[2] == nlis[2] and w[3] == nlis[3]:
        print("3 GoodMatch and 1 BadMatch")
    elif w[0] == nlis[0] and w[1] != nlis[1] and w[2] == nlis[2] and w[3] == nlis[3]:
        print("3 GoodMatch and 1 BadMatch")
    elif w[0] == nlis[0] and w[1] == nlis[1] and w[2] != nlis[2] and w[3] == nlis[3]:
        print("3 GoodMatch and 1 BadMatch")
    elif w[0] == nlis[0] and w[1] == nlis[1] and w[2] == nlis[2] and w[3] != nlis[3]:
        print("3 GoodMatch and 1 BadMatch")

    elif w[0] == nlis[0] and w[1] == nlis[1] and w[2] == nlis[2] and w[3] == nlis[3]:
        print("4 GoodMatch and 0 BadMatch")

flist = ["near", "dear", "tear", "gate", "pull", "push", "math", "next"]
w = list(input("Enter your guess: "))
if len(w) > 4 or len(w) < 4:
    print("Enter 4 letters only")
else:
    fstring = ','.join(flist)
    substring = fstring.split(",")
    print(substring)
    for i in range(len(substring)):
        spl = substring[i].split(",")
        print(spl)
        for j in range(len(spl)):
            nlis = []
            nlis[:0] = spl[j]
            print(nlis)
    match()



            #print(w[0] == nlis[0])
            #print(w[1] == nlis[1])
            #print(w[2] == nlis[2])
            #print(w[3] == nlis[3])
