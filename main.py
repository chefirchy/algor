def bubble_sort(array):
    length = len(array)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

print("Сортировка пузырьком")
arr = []
n = int(input("Введите длину массива: "))
for i in range(0, n):
    element = int(input("arr[" + str(i + 1) + "] = "))
    arr.append(element)
bubble_sort(arr)
print("Отсортированный массив: ")
print(arr)