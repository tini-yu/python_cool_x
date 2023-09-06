top = int(input('Введите число: '))
three_del = []
five_del = []
for x in range(1, top+1):
    if (x%3)==0:
        three_del.append(x)
    if (x%5)==0:
        five_del.append(x)

for i in three_del:
    for j in five_del:
        if i==j:
            three_del.remove(i) #Удаляем те что делятся на 5 из списка делящихся на 3
print(three_del)
print(five_del)

threes = 0
fives = 0
for k in three_del:
    threes += k
for l in five_del:
    fives += l
print("Сумма чисел кратных 3 (но не пяти): ", threes, "\nСумма чисел кратных 5 (и иногда 3): ",
      fives, "\nОбщая сумма: ", threes+fives)

