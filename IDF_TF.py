
# coding: utf-8

# In[3]:


import string
import re
#for python shell IDE read file or write file are like below
#f1 = open("read.txt",'r')
#f2 = open("write.txt','w')
f1 = open("C:/Users/Elias/Desktop/read.txt",'r')
f2 = open("C:/Users/Elias/Desktop/write.txt",'w')
stopword = [",",".","!","-","'","$","^","@","&"]
for line in f1:   
    for i in line:
        flag = 0
        for j in range(len(stopword)):
           if i==stopword[j]:
               flag=1
               #print("..")
               break;
        if flag==0:
            f2.write(i)
tokenize = []

        
            
#example_words = open('write.txt','r')
#example_words = tokenize(example_words)                          
   

f1.close()
f2.close()

modifiedDocument = open("C:/Users/Elias/Desktop/write.txt",'r')
text_string = modifiedDocument.read().lower()
frequency = {}
match_pattern = re.findall(r'\b[a-z]{2,15}\b', text_string)
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
    print (words, frequency[words])

