# def my_personal_sum(  #объявляем функцию
#         x: int | float,
#         y: int | float,
# ) -> int| float: # функция вернет int or float
#     answer = x + y
#     return answer

def my_personal_sum(
        num_list: list
) -> int | float:
    answer =0
    for num in num_list:
        answer += num
    return answer

print(my_personal_sum([3, 4, 5]))

# def my_personal_sum(*args, **kwargs) -> int | float:   # * - распаковывает (работает и со списками)
#     print(f"Args: {args}", f"Kwargs: {kwargs}")
#
# print(my_personal_sum(3, 4, 5))