# snake_case = 0
#camelCase = 0
#OtherCase = 0
# _hed = 0 starts with _ = probably should be used
b: bool = True
c: float = 0.0
g: int = 0
n: None = None
a: list = [1, 2, 4, None, False, 'ded', c, g]
#print(a[1:7])
#print(a[4:])
#print(a[0:5:2])
a2 = [b, n, a]
_set: set = {c, g, b, n}
#print(_set) # set избавляется от дубликатов
#print(a)
# Порядковый номер элементов в сете постоянно меняется сам по себе
_set2 = {'a', 'l', 'r'}
_set3 = {'a', "g", "k"}
print(_set3.intersection(_set2))

mississipi = list("mississipi")
print(mississipi)

_matrix = [
    [1,2,3],
    [2, 3, 4],
    [3, 4, 5]
]
print(_matrix[2][2]) # Вытащить элемент из списка в списке

