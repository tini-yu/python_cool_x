player1, player2 = input('Ввод: ').split(' ')

pile1 = ['камень', 'ножницы', 'бумага']
pile2 = ['камень', 'ножницы', 'бумага', 'камень', 'ножницы', 'бумага']
p1_index = pile1.index(player1)
p2_index = pile2.index(player2)
# Поскольку мы не меняем индексы в списке, мы можем сравнить выборы игроков относительно них.
if pile1[p1_index] == pile1[p2_index]:
    print(p1_index, p2_index, "ничья")
elif pile1[p1_index] == pile2[p2_index + 1]:
    print("игрок 1 проиграл")
else:
    print("игрок 1 выиграл")
