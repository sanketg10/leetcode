def my_sort(a):  
    for i in range(1,len(a)): 
        while i>0 and a[i] < a[i-1]: 
            temp = a[i-1] 
            a[i-1] = a[i] 
            a[i] = temp  
            i = i-1  
    return a 
        
a = [5,6,3,10,78,1,49] 
# a.sort() 
print my_sort(a)