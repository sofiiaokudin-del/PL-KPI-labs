#Знайти максимальний елемент масиву із 20 випадкових чисел.
import random
lst = [random.randint(1, 100) for _ in range(20)]

print("Масив з 20 випадкових чисел:")
print(lst)

max = max(lst)
print("Максимальний елемент масиву:", max)
