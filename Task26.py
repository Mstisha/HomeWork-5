a = int(input("Введите число: "))
b = int(input("Введите число во сколько раз возвести: "))
def num(a, b):
    if b == 1:
        return a
    return pow(a, b)
print(num(a, b))