# 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

#n=input("Введи число:")

n=(int(input("Введите число n элементов: ")))
element_list_1=set()
for i in range(n):
    element = int(input("Введите числа "))
    element_list_1.add(element)
print(element_list_1)
m=(int(input("Введите число m элементов: ")))
element_list_2=set()
for i in range(m):
    element = int(input("Введите числа "))
    element_list_2.add(element)
print(element_list_2)
k=element_list_1.intersection(element_list_2)
print(sorted(k))