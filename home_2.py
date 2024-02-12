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
