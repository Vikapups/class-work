a = int(input("Введите количество чисел ряда Фибоначчи:"))
fib1 = 0
fib2 = 1
print(fib1)
print(fib2)
i = 2
while i < a:
    s = fib1 + fib2
    print(s)
    fib1 = fib2
    fib2 = s
    i = i + 1 