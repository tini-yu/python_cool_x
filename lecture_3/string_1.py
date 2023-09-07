import string

# pip install *

#local


# new_name: str = input('type name: ')
#
# greeting = 'hello bob!! aboba'
#
# # greeting: str = (
# #     greeting[:-3] + new_name
# # )
# greeting: str = \
#     (greeting.replace(" bob!", f' {new_name} '))
# print(greeting)

# river: str = "mmmmmississippi" # опечатка
# print(
#     "m" + river.lstrip('msi') # удаляет все символы, которые он встречает до тех пор пока не увидит не указанный символ
# )

# words = '<!---hello this comment---!>'
#
# print(
#     words.strip("<!>-").split()
# )
#
#
# numbers: str = string.digits
# wordel: str = "hello234 b45ob how444 are y85749ou?"
# _wordel: str = ""
#
# for ch in wordel:
#     if ch in numbers:
#         continue
#     else:
#         _wordel += ch
#
# wordel = _wordel
# del _wordel
#
#
# # for number in numbers:
# #     wordel = wordel.replace(number, "") # итерируемся во цифрам
#
# print(
#     wordel
# )
#
# _set: set = set([]) # empty set
# _dict: dics = {} # empty dictionary

words: str = "HEllo Bob, are you a bob? BOB!"
# words = words.lower().replace('bob')


while True:
    bob_index = words.lower().find("bob")
    if bob_index == -1:
        break
    else:
        words = (
            words[:bob_index] + 'Greg' + words[bob_index+len("bob"):]
        )
print(words)



