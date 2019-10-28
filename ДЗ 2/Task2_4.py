# ЗАДАНИЕ 4

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]

# создаём новый список
list_3 = []
for i in range(len(list_1)):
    list_3.append(list_1[i] + list_2[i])
    # выводим print'ом
    print(list_1[i] + list_2[i], end=' ')
# выводим новый список 
print(list_3)




