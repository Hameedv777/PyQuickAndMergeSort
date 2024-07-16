def quick_Sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[0]
        lesser_tha_pivot=[x for x in arr[1:]if x<=pivot]
        greater_than_pivot=[x for x in arr[1:]if x> pivot]
        return quick_Sort(lesser_tha_pivot)+[pivot]+quick_Sort(greater_than_pivot)
#Example usage:
my_list=[10,7,8,9,5,1]
print("Unsorted list",my_list)
sorted_lisst=quick_Sort(my_list)
print("Sorted list is :",sorted_lisst)