tablo = [1, 2, 3, 5]
tablo2 = [2, 4, 5, 7]
t=[]
for el in tablo:
    if el in tablo2:
        t.append(el)

print(t)