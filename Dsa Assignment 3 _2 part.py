#!/usr/bin/env python
# coding: utf-8

# In[ ]:


T(n) = T(n/2) + T(n/3) + T(n/5) + c

#in recursive tree appraoch n is divided into three parts n/2 , n/3 , n/5 with 3 constant 
T(n) = T(n/2) + T(n/3) + T(n/5) +3c
# After that each of parts are divided into three more parts and this continously going on with each 3 constants
T(n/2) = T(n/2^2) + T(n/3^2) + T(n/5^2) + 3c
T(n/3) = T(n/2^3) + T(n/3^3) + T(n/5^3) + 3c
T(n/5) = T(n/2^5) + T(n/3^5) + T(n/5^5) + 3c
# After this part each of the parts will be divided into 3 parts because of recursion tree aproach
# for time complexity we get three value 2,3,5 as we know in logarithmic lower the value of base higher the value so we choose 2

n/2^k = 1
n = 2^k
#taking log both sides
log2^n = k 

'for constants we get the values:'
    (3)^0.c+ (3)^1.c+(3)^2.c+(3)^3.c..........+(3)^k.c
#taking c common from this equation
    C((3)^0+ (3)^1+(3)^2+(3)^3...........+(3)^k)

#As we know we it's an gp series so we get
a = 1
r = 3 [r >1]

S = a(r^n -1)/(r-1)
S = c[1 (3^log2^n -1)/(3-1)]
S = c[n^log2^3 -1] /2

#by solving the equation the time complexity of this equation is O(n^1.5)




# In[ ]:




