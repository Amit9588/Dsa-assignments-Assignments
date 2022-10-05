#!/usr/bin/env python
# coding: utf-8

# In[ ]:


T(n) = {1         n=1
       2T(n/2 +n) n>1 }

#by substitution method we get
T(n) = 2[2T(n/2^2)+n/2] +n
#by simplifying we get
T(n) = 2^2T(n/2^2) +2n
#Again substituting we get
T(n) = 2^3T(n/n^3) +3n
#by substituting k times we get
T(n) = 2^kT(n/2^k) +kn

#from there we get
(n/2^k) = 1
n = 2^k

#by applying logarithm we get
log2^n = k
#putting the value of k in the equation

2^log2^n.T(n/2^log2^n) +log2^n .n
# by logarithmic formula we get
nT(1) + log2^n .n #put T(1) = 1 then we get

n + nlogn # In Big O time complexity we neglect the constant and lower value

#so The time complexity of the equation is O(nlogn)




# In[ ]:


T(n) = {n=1            1
       8T(n/2)+n^2     n>1}

#by substution method we get
T(n) = 8[8T(n/2^2 + (n/2)^2) +n^2]
#by simplifying the equation
T(n) = 8^2T(n/2^2)+8(n^2/4) +n^2
T(n) = 8^2T(n/2^2) + 3n
# by substituting again we get
T(n) = 8^2[8T(n/2^3) + (n/2^2)^2 + 3n^2]
T(n) = 8^3T(n/2^3) + 64.(n^2/16) + 3n^2
T(n) = 8^3T(n/2^3) + 7n^2
# by substituting upto k times we get
T(n) = 8^kT(n/2^k) + (2^k-1).n^2

#from there we get
n/2^k = 1
n = 2^k

#by applying log we get
log2^n = k

putting the value of k in equation
T(n) = 8^log2^n.T(n/2^log2^n) + (2^log2^n).n^2
# by simplifying the equation we get
T(n)= n^3T(n/n) + (n-1).n^2
# when T(1) is one
T(n) = n^3.1 + n^3 - n^2

# as we know in big o complexity we ignore the constant and lower value and time complexity of this equation is O(n^3)


  


# In[ ]:




