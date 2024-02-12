# Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
my_list = ['a', 'b', [1, 2, 3], 'd']
print(*my_list[2])


# Дан список list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'
list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
sum_of_numbers = 0

for i in list_1:
    if isinstance(i, int):
        sum_of_numbers += i

print("Сумма всех чисел в списке:", sum_of_numbers)

list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]

for i in list_1:
    if isinstance(i, str) and 'a' in i:
        print(i)

# Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
a = ['cat', 'dog', 'horse', 'cow']
print(tuple(a))

#  Напишите программу, которая определяет, какая семья больше. 
#      1) Программа имеет два input() - например, family_1, family_2. 
#      2) Членов семьи нужно перечислить через запятую. 
#     Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
family_1 = input().split(",")
family_2 = input().split(",")

if len(family_1) > len(family_2):
    print('Семья 1 больше')
elif len(family_2) > len(family_1):
    print('Семья 2 больше')
else:
    print('Equal')
