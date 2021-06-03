def checkDuplicates(list):    
    for x in list:
        if list.count(x) > 1:
            return True
    return False
l=['a','d','a']
res=checkDuplicates(l)
print(res)

