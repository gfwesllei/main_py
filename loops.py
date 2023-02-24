def paresInRange(start:int,end:int):
    pares =[]
    for index in range(start,end):
        if index%2==0:
            pares.append(index)
    
    return len(pares)

total = paresInRange(start=1,end=10);
print(total)
assert total == 4, "Expected 4 numbers"