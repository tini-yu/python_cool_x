time: int = int(input('Seconds: '))
hours: int | str = time // 3600
minutes: int = (time // 60) % 60
print(f'{hours} час(а/ов) и {minutes} минут(а/ы)')