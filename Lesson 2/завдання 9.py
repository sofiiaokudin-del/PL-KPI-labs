#Порахувати кількість додатних елементів у заданому масиві.
import random
k = int(input("введіть кількість елементів масиву"))
lst = []
newlst =[]
count = 0
for i in range(k):
    lst.append(random.randint(-100, 100))
for b in range(len(lst)):
    if lst[count] > 0:
        print(lst[count])
        newlst.append(lst[count])
    count +=1
print(newlst)
print("Довжина масиву: ", len(newlst))
