#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def math():
    num1 = int(input('How many number you need in list started from 1 : '))
    number = [i for i in range(1,(num1+1))] 
    Avrage = (sum(number) / len(number))
    print('The Avrage = ' , Avrage)

