#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution:
	# @param A : tuple of integers
	# @return an integer
	def trap(self, A):
        n=len(A)
        Lmax=[0]*n
        Rmax=[0]*n
        water=0
        
        Lmax[0]=A[0]
        for i in range(1,n):
            Lmax[i]=max(Lmax[i-1],A[i])
        
        Rmax[n-1]=A[n-1]
        for i in reversed(range(n-1)):
            Rmax[i]=max(Rmax[i+1],A[i])
        
        for i in range(0,n):
            water=water+(min(Lmax[i],Rmax[i])-A[i])
        return water
        


# In[ ]:




