#!/usr/bin/env python
# coding: utf-8

# In[18]:


# This calculates the sum of all numbers from 1 to a given positive integer n.

def sum_of_numbers(n):
    number_total = 0
    for i in range(n+1):
        number_total += i
    print(number_total)
    
sum_of_numbers(5)


# In[62]:


# takes an integer n as a parameter and prints the numbers from 1 to n 
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(5)


# In[34]:


# takes an integer and calculates the facorial of the integer

def factorial_calculator(n):
    holder = 1
    for i in range(1, n+1):
        holder *= i

factorial_calculator(5)


# In[40]:


# takes an integer and calculates the squares of the integer
def squares(n):
    for i in range(1, n + 1):
        squared = i**2
        print(squared) 
squares(4)



# In[43]:


# takes an integer and calculates the sum of the squares leading up to and inclduing integer
def squares(n):
    holder = 0 
    for i in range(1, n + 1):
        squared = i**2
        holder += i**2
    return holder 
squares(4)


# In[49]:


#  takes a string and returns the number of vowels within the string
def vowel_counter(word):
    vowel_count = 0
    for count in word:
        if count == 'a' or count == 'e' or count == 'i' or count == 'o' or count == 'u':
            vowel_count += 1

    return vowel_count
vowel_counter(word = input('please enter a word: '))


# In[60]:


#  takes an integer and returns true if it is a prime number
def prime_number_checker(n):
    for i in range(2, n):
         if n % i == 0:
            return False
    return True
prime_number_checker(21)


# In[ ]:




