def rotate_array_k_step(arr,k):
    k = k%len(arr)
    l,r = 0,len(arr)-1
    while(l<r):
        arr[l],arr[r] = arr[r],arr[l]
        l+=1
        r-=1
    l,r = 0,k-1
    while(l<r):
        arr[l],arr[r] =arr[r], arr[l]
        l+=1
        r-=1
    l,r = k,len(arr)-1
    while(l<r):
        arr[l],arr[r] = arr[r],arr[l]
        l+=1
        r-=1
    return arr

arr =[1,2,3,4,5,6]
k=7
print(rotate_array_k_step(arr,k))