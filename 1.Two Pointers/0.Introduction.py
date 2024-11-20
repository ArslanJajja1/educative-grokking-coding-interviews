'''
The Two Pointers pattern is a common technique in Data Structures and Algorithms (DSA), particularly useful for solving problems that involve searching pairs or subsequences in arrays or linked lists. It involves using two pointers (or indices) to traverse or examine a data structure in a specific way, often with one pointer starting from the beginning and the other from the end, or both moving in tandem.

                                    When to Use Two Pointers?

Sorted arrays or lists: Problems involving sums or pairs in sorted arrays.
Substring problems: Finding substrings with certain properties.
Merging or comparing sequences: Such as in merge sort or comparison operations.
Removing or modifying elements: Like removing duplicates in-place.

                                            Advantages

Reduces the time complexity compared to brute force approaches.
Often reduces space complexity by not requiring extra data structures.
Simplifies implementation for problems with sorted data.

                                    Types of Two Pointer Techniques
1. Opposite Direction Pointers

One pointer starts at the beginning of the array, and the other starts at the end.
Common for problems that require finding pairs with a specific property.
Example: Find if two numbers sum to a target

def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]  # Indices of the numbers
        elif current_sum < target:
            left += 1  # Increase the sum
        else:
            right -= 1  # Decrease the sum
    return []  # No pair found

# Example usage
arr = [1, 2, 3, 4, 6]
target = 6
print(two_sum_sorted(arr, target))  # Output: [1, 3] (2 + 4 = 6)

Explanation:

Start with left = 0 and right = n-1.
If the sum is less than the target, increment left to increase the sum.
If the sum is greater, decrement right to decrease the sum.
2. Same Direction Pointers
Both pointers start at the same position or close and move in the same direction.
Useful for problems involving subsequences or subarrays.

Example: Find the longest substring with unique characters

def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:  # Shrink the window
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Example usage
s = "abcabcbb"
print(longest_unique_substring(s))  # Output: 3 ("abc")

Explanation:

Use left to shrink the window when a duplicate is found.
Use right to expand the window.

3. Two Pointers for Merging

Useful when merging two sorted arrays.

Example: Merge two sorted arrays

def merge_sorted(arr1, arr2):
    i, j = 0, 0
    merged = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    # Add remaining elements
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    
    return merged

# Example usage
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(merge_sorted(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6]

Explanation:

i and j move forward in their respective arrays.
Compare elements at the current indices and add the smaller one to the merged list.
4. Removing Duplicates (In-place Modifications)
Often used with same-direction pointers to modify arrays in-place.

Example: Remove duplicates from a sorted array


def remove_duplicates(arr):
    if not arr:
        return 0
    
    write_index = 1  # Index for placing the next unique element
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[write_index] = arr[i]
            write_index += 1
    
    return write_index  # Length of the modified array

# Example usage
arr = [1, 1, 2, 2, 3, 4, 4]
length = remove_duplicates(arr)
print(arr[:length])  # Output: [1, 2, 3, 4]

Explanation:

write_index ensures overwriting duplicate values while preserving unique ones.
Complexity

Time Complexity: Typically O(n) for traversals, depending on the operation inside the loop.
Space Complexity: Often O(1), as it doesn't require additional space.
'''