
def merge_interval(intervals):
    intervals = list(intervals)
    intervals.sort(key = lambda i:i[0])
   
    merged_result = [list(intervals[0])]
    for current in intervals[1:]:
        last_merge = merged_result[-1] #add last pair to last merge from merge_result
        
        if current[0] <= last_merge[1]:
            last_merge = max(current[1],last_merge[1])
        else:
            merged_result.append(current)
    return merged_result


intervals = [1,3],[2,6],[8,10,[15,18]]
print(merge_interval(intervals))

def merge_intervals(intervals):
    # Convert intervals to a list if it's a tuple
    intervals = list(intervals)
    
    # Sort intervals based on the start time
    intervals.sort(key=lambda i: i[0])

    # Initialize the merged list with the first interval
    merged = [list(intervals[0])]  # Convert the first interval to a list if needed
    
    for current in intervals[1:]:
        current = list(current)  # Ensure current is a list
        last_merged = merged[-1]  # The last interval in the merged list
        
        # If intervals overlap, merge them
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged.append(current)
    
    return merged

# Example usage
intervals = ((1, 3), (2, 6), (8, 10), (15, 18))  # Input as a tuple
merged_intervals = merge_intervals(intervals)
print("Merged Intervals:", merged_intervals)

