def bubble_sort(array):
    for i in range(1,len(array)): #sıraladı
        for a in range (len(array)-i):
            if array[a]>array[a+1]:
                b=array[a]
                array[a]=array[a+1]
                b=array[a+1]
    return array


sayilar=[99,13,14,4,77,34]

print("{}".format(bubble_sort(sayilar)))