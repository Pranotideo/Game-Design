q = ["near", "dear", "tear", "gate", "pull", "push", "math", "next"]
w = str(input("Enter your guess: "))
p = len(w)
if p > 4 or p < 4:
    print("Enter 4 letters only")
else:
    for i in range(len(q)):
        print(q[i]==w)
