"""
число n float
y = (n**3)/9
потолок от y (округление, до большего)
вывести: ты очень*y крут
"""

n = float(input("Ведите число: "))
y = (n**3)/9
print(y)
if round(y) < y:
    y = y+1
y = int(y)
print(y)
print('Ты ' + 'очень '*y + 'крут')
