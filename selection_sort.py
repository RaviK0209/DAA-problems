def selection_sort(array_list):
    for i in range(0,len(array_list)):
        min=i
        for j in range(i+1,len(array_list)):
            if(array_list[min]>array_list[j]):
                min=j
        array_list[i],array_list[min]= array_list[min],array_list[i]
    print(array_list)

# input_array=input("enter the integers with a space between them")
# input_array=input_array.split()
# input_array=map(int,input_array)
# array_list=list(input_array)
array_list=list(map(int,input("enter the integers with a space between them: ").split()))
# array_list=[2,1,7,6,5,3,4,9,8]
selection_sort(array_list)
