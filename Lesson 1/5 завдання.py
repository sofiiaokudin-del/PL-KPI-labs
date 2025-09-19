number = input("Введіть число: ")

if number == number[::-1]:
    print(number, "це є паліндром")
else:
    print(number, "це не є паліндром")

