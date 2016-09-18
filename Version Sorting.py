# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 18:17:38 2016

@author: RAVI TEJA
"""
x = ["1.2.3", "3.2.1", "1.1", "0.1", "1.2"]
print x


def answer(x):
    # your code here
    i = len(x) 
    a = []
    print i
    for i in range(i):
        a.append(list(x[i]))
    

   #minor slection
    for i in range(i+1):
        if len(a[i]) == 3:
            a[i].insert(3,'.')
            a[i].insert(4, '0')
    
    for i in range(i+1):
        if len(a[i]) == 1:
            a[i].insert(1,'.')
            a[i].insert(2, '0')
            a[i].insert(3,'.')
            a[i].insert(4, '0')
    print a
    #Major sorting
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j+1]:
                a[j+1], a[j] = a[j], a[j+1]
    
    b = a
    #Minor sorting
    while i < len(b)-1:
        if b[i][0] == b[i+1][0]:
            for j in range(len(a) - 1):
            
                if b[j][2] > b[j+1][2]:
                    b[j+1], b[j] = b[j], b[j+1]
        i +=1
    c = b
    while i < len(b)-1:
        if b[i][0] == b[i+1][0]:
            if b[i][2] == b[i][2]:
                for j in range(len(a) - 1):
            
                    if b[j][4] > b[j+1][4]:
                        b[j+1], b[j] = b[j], b[j+1]
        i +=1
    print "sorted list"
    print c
    
    d = c
    #poping extra elements
    print "after popping"
    for k in range(i+1):
        if d[k][4] == "0":
            d[k].pop(4)
            d[k].pop(3)
            if d[k][2] == "0":
              d[k].pop(2)
              d[k].pop(1)  
    print d
    e = d
    
    #combing into strings
    for k in range(i+1):
        e[k] = "".join(e[k])
    print e


answer(x)
