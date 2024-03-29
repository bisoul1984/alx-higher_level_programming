#!/usr/bin/python3

def find_peak(list_of_integers):
    # Get the length of the list
    n = len(list_of_integers)
    
    # Base cases
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]
    
    # Binary search
    left = 0
    right = n - 1
    while left < right:
        mid = (left + right) // 2
        # Check if the middle element is a peak
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    # Return the peak element
    return list_of_integers[left]

# Example usage:
print(find_peak([1, 3, 5, 7, 4, 2]))  # Output: 7

