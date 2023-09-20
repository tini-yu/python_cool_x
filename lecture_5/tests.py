a: list[int] = [1, 2, 3, 3, 5]
b: list[int] = [0, 0, 1, 0, 1]
# answer = [0, 0, 3, 0, 5]

def mask_list(array: list[int], mask: list[int]) -> list[int]:
    return [val * mask[i] for i, val in enumerate(array)]

def test_mask_list():
    print('Testing...')
    assert mask_list([1, 2, 3], [0, 1, 0]) == [0, 2, 0], 'mask is not working correctly'

answer = mask_list(array=a, mask=b)

print(test_mask_list(), answer)


# answer = [
#     val * b[i]
#     for i, val in enumerate(a)
# ]







# answer = [i*2 for i in a] # v.1
# for i in a: # v.2
#     answer.append(i)

# for i, val in enumerate(a):
#     print(f'index = {i}, value = {val}')
# print(list(enumerate(a)))