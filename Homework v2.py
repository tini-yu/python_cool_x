top = int(input("Any number: "))
three_n = top//3
five_n = top//5
fifteen_n = top//15
three_sum = (6 + 3*(three_n - 1))/2*three_n  # Формула суммы арифм. прогрессии
five_sum = (10 + 5*(five_n - 1))/2*five_n
fifteen_sum = (30 + 15*(fifteen_n - 1))/2*fifteen_n

all_sum = five_sum + three_sum - fifteen_sum
print(all_sum)
