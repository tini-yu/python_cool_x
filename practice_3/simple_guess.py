# input any N number
# Output: корень этого числа, если он целый
# если такого нет "трудно, не могу"
# def guesss(num: int) -> int:

n = int(input("N:"))

def guess(num: int)-> int | str:
    counter = 0
    for i in range(1, (num//2)+1): # обрезаем половину, потому что после половины, квадрат всегда будет больше n
        counter += 1
        if i*i == num:
            return i
        else:
            if counter == num//2:
                return "Трудно, не могу."

print(guess(n))
