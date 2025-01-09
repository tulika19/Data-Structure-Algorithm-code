def merge_two_sortedArray(nums1,nums2):
    result =[]
    i = j = 0
    while i<len(nums1) and j<len(nums2):
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i+=1
        else:
            result.append(nums2[j])
            j+=1
    result.extend(nums1[i:])
    result.extend(nums2[j:])
    n = len(result)
    mid = n//2
    if n%2 !=0:
        return result[mid]
    else:
        return (result[mid-1]+result[mid])/2.0
    

nums1 = [1,3,4]
nums2 = [2]
print(merge_two_sortedArray(nums1,nums2))