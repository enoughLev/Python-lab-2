first = input()
new = input()

if (first[-1] == new[0]):
    while True:
        in_t = input()
        if (in_t[0] == new[-1]):
            new = in_t
        else:
            print(in_t)
            break
else:
    print(new)
