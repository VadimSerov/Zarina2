n = int(input("введите максимальную разрядность числа "))
print("Digit fifth powers")
# Граничные условия
sum_digit_max = 0
i = 0
while i < n:
    sum_digit_max += 9**5
    i += 1
print("max sum digit fifth power ",sum_digit_max)
# массив чисел соответствующих условию
hipe = []
# число для проверки
number = 2
while number < sum_digit_max:
    # преобразовать в строку
    str_digit = str(number)
    j = 0
    sum_digit = 0
    while j < len(str_digit):
        # каждую цифру возвести в пятую степень и всё сложить
        sum_digit += int(str_digit[j])**5
        j += 1
    if sum_digit == number:
        # если условию удовлетворяет добавить в массив
        hipe.append(number)
    number += 1
# вывести результат
print(hipe)
