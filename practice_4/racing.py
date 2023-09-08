from import_this import RACE_DATA


def time_convert(placement) -> str:  # Переводим время в формат чч:мм:сс
    time: int = RACE_DATA[placement]['FinishedTimeSeconds']
    hours: int | str = time // 3600
    minutes: int = (time // 60) % 60
    seconds: int = time % 60 % 60
    if hours < 10:
        hours: str = f'0{hours}'
    if minutes < 10:
        minutes: str = f'0{minutes}'
    if seconds < 10:
        seconds: str = f'0{seconds}'
    return f'{hours}:{minutes}:{seconds}'


def order() -> list:  # Определяем ключи 3х победителей
    places: list = []
    for key in range(1, len(RACE_DATA)+1):
        place: int = RACE_DATA[key]['FinishedPlace']
        places.append(place)
    first: int = places.index(1)+1  # Индексы начинаются с 0, ключи дикт с 1
    second: int = places.index(2)+1
    third: int = places.index(3)+1
    return [first, second, third]


def output(placement) -> str:
    return f'''
Гонщик на {RACE_DATA[placement]['FinishedPlace']} месте:
\tИмя: {RACE_DATA[placement]['RacerName']}
\tКоманда: {RACE_DATA[placement]['RacerTeam']}
\tВремя: {time_convert(placement)}'''


if __name__ == '__main__':
    ordering: list = order()
    winner: str = RACE_DATA[ordering[0]]['RacerName']
    leng: int = len(winner)
    under_lines: str = '_'*24 + '_'*leng  # кол-во _ равно длине строки сверху
    print(f'''
Выиграл - {winner}! Поздравляем!
{under_lines}
Первые три места:''')
    for x in ordering:
        print(output(x))
