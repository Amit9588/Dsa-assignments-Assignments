#!/usr/bin/env python
# coding: utf-8

# In[ ]:


i = n 
while(i < 2):
    i = (i)^1/25

then i = (n)^1/25
 i = (n)^1/(25)^2
.
.
. k times
i = (n)^1/(25)^k

(n)^1/(25)^k = 2 

Taking logarithm both side

1/(25)^k .log2n = 1

log2n = (25)^k

 Taking log both side again
 log25(log2n) = k

So the time complexity is O(log(logn))


# In[ ]:


i = 29
while i<n:
    i = (i)^23

let n = 30
while 29<30:
    i = (29)^23
    .
    .
    .
    k times 
    i = (29)^23.k
    
    so (29)^23.k = n
    taking log both side
    23k.logn(29) = 1
    logn(29) = 1/(23)^k
    taking again log both side
    log23(logn(29))= k
    
so the time complexity of this question is O(log(logn))


# In[ ]:


i = 1
while i<n:
    i = 2 * i
    i = 3 * i
we can write this equation like this:
    i = 6* i

then let n = 35
then 1<36:
    i = 6*i
    .
    .
    .
    .
the loop is terminated when the value is 30 because the value is gonna be 36 which is greater than n 
thats why loop is terminated

to solve time complexity we can
:
    (6)^k = n
    taking logarithm both side
    k = log6n

so the time complexity is o(log6n)


# In[ ]:





# In[ ]:




