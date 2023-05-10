########    Assignmemt 7 ################

# q.1 using two pointer appraoch
# time complexity O(n^2)

def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    closestSum = float('inf')

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]

            if currentSum == target:
                return currentSum

            if abs(currentSum - target) < abs(closestSum - target):
                closestSum = currentSum

            if currentSum > target:
                right -= 1
            else:
                left += 1

    return closestSum


# q.2  Given three points, check whether they lie on a straight (collinear) or not.

# Time complexity (1) and space complexity o(1)

def arePointsCollinear(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    slope1 = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else float('inf')
    slope2 = (y3 - y2) / (x3 - x2) if (x3 - x2) != 0 else float('inf')

    return slope1 == slope2


p1 = (1, 1)
p2 = (2, 2)
p3 = (3, 3)

collinear = arePointsCollinear(p1, p2, p3)
print(collinear)


''' Q.3  An e-commerce site tracks the purchases made each day. The product that is purchased
the most one day is the featured product for the following day. If there is a tie for the product
purchased most frequently, those product names are ordered alphabetically ascending and
the last name in the list is chosen.[Amazon]

using heap time and space complexity can be improved than naive approach

'''

import heapq

def findFeaturedProduct(purchases):
    product_counts = {}
    
    # Step 2: Update frequencies
    for product in purchases:
        product_counts[product] = product_counts.get(product, 0) + 1
    
    pq = []
    
    # Step 4: Insert products into priority queue
    for product, count in product_counts.items():
        heapq.heappush(pq, (-count, product))  # Using negative count for max heap behavior
    
    top_products = []
    
    # Step 6: Pop products with highest frequency
    while pq and (-pq[0][0]) == (-pq[0][0]):
        _, product = heapq.heappop(pq)
        top_products.append(product)
    
    # Step 7: Sort products in ascending alphabetical order
    top_products.sort()
    
    # Step 8: Return the last product
    return top_products[-1]

purchases = ["apple", "banana", "apple", "orange", "banana", "apple", "banana"]

featured_product = findFeaturedProduct(purchases)
print(featured_product)



''' Q.4 An almost sorted array is given to us and the task is to sort that array completely. Then,
which sorting algorithm would you prefer and why?[Salesforce]

for almost sorted array inserton sort is better than any other approach cause of its time complexity w
which is o(n+k)
'''

def insertionSort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

# Example usage:
arr = [3, 2, 1, 5, 4, 7, 6]
insertionSort(arr)
print(arr)
