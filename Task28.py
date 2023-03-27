a = int(input("Введите число: "))
b = int(input("Введите число: "))
def sumnum(a, b):
    if a < 0 and b < 0:
        return None
    return a + b
print(sumnum(a, b))