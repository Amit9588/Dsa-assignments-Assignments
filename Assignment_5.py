


def squareRoot(number):
    start = 0
    end, ans = number, 1

    # For computing integral part
    # of square root of number
    while (start <= end):
        mid = int((start + end) / 2)

        if (mid * mid == number):
            ans = mid
            break

        # incrementing start if integral
        # part lies on right side of the mid`
        if (mid * mid < number):
            start = mid + 1
            ans = mid

        # decrementing end if integral part
        # lies on the left side of the mid
        else:
            end = mid - 1

    # For computing the fractional part
    # of square root upto given precision


    return ans



# Driver code
number = 8

print(squareRoot(number))

#Q.2
# Method Definition
def first_bad_version(a):
    left = 0
    right = len(a) - 1
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if a[mid - 1] == 0 and a[mid] == 1:
            ans = mid
            break
        elif a[mid] == 0:
            left = mid + 1
        else:
            right = mid - 1

    return ans


# Driver Code
a= [0,2,2,2,2,2]
print(first_bad_version(a))

#Q.3
def perfect_square(num):
    left = 0
    right = num

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == num:
            return True

        elif mid * mid > num:
            right = mid - 1

        else:
            left = mid + 1
    return False


## Driver Code
num = 28
print(perfect_square(num))