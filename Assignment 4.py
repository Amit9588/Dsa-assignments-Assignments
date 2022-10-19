

# In[ ]:

Q.1
T(n) = {1   n = 1

        T(n / 2 + n)  n > 1}

# by substitution method we get
T(n) = 2[2
T(n / 2 ^ 2) + n / 2] +n
# by simplifying we get
T(n) = 2 ^ 2
T(n / 2 ^ 2) + 2
n
# Again substituting we get
T(n) = 2 ^ 3
T(n / n ^ 3) + 3
n
# by substituting k times we get
T(n) = 2 ^ kT(n / 2 ^ k) + kn

# from there we get
(n / 2 ^ k) = 1
n = 2 ^ k

# by applying logarithm we get
log2 ^ n = k
# putting the value of k in the equation

2 ^ log2 ^ n.T(n / 2 ^ log2 ^ n) + log2 ^ n.n
# by logarithmic formula we get
nT(1) + log2 ^ n.n  # put T(1) = 1 then we get

n + nlogn  # In Big O time complexity we neglect the constant and lower value

# so The time complexity of the equation is O(nlogn)


# In[ ]:




# In[ ]:

#Q.2
t(n) = 2t(n/2) + n/log(n)
     = 2(2t(n/4) + n/2/log(n/2)) + n/log(n)
     = 4t(n/4) + n/log(n/2) + n/log(n)
     = 4(2t(n/8) + n/4/log(n/4)) + n/log(n/2) + n/log(n)
     = 8t(n/8) + n/log(n/4) + n/log(n/2) + n/log(n)
     = 16t(n/16) + n/log(n/8) + n/log(n/4) + n/log(n/2) + n/log(n)
     = n * t(1) + n/log(2) + n/log(4) + ... + n/log(n/2) + n/log(n)
     = n(1 + Sum[i = 1 to log(n)](1/log(2^i)))
     = n(1 + Sum[i = 1 to log(n)](1/i))
     ~= n(1 + log(log(n)))
     = n + n*log(log(n)))
     ~= n*log(log(n))

Q.3
T(n) = 2T(n/2)+n^2
by applying the master theorm we get
a=2 ,b= 2, k=2, p=0
so log2^2 = 1  which is less than k so and p = 0 so
0(n^k.logn^p)
so the time complexity is o(n^2)

Q.4
T(n) = {n = 1               1

        8T(n / 2) + n ^ 2   n > 1}

# by substution method we get
T(n) = 8[8
T(n / 2 ^ 2 + (n / 2) ^ 2) + n ^ 2]
# by simplifying the equation
T(n) = 8 ^ 2
T(n / 2 ^ 2) + 8(n ^ 2 / 4) + n ^ 2
T(n) = 8 ^ 2
T(n / 2 ^ 2) + 3
n
# by substituting again we get
T(n) = 8 ^ 2[8
T(n / 2 ^ 3) + (n / 2 ^ 2) ^ 2 + 3
n ^ 2]
T(n) = 8 ^ 3
T(n / 2 ^ 3) + 64.(n ^ 2 / 16) + 3
n ^ 2
T(n) = 8 ^ 3
T(n / 2 ^ 3) + 7
n ^ 2
# by substituting upto k times we get
T(n) = 8 ^ kT(n / 2 ^ k) + (2 ^ k - 1).n ^ 2

# from there we get
n / 2 ^ k = 1
n = 2 ^ k

# by applying log we get
log2 ^ n = k

putting
the
value
of
k in equation
T(n) = 8 ^ log2 ^ n.T(n / 2 ^ log2 ^ n) + (2 ^ log2 ^ n).n ^ 2
# by simplifying the equation we get
T(n) = n ^ 3
T(n / n) + (n - 1).n ^ 2
# when T(1) is one
T(n) = n ^ 3.1 + n ^ 3 - n ^ 2

# as we know in big o complexity we ignore the constant and lower value and time complexity of this equation is O(n^3)
