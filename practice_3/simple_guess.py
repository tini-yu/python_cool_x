# input any N number
# Output: корень этого числа, если он целый
# если такого нет "трудно, не могу"
# def guesss(num: int) -> int:

n = int(input("N:"))

def guess(num: int)-> int | str:
    counter = 0
    for i in range(1, (num//2)+2): # обрезаем, потому что после половины, квадрат всегда будет больше n
        counter += 1
        if i*i == num:
            return i
    return "Трудно, не могу."

print(guess(n))
