
# coding: utf-8

# In[1]:


from math import*
#list indexes are assumed as user like index 0 is user mark...
list = [[1,9,3], [2,3,5],[0,0,5], [5,1,3]]
#you can add as more list as u want as it is dynamic solution..

def square_rooted(x):
    return round(sqrt(sum([a*a for a in x])),3)
def cosine_similarity(x,y):
    p = sum(a*b for a,b in zip(x,y))
    q = square_rooted(x)*square_rooted(y)
    return round(p/float(q),3)


mx = -99999
for i in range(len(list)):
    print("index...",i)
    for j in range(len(list)):
        if i!=j:
            #printing the similariy between i with all j ..as similarity of mark with all other user ..it is just for debugging
            print(i,"-",j)
            mx = max(mx,cosine_similarity(list[i],list[j]))
            print(cosine_similarity(list[i],list[j]))
    #here each i is a user like maximum similarity for index 0 is maximum similarity for mark with all other user like all indexes..                              
    print("the maximum similarity for ",i ,"is = ",mx)
    print("\n")
    mx = -999999
            


