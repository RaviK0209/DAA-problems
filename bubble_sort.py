def bubble_sort(array):
    n = len(array)
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if array[j]>array[j+1]:
                # temp=array[j]
                # array[j]=array[j+1]
                # array[j+1]=temp
                array[j],array[j+1]=array[j+1],array[j]
    print(f"array after bubble sort is  {array}")
array=list(map(int,input("enter the array elements with space between them: ").split()))
bubble_sort(array)
