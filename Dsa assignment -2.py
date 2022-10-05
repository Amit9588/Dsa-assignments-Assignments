#!/usr/bin/env python
# coding: utf-8

# In[ ]:


f(n) = n-10
g(n) = n+10 

#we have to prove that f(n) = θ(g(n)) 

so for big(o) 
f(n) <= c(g(n))
n-10 <= 1. n+10  #condtition is satisfied as value of c is 1 and it's constant

 f(n) =O(g(n))
#Now we have to check for omega
f(n) >= Ω(g(n))
n-10 >= c.n+10
n-10 >= 1/5 . n+10 # conditon is satisfied as value of c is 1/5 and it's constant]
                    
#so both conditon are satisfed thats why the condtion of theta is also satisfied
                    
it is True                  


# In[ ]:


f(n) =n
g(n)= n

#we have given the condtion f(n)=  θ(g(n))

so for big(o)
f(n) <= c(g(n))
n = 1.n #here the value of constant is 1 so condtion satistfied

#Now we have to check for omega

f(n) >= c(g(n))
n = 1.n #here the condtion is also satisfied 

so It is True


# In[ ]:


64^log2^n . 32^log2^n =O(n^5)

#by applying logarithmic formula we get

n^6.n^5 = O(n^5)
#for bigo conditon is given
f(n) <= c(g(n))
n^11 <= c(n^5) # here the condtion is not satisfied because we have to multiply with n^6 which is not a constant

It is False


# In[ ]:


4^n/2^n = O(2^n)
#Here by applying maths we get
2^n = o(2^n)
#so the condtion for big o is:
f(n) <= c.(g(n))
2^n <= 1.2^n # here the conditon is satisfied and value is 1 which is constant

It is True


# In[ ]:


128.log2^n .n^2 = o(n^9)
#By applying log we get

n^7.n^2 = O(n^9)
#for bigo the condition is
f(n) <= c(g(n))
n^9 <= 1.n^9 #here the condition is satisfied and the value of c is also constant

It is True

