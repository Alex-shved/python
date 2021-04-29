# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.
import re
matA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matB = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

class Matrix:

    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
            return re.sub('], ',']\n',str(self.lists)[1:-1])

    def __add__(self, other):
        matC = []
        for i in range(len(self.lists)):
            matC.append([])
            for j in range(len(self.lists[0])):
                matC[i].append(self.lists[i][j] + other.lists[i][j])
        return re.sub('], ',']\n',str(matC)[1:-1])


matrix1 = Matrix(matA)
matrix2 = Matrix(matB)

print(matrix1)
print(matrix2)
print(matrix1 + matrix2)