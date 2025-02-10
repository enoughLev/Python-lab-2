text = "Helqlow"
lenght_slash = (len(text)+1)/2
leng = 2

piece_one = text[0:int(lenght_slash):1]
piece_two = text[int(lenght_slash)::]
print(piece_two + piece_one)