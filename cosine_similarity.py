from math import*

list = [[1,9,3], [2,3,5],[0,0,5], [5,1,3]]

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
            print(i,"-",j)
            mx = max(mx,cosine_similarity(list[i],list[j]))
            print(cosine_similarity(list[i],list[j]))
                       
    print("the maximum similarity for ",i ,"is = ",mx)
    print("\n")
    mx = -999999
            

