text = "bad h boy in the darkh"
lenght = len(text)
mass = list()
count = 1

for var in text:
    if var == 'h':
        mass.append(count)
    count = count + 1

print(text[min(mass):max(mass)])
