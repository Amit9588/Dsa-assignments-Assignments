#Strassen’s Matrix Multiplication (Exploration)
#Given two square matrices of size A and B of size n * n, find their matrix multiplication. [Hint: Try to solve the given problem using the Divide and Conquer Approach]
def strassen_matrix_multiplication(A, B):
    n = len(A)

    # Base case: If matrices are 1x1, return their multiplication
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Divide both matrices into four equal-sized submatrices
    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Recursive calls to calculate seven matrix products
    P1 = strassen_matrix_multiplication(A11, matrix_subtraction(B12, B22))
    P2 = strassen_matrix_multiplication(matrix_addition(A11, A12), B22)
    P3 = strassen_matrix_multiplication(matrix_addition(A21, A22), B11)
    P4 = strassen_matrix_multiplication(A22, matrix_subtraction(B21, B11))
    P5 = strassen_matrix_multiplication(matrix_addition(A11, A22), matrix_addition(B11, B22))
    P6 = strassen_matrix_multiplication(matrix_subtraction(A12, A22), matrix_addition(B21, B22))
    P7 = strassen_matrix_multiplication(matrix_subtraction(A11, A21), matrix_addition(B11, B12))

    # Combine the seven matrix products to get the result
    C11 = matrix_addition(matrix_subtraction(matrix_addition(P5, P4), P2), P6)
    C12 = matrix_addition(P1, P2)
    C21 = matrix_addition(P3, P4)
    C22 = matrix_subtraction(matrix_subtraction(matrix_addition(P5, P1), P3), P7)

    result = []
    for i in range(mid):
        result.append(C11[i] + C12[i])
    for i in range(mid):
        result.append(C21[i] + C22[i])

    return result

def matrix_addition(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[i]))] for i in range(len(A))]

def matrix_subtraction(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[i]))] for i in range(len(A))]

# Example usage
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = strassen_matrix_multiplication(A, B)
print(result)  # Output: [[19, 22], [43, 50]]

#Median of Two Sorted Arrays (Apple)
#Given two sorted arrays num1 and num2 of size m and n respectively, return the median of the two sorted arrays.
def findMedianSortedArrays(nums1, nums2):
    merged = []
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    merged += nums1[i:]
    merged += nums2[j:]

    n = len(merged)
    if n % 2 == 0:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2
    else:
        return merged[n // 2]

# Example usage
nums1 = [1, 3]
nums2 = [2]
result = findMedianSortedArrays(nums1, nums2)
print(result)  # Output: 2.0

#Pow(x,n) (Facebook)
#Implement pow(x,n) which calculates x raised to the power n (i.e. x^n)
def pow(x, n):
    if n < 0:
        x = 1 / x
        n = -n

    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2

    return result

# Example usage
x = 2.0
n = -2
result = pow(x, n)
print(result)  # Output: 0.25


#Divide Two Integers (Facebook)
#Given two integers, dividend and divisor, divide the two integers without using multiplication, division, and mod operator.
def divide(dividend, divisor):
    if dividend == 0:
        return 0

    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1

    quotient = min(max(sign * quotient, INT_MIN), INT_MAX)
    return quotient

# Example usage
dividend = 10
divisor = 3
result = divide(dividend, divisor)
print(result)  # Output: 3
