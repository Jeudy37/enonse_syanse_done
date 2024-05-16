tablo=[1,2,3,4,5,6,7,8,9]

tablo2 =[x for x, i in enumerate(tablo) if i % 3==0]
print(tablo2)