def insertion_sort(array):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while key<=array[j] and j>-1:
            array[j+1]=array[j]
            array[j]=key
            j=j-1
    print(f"array after insertion sorting is: {array}")

array=list(map(int,input("enter the integers with space between them: ").split()))
insertion_sort(array)