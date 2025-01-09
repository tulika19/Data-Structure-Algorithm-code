def missing_num(arr):
    n = len(arr)
    total_sum = (n*(n+1))//2
    arr_sum=sum(arr)
    return total_sum - arr_sum

def missing_num_style2(arr):
    n = len(arr)+1
    return (n*(n+1))//2 - sum(arr)
def missing_num_with_zero(arr):
    n = len(arr)  # Array length
    max_num = max(arr)  # Maximum number in the range
    total_sum = (max_num * (max_num + 1)) // 2  # Full sum
    arr_sum = sum(arr)
    return total_sum - arr_sum
    

arr =[9,6,4,2,3,5,7,0,1]
arr1 =[1,3,4,5]
print(missing_num(arr))
print(missing_num_style2(arr1))
print(missing_num_with_zero(arr))