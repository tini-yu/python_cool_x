def convert_ab_to_int(a: str, b: str) -> (int, int):
    a, b = int(a), int(b)
    return a, b

def divide (a: int | float, b: int | float):
    if 3 in [a, b]:
        raise AttributeError('Я НЕНАВИЖУ ТРОЙКИ')
    return a/b

while True:
    a, b = input('Введите 2 числа для их суммы: ').split()
    division_score = None
    try:
        a, b = convert_ab_to_int(a, b)
        division_score = divide(a, b)
    # except Exception as e: # Ловит все ошибки
    except (ZeroDivisionError, ValueError) as e:
        print(f'Ошибка {e}', 'Давай без нулей и только цифры')
        continue
    except AttributeError as ex:
        print(f'разраб злой, потому что он цитата "{ex}"')
        continue
    # except ZeroDivisionError as e:
    #     print(f'Ошибка {e}', 'Давай без нулей')
    #     continue
    finally:
        print('Мы в финале') # Всегда выполняется после try либо except даже если там break
    ab_sum = a + b
    print(f"{a} + {b} = {ab_sum}")
    print(f"{a} / {b} = {division_score}")
    print()