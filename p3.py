
def divideList(list,size):
    list1=[]
    i=0
    while(i<len(list)):
          for j in range(i,size):
              list1[j].append(list[j])
         
          i+=1;
    print(list1)       

l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
n=3
divideList(l,n)

          
          
          
          
          
          
        
        
    
