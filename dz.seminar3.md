    Задача №1
    Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

    Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

Решение:
a = [2, 3, 5, 9, 3,]
print(sum(a[1::2])) # [1::2]- Начинаем с первого элемента списка по индексу, с приращением в 2 элемента.




   Задача №2
    Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

    Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]

Решение:

a=[2,3,4,5,6]
new_list=[]
for i in range(len(a)+1//2):
    new_list.append(a[i]*a[len(a)-1-i])
print(new_list[0:3])


Задача №3
    Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

    Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

Решение:
a = [1.1, 1.2, 3.1, 5, 10.01]
min = 1
max = 0
for i in a:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)  
print(max-min)

Задача №4 


    Напишите программу, которая будет преобразовывать десятичное число в двоичное.

    Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
Решение:

n= int(input("Введите n: "))
def k(n):

	if(n > 1):
		
		k(n//2)
	
	print(n%2, end=' ')
	
if __name__ == '__main__':
	k(n)
	print("\n")
