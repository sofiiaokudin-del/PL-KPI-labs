#Вивести всі числа від 100 до 200, які закінчуються на 5.
for number in range(100,201):
    if number % 10 == 5:
        print(number)
