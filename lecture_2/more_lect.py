# numbers: list = [
#     1, 2, 3, 4, 5, 6, 7, 8, 9, 15
# ]
#
# for n in numbers:
#     if n % 3 == 0:
#         print(f'Число - {n} кратно 3')
#     if n % 3 != 0:
#         print(f'Число - {n} не кратно 3')
# for n in numbers:
#     if n % 3 ==0 and n % 5 == 0:
#         print(f'Число - {n} кратно 3 и 5')
#     elif n % 3 ==0:
#         print(f'Число - {n} кратно 3')
#     elif n % 5 == 0:
#         print(f'Число - {n} кратно 5')
#     else:
#         print(f'Число - {n} не делится ни на 3 ни на 5')

# word = input('Введите слово: ')
# vowel: str = "aeiouy"
#
# vowel_count: int = 0
# for char in word:
#     if char in vowel:
#         vowel_count += 1
# print(vowel_count)

n: int = int(input("N: "))

# sum_3_5 = 0
# sum_3 = 0
# sum_5 = 0
#
# for i in range(1, n+1):
#     if i % 3 == 0 and i % 5 == 0:
#        sum_3_5 += i
#     elif i % 3 ==0:
#         sum_3 += i
#     elif i % 5 == 0:
#         sum_5 += i
# print(sum_3_5, sum_3, sum_5)

sum_all = 0
for x in range (n+1):
    if x % 3 == 0 or x % 5 == 0:
        sum_all += x
print(sum_all)
