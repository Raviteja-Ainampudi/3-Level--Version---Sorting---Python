# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 22:13:04 2016

@author: RAVI TEJA
"""

x = [ "0", "00.00", "0.0", "0.0.0", "0.1", "0.01"]
print x
def answer(x): 
    i = len(x) 
    a = []
    #print i
    for i in range(i):
        m = x[i].split('.')
        if len(m) == 3:
            m.insert(1,".")
            m.insert(3,".")
        elif len(m) ==2:
            m.insert(1, ".")
        else:
            pass
        a.append(m)
    
    for i in range(i+1):
        if len(a[i]) == 3:
            a[i].insert(3,'.')
            a[i].insert(4, '0000000000000000000000000000000000000000000000000')
    
    for i in range(i+1):
        if len(a[i]) == 1:
            a[i].insert(1,'.')
            a[i].insert(2, '0000000000000000000000000000000000000000000000000')
            a[i].insert(3,'.')
            a[i].insert(4, '0000000000000000000000000000000000000000000000000')    
    #print a
    #Sorting - Major
    for i in range (len(a)):
        for j in range (i+1,len(a)):
            if int(a[i][0]) > int(a[j][0]):
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    print "Major sorting"
    #print a
    
    for i in range (len(a)):
        for j in range (i+1,len(a)):
            if int(a[i][0]) == int(a[j][0]):
                if int(a[i][2]) > int(a[j][2]):
                    temp = a[i]
                    a[i] = a[j]
                    a[j] = temp
    print "Minor sorting"
    #print a
    
    for i in range (len(a)):
        for j in range (i+1,len(a)):
            if (int(a[i][0]) == int(a[j][0])) and (int(a[i][2]) == int(a[j][2])):
                    if(int(a[i][4]) > int(a[j][4])):
                        temp = a[i]
                        a[i] = a[j]
                        a[j] = temp
                    
    print "Revision sorting"
    #print a
    for k in range(i+1):
        if a[k][4] == "0000000000000000000000000000000000000000000000000":
            a[k].pop(4)
            a[k].pop(3)
            if a[k][2] == "0000000000000000000000000000000000000000000000000":
              a[k].pop(2)
              a[k].pop(1)
    print "after popping"
    #print a
    e = a
    
    #print e
    
    #Re-order elements
    f=[]
    for k in range(len(e)):
        f.append(list(e[k]))
    #print f
    # 3 to 2
    for k in range (len(f)-1):
        if (len(f[k])==5) and (len(f[k+1])==3):
            if ((int(f[k][0]))== int(f[k+1][0])) and ((int(f[k][2]))==int(f[k+1][2])):
                if int(f[k][4])== 0:
                    temp = f[k+1]
                    f[k+1] = f[k]
                    f[k] = temp
    #3 to 1
    for k in range (len(f)-1):
        if (len(f[k])==5) and (len(f[k+1])==1):
            if ((int(f[k][0]))== int(f[k+1][0])):
                if (int(f[k][4])==0) and (int(f[k][2])==0):
                    temp = f[k+1]
                    f[k+1] = f[k]
                    f[k] = temp
    
    #2 to 1
    for k in range (len(f)-1):
        if (len(f[k])==3) and (len(f[k+1])==1):
            if (int(f[k][0])==int(f[k+1][0])):
                if (int(f[k][2]))==0:
                    temp = f[k+1]
                    f[k+1] = f[k]
                    f[k] = temp
    
    h = f
    for k in range(i+1):
        h[k] = "".join(f[k])
    print "End result"
    print h
answer(x)