
# coding: utf-8

# In[259]:

import numpy as np
from bitarray import bitarray
import random


# In[260]:

## define some helper methods

# @param ca,cb: hashing coefficients
# @param val: value to be hashed
# @param prime: size of hash table
# @return: hash 
def my_hash(ca, cb, val, prime): return (a*val + b) % prime

# set True to @position in @bitar:bitarray
def update_bloom(position, bitarr): bitarr[position] = 1

# find next prime number
def find_next_prime(n): return find_prime_in_range(n, 2*n)

def find_prime_in_range(a, b):
    for p in range(a, b):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            return p
    return None

# test
print find_next_prime(19+1)


# In[261]:

# example list of spam emails
email_list = ["spammer1@gmail.com", "spammer2@viagra.com",
              "spammer2@gmail.com","imnotAspammer@gmail.com",
              "checkmywebsite@hotmail.com", "dark_net@yougotme.com"]


# In[262]:

# initialise bloom filter
bloom_filter = bitarray(hashtable_size)
# set all bits to 0
bloom_filter[:] = False
print "Bloom Filter:", bloom_filter


# In[263]:

# calculate unicode sum of characters for every email-address
email_unicode_sum_list = [sum([ord(char) for char in email]) for email in email_list]
email_unicode_sum_list


# In[264]:

#The coefficients a and b are randomly chosen integers less than the maximum value of x. 
#c is a prime number slightly bigger than the maximum value of x.

# h_x = (a*x + b)%c

# choose 2 random numbers up to maximum unicode value 
# and set them to be hashing coefficients
a = random.randint(1, max(email_unicode_sum_list)-1)
b = random.randint(2, max(email_unicode_sum_list)-1)

print a,b


# In[265]:

# since we have fixed size of input, the hashtable could have 1.0 load factor
# yet, 0.75 load has much less colisions
# choose next prime number from the number of elements in email list
hashtable_size = find_next_prime(int(round(len(email_unicode_sum_list)*1.25)))
hashtable_size


# In[266]:

# hash emails
hash_list = [my_hash(a,b,unicode_sum,hashtable_size) for unicode_sum  in email_unicode_sum_list]


# In[267]:

# assign hash_values & unicode-sums to emails
[(email,"->",unicode_sum, "->", hashp) for email, unicode_sum, hashp in zip(email_list, email_unicode_sum_list, hash_list)]


# In[269]:

# update bloom filter
[update_bloom(index, bloom_filter) for index in hash_list]
# check updated bloom filter
bloom_filter


# In[271]:

## now do some tests
# for every email in the list check if it has already been seen by bloom filter
for email in email_list:
    if bloom_filter[my_hash(a,b,sum([ord(char) for char in email]),hashtable_size)] == True: 
        print email, "has ALREADY been seen";
    else:
        print email, "has NOT been seen";


# In[ ]:



