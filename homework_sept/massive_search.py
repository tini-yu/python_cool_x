massive = [-15, -1, 0, 1, 2, 3, 45, 67, 69, 70, 71, 73, 76, 100]
# massive = [0]
# massive = [-10, 100000]

nums = []
for frst in massive[:-1]:  # Нет смысла проверять последний элемент списка
    scnd = massive[massive.index(frst) + 1]
    if scnd-frst >= 2:
        nums.append(massive.index(scnd))

if not nums:
    print('Не найдено')
elif len(nums) == 1:
    print(f'Only number: {massive[nums[0]]}')
else:
    print(f"Indexes: {nums}")
