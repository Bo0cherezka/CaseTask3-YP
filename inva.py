n = int(input("Введите количество элементов массива: "))

A = []

print("Введите элементы массива:")

for i in range(n):
    A.append(int(input()))

max_index = A.index(max(A))
min_index = A.index(min(A))

left = min(max_index, min_index)
right = max(max_index, min_index)

sum_negative = 0

for i in range(left + 1, right):
    if A[i] < 0:
        sum_negative += A[i]

print("Сумма отрицательных элементов =", sum_negative)