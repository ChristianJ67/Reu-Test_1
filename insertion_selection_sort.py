list = []
n = int(input("how numbers"))

for i in range(0,n): 
    print("num", i+1)
    numlist = int(input("type number you want in list"))
    
    list.append(numlist)
    print("its goes selection then insertion")
    
    
def selection_sort(a):
    for i in range(len(a)):
        low = i 
        for j in range(i+1, len(a)):
            if a[j] < a[low]:
                low = j 
            a[i], a[low] = a[low], a[i]
selection_sort(list)
print(list)


def insertion_sort(a): 
     for i in range(1,len(nums)): 
         x = a[i]
         j = -1 
         while >= 0 and a[j] > x:
             a[j+1] = a[j]
             j -= 1 
        a[j+1] = x
insertion_sort(list)
print(list)





            
    
    
    
    


