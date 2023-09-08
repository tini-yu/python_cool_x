from module import greet # Соседний файл

x = 14

def outer(y):
    print(f'y in outer before assig: {"y" in locals()}')
    y = 12
    f'y in outer exists {"y" in locals()}'
    def answer(x):
        asds = x+ y+ 133
        x = 12
        print(f'y in answer exists {"y" in locals()}')
        return x
    return answer(x)

# print(
#     greet("vova")  # imported function
# )

if __name__ == '__main__':
    x = 42
    print(
        outer(12),
        f'y in outer after ass exists {"y" in locals()}',
        f'\ny in main exists {"y" in locals()}'
    )