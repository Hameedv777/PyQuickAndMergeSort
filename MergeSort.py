def merge_sort(arr):
    if len(arr)<=1:
        return(arr)
    
    mid=len(arr)//2
    left_half=arr[:mid]
    right_half=arr[mid:]
    
    left_half=merge_sort(left_half)
    right_half=merge_sort(right_half)
    
    return merge(left_half,right_half)

def merge(left,rigt):
        result=[]
        left_idx=0
        rigt_idx=0
        
        while left_idx < len(left) and rigt_idx < len(rigt):
            if left[left_idx]<rigt[rigt_idx]:
        
        
                result.append(left[left_idx])
                left_idx+=1
            else:
                result.append(rigt[rigt_idx])
                rigt_idx+=1
        result.extend(left[left_idx:])
        result.extend(rigt[rigt_idx:])
        return result
#Example Usage:
arr=[12,11,13,5,6,7]
sorted_arr=merge_sort(arr)
print("Sorted Array is: ",sorted_arr)