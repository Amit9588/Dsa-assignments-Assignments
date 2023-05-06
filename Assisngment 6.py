####################### Assignment 6 #######################

# Q.1 

# def heapify(arr, n, i):
#     smallest = i
#     left = 2 * i + 1
#     right = 2 * i + 2
  
#     if left < n and arr[left] < arr[smallest]:
#         smallest = left
  
#     if right < n and arr[right] < arr[smallest]:
#         smallest = right
  
#     if smallest != i:
#         arr[i], arr[smallest] = arr[smallest], arr[i]
#         heapify(arr, n, smallest)
  
# def buildHeap(arr, n):
#     start_idx = n // 2 - 1
#     for i in range(start_idx, -1, -1):
#         heapify(arr, n, i)
#     return arr

# Q.2  most frequent words
import heapq

def topKFrequent(words, k):
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    heap = [(-count, word) for word, count in freq.items()]
    heapq.heapify(heap)
    
    topk = []
    for i in range(k):
        count, word = heapq.heappop(heap)
        topk.append(word)
    
    return sorted(topk)

# Q.3  k closest point approach by quicksort algorithm to improve time complexity

import math

def kClosest(points, k):
    def partition(l, r):
        pivot = distances[r]
        i = l - 1
        for j in range(l, r):
            if distances[j] < pivot:
                i += 1
                distances[i], distances[j] = distances[j], distances[i]
                points[i], points[j] = points[j], points[i]
        distances[i+1], distances[r] = distances[r], distances[i+1]
        points[i+1], points[r] = points[r], points[i+1]
        return i+1
    
    distances = [math.sqrt(x**2 + y**2) for x, y in points]
    left, right = 0, len(points)-1
    while left <= right:
        pivot_idx = partition(left, right)
        if pivot_idx == k-1:
            return points[:k]
        elif pivot_idx < k-1:
            left = pivot_idx + 1
        else:
            right = pivot_idx - 1
