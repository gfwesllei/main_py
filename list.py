itens = [['Banan','maca'],['Mamao','uva']]

for ic in range(0,len(itens)):
    #print(itens[ic])
    for il in range(0,len(itens[ic])):
        print(itens[ic][il])


items =[1,2,3,4,5,6,7]

item1,*others,last = items

print(item1,last)
print(others)