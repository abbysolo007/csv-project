import os
import difflib
f=open('a.csv','r')  
f1=open('b.csv','r') 
str1=f.read()
str2=f1.read()
str1=str1.split()  
str2=str2.split()
d=difflib.Differ()  
diff=list(d.compare(str1,str2))
print '\n'.join(diff)