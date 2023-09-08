from typing import TypeAlias, Any

# В словарях есть ключи и привязанные к ним переменные
# Можно хранить в значения что угодно
# Ключи нельзя list
# True = 1  - true будет конвертироваться в 1, а false в 0

intorNonetype: TypeAlias = int | None

alphabet: dict[intorNonetype | str | float, str|list|int|dict[int, str| int | dict[int, int ]]] = {  # до запятой - возможные ключи, после - возможные значения
    1: 'A',
    2: [1, 3],
    5: {
        1: 'A',
        2: 4,
        3: {
            1: 5
        }
    },
    3: 'C',
    4: 'X',
    'Z': 10,
}

print(alphabet['Z'])
# class A:
#     def __init__(self, **kwargs):
#         for key, value in kwargs:
#             self.key = value
#
# for_class_a = dict[str, Any] = {
#     'A': 1,
#     "B": 235
# }


#print(alphabet[5]) # Gives error - no such keys

# for pair in alphabet:  # Gives only the keys
#     print(pair)

# for pair in alphabet.items():  # Gives картежи с ключами и значениями
#     print(pair)

# for key, value in alphabet.items():  # Питон сам распаковывает картежи
#     print(key, value)

# print(alphabet.get('Z', None))  # if 'Z' exist print it, otherwise print None
# # Ищет по ключам

# print(alphabet.get(5).get(3).get(1))  # Значения из вложенного 3 раза dict