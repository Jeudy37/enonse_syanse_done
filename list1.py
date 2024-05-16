tablo=[1,2,3,4,5,6,7,8,9]
tablo2=[]
for t,i in enumerate(tablo):
    if t % 2 == 0:
        tablo2.append(t)

print(tablo2)