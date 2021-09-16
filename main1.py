def insertion_sort(array):
    length = len(array)
    for i in range(1, length):
        key = array[i]
        j = i
        while (j - 1 >= 0) and (array[j - 1] > key):
            array[j - 1], array[j] = array[j], array[j - 1]
            j = j - 1
        array[j] = key

print("Сортировка вставками")
arr = []
length = int(input("Введите длину массива: "))
for i in range(0, length):
    element = int(input("arr[" + str(i + 1) + "] = "))
    arr.append(element)
insertion_sort(arr)
print("Отсортированный массив: ")
print(arr)