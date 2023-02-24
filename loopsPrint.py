def printSqr(size:int,border:str):
    for index_col in range(size):
        for index_line in range(size):
            print(border)
    print()


def ifTernario(value:int):
    if 20<= value <=30:
        return True
    return False


def functionArgs(name,*values):
    print(F'{name} contains :')
    for value in values:
        print(F'# {value} ',end='')
    print()


def printParam(param:str,**item):
    print(item[param])


printParam('name',name='Michael',age=30,balance=0)


#functionArgs('Item1','Cafe')
#functionArgs('Item2','Cafe','Macarrao')

#print(F'Value returned {ifTernario(25)}')
#printSqr(4,"#")