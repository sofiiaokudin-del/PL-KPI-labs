#Перевірити, чи містить масив число 0. Якщо так, вивести індекс першого
#нуля.

import random
k = int(input("введіть кількість елементів масиву"))
lst = []
newlst =[]
count = 0
for i in range(k):
    lst.append(random.randint(-100, 100))
if 0 in lst:
    index = lst.index(0)
    print(index)
