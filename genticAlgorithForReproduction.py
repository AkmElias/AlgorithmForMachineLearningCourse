
# coding: utf-8

# In[141]:


import math
#population...
populations  = [[1,0,0,1,0],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,0],[1,0,1,1,1]]
#expected outecome or target generation
expected_output = [1,1,0,1,0]
#maximum bit not changed..
mxbit = 0
for i in range(len(populations)):
    cnt = 0
    for bit in range(len(populations[i])):
        #print(populations[i][bit])
        if populations[i][bit]!=expected_output[bit]:
            break
        else:
            cnt+=1
    if mxbit<cnt:
        mxbit = cnt
print("bit will rmain same upto ",mxbit)  
#main algo start...
#we will need these list later..
listToCross = []
listToCross2 = populations
#homany time the expected generation found..
maincount = 0
#threshold_value assigninig or assuming..let assume 2 for this problem
thv = 2
flag=0

#fitness function..we will do this by comparing eith expected outecome to all the population given
value = []
def bestFit(population):  
    global value
    value = []
    #print("bestfit")
    j = 0
    for i in range(len(population)):
        cnt = 0
        for bit in range(len(population[i])):
            #print(populations[i][bit])
            if population[i][bit]!=expected_output[bit]:
                cnt+=1
        value.append(cnt)
    #j+=1
    
#list assigning after best fit function..
def assigningBestPopulations(population):
    global value
    for i in range(len(population)):
        if value[i]<=2:
            #print(value[i]) 
            listToCross.append(population[i])
        
        
def crossover():
    #print(i)
    global listToCross2
    global mxbit
    listcr = []
    check = 0
    flag=0
    maincount = 0
   
        #crossover for every combination..
    for j in range(len(listToCross)-1):
        cmp1 = j
        for k in range(len(listToCross)-j-1):
            cmp1+=1
            temp1 = []
            temp2 = []
            for vl in range(len(listToCross[cmp1])):
                    #bit can remain same upto maxbit ..
                if vl<mxbit:
                    temp1.append(listToCross[j][vl])
                    temp2.append(listToCross[cmp1][vl])
                    #else flip the bit ...    
                else:
                    temp1.append(listToCross[cmp1][vl])
                    temp2.append(listToCross[j][vl])
                        
            check = 0
            for vl in range(len(expected_output)):
                    #print(temp1[vl])
                if temp1[vl]!=expected_output[vl]:
                        #print(1)
                    check=1
                        
            if check==0:
                maincount+=1
                flag=1
                    #print(1)
            check=0
              
            for vl in range(len(expected_output)):
                    #print(temp1[vl])
                if temp2[vl]!=expected_output[vl]:
                    check=1
                        
            if check==0:
                flag=1
                maincount+=1
                    #print(1)
                #new two population found after crossover...                           
            listcr.append(temp1)
            listcr.append(temp2)
        #storing the new populations for future need like if i >0..these new populations will crossover among them..      
        listToCross2 = listcr 
    #equations are smae here but combinations are different..     
   
       
       
        #print(listcr)
       
    return flag,maincount 
#here looping limit is 3 because it assumed that within 3 crossover target generation will be found..
for i in range(3):
    bestFit(listToCross2)
    assigningBestPopulations(listToCross2)
    flag,maincount = crossover()
    if flag==1:
        print("found ",maincount)
        break
            
