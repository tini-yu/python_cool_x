n: int = int(input("N: "))
# while n > 0:
#     print(n)
#     n -= 1

array: list = list(range(1, n))
x = 0
while True:
    if array[x] % 13 == 0:
        print(array[x], 'deletsa')
        break
    x += 1


