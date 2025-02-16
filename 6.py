slow_word = input()

if slow_word != '':
    length = len(slow_word)
    i = 0
    while length > 0:
        print(slow_word[i]*(i+1), end='')
        i+=1
        length-=1