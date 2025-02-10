text = "0xf1232f0"

first_f = text.find('f')
last_f = text.rfind('f')

if first_f != -1:
    if first_f == last_f:
        print(first_f)
    else:
        print(first_f, last_f)