
# coding: utf-8

# In[12]:


import math
x=[3,4,4,5,5,1]
y=[3,2,3,2,4,3]
length=len(a)
muX=sum(a)/length
muY=sum(b)/length
print("muX = ",muX,"muY=",muY)
sigmaSquareX=float(sum([(x-c)**2 for x in a]))/length
sigmaSquareY=float(sum([(x-d)**2 for x in b]))/length
print("sigmaSquareX=",sigmaSquareX,"sigmaSquarey=",sigmaSquareY)

sigmaX = math.sqrt(sigmaSquareX)
sigmaY = math.sqrt(sigmaSquareY)
print("sigmaX=",sigmaX,"sigmaY=",sigmaY)

#here 2*pi = 6.2832 
Nx = ((1/(math.sqrt(6.2832)*sigmaX)))*math.exp(-((x[-1]-muX)**2)/(2*sigmaSquareX))
Ny = ((1/(math.sqrt(6.2832)*sigmaY)))*math.exp(-((y[-1]-muY)**2)/(2*sigmaSquareY))
print("Nx=",Nx,"Ny=",Ny)
print(Nx*Ny)


