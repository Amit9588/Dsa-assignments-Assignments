# Question 1 
# Solved with the complexity of O(nlogn)
def kth_smallest_element(arr, k):
    arr.sort()
    return arr[k - 1]

# Example usage
arr = [40, 25, 68, 79, 52, 66, 89, 97]
k = 2
result = kth_smallest_element(arr, k)
print(result)  # Output: 40

#Q.2
# Solved with the complexity of O(n)
def sort_colors(nums):
    count = [0, 0, 0]
    for num in nums:
        count[num] += 1

    i = 0
    for color, freq in enumerate(count):
        for _ in range(freq):
            nums[i] = color
            i += 1

# Example usage
nums = [2, 0, 2, 1, 1, 0]
sort_colors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]

#q.3 
# Solved with the complexity of O(n)
import heapq

def kth_largest_element(nums, k):
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

    return min_heap[0]

# Example usage
arr = [40, 25, 68, 79, 52, 66, 89, 97]
k = 2
result = kth_largest_element(arr, k)
print(result)  # Output: 89


# Q.4
# Solved with the complexity of O(n)
def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

# Example usage
nums = [2, 2, 1, 1, 1, 2, 2]
result = majority_element(nums)
print(result)  # Output: 2


#Q.5
# Solved with the complexity of O(logn)
def find_peak_element(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left

# Example usage
nums = [1, 2, 3, 1]
result = find_peak_element(nums)
print(result)  # Output: 2

