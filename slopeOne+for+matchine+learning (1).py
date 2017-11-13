
# coding: utf-8

# In[4]:


import math
A = [5,3,0]
B = [3,4,2]
C = [2,0,5]
L = [A,B,C]
#0 in the list means no value in that position .. have to find or predict  the value for that position
jhon = [5,3,2]
mark = [3,4,0]
lucy = [0,2,5]

def averageRating(X,Y):
    sum = 0
    cnt = 0
    for i in range(len(X)):
        if X[i]!=0 and Y[i]!=0:
            sum = sum + (X[i]-Y[i])
            cnt+=1
    return float(sum)/cnt,cnt

#for mark...because mark has one position where value is missing
#to find the missing value for a user just copy the below code and just replase user name
rating = 0
temp = 0
for i in range(len(mark)):
    if mark[i]==0:
        #print("ajaj")
        for j in range(len(L[i])):
            if j!=i:
                t1,count = averageRating(L[j],L[i])
                temp = float((mark[j]+t1))*count
                #print(mark[j])
                #print(t1,count)
                #print(temp)
                rating = rating+temp
answer = float(rating)/len(L)
print("for mark .. = ",answer)
#for lucy...because lucy has one position where value is missing
rating = 0
temp = 0
for i in range(len(lucy)):
    if lucy[i]==0:
        #print("ajaj")
        for j in range(len(L[i])):
            if j!=i:
                t1,count = averageRating(L[j],L[i])
                temp = float((lucy[j]+t1))*count
                #print(lucy[j])
                #print(t1,count)
                #print(temp)
                rating = rating+temp
answer = float(rating)/len(L)
print("for lucy .. = ",answer)


