# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# day = int(input('Введите число: '))
# if day < 1 or day > 7:
#     print('It is an input mistake')
# elif day ==6 or day==7:
#     print('Greate! It is weekend!')
# else:
#     print('No, it is not weekend')

# Задача 2.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# print('x y z')
# for x in range (2):
#     for y in range(2):
#         for z in range(2):
#             if (not(x or y or z)) == (not(x) and not(y) and not(z)):
#                 print(x,y,z)
#                 print (f'¬(X={x} ⋁ Y={y} ⋁ Z={z})=¬X={x} ⋀ ¬Y={y} ⋀ ¬Z={z}')

# for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 print(f'x={x}, y={y}, z={z}')
#                 print(not (x or y or z) == (not x and not y and not z))


# Задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input('Введите координаты точки по оси x: '))
# y = int(input('Введите координаты точки по оси y: '))
# if x != 0 and y != 0:
#     if x > 0 and y > 0:
#         print('1')
#     elif x < 0 and y > 0:
#         print('2')
#     elif x < 0 and y < 0:
#         print('3')
#     elif x > 0 and y < 0:
#         print('4') 
# else:
#     if x==0 and y==0:
#         print('Точка находится в месте пересечения осей координат')    
#     elif x==0 and y!=0:
#         print('Точка находится на оси X')
#     elif y==0 and x!=0:
#         print('Точка находится на оси Y')

# Задача 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# quarter = int(input('Введите номер четверти: '))
# if quarter==1:
#     print('x>0 and y>0')
# elif quarter==2:
#     print('x<0 and y>0')
# elif quarter==3:
#     print('x<0 and y<0')
# elif quarter==4:
#     print('x>0 and y<0')
# else:
#     print ('It is an input mistake. Repeate an input')

#5.Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#*Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

#xA = int(input('Введите координаты точки А по оси x: '))
#yA = int(input('Введите координаты точки А по оси y: '))
#xB = int(input('Введите координаты точки B по оси x: '))
#yB = int(input('Введите координаты точки B по оси y: '))
#AB_distance = ((xB-xA)**2 + (yB-yA)**2)**0.5
#print('{:.2f}'.format(AB_distance))