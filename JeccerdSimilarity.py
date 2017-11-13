
# coding: utf-8

# In[1]:


from math import*

#list indexes are assumed as user like index 0 is user mark...
list = [[1,9,3], [2,3,5,0,1,3],[0,0,5], [5,1,3],[3,5,9]]
#you can add as more list as u want as it is dynamic solution..
def jaccard_similarity(x,y):
    p = len(set.intersection(*[set(x),set(y)]))
    q = len(set.union(*[set(x),set(y)]))
    return p/float(q)

mx = -99999
for i in range(len(list)):
    print("index...",i)
    for j in range(len(list)):
        if i!=j:
            #printing the similariy between i with all j ..as similarity of mark with all other user ..it is just for debugging
            print(i,"-",j)
            mx = max(mx,jaccard_similarity(list[i],list[j]))
            print(jaccard_similarity(list[i],list[j]))
    #here each i is a user like maximum similarity for index 0 is maximum similarity for mark with all other user like all indexes..                   
    print("the maximum similarity for ",i ,"is = ",mx)
    print("\n")
    mx = -999999
#            


