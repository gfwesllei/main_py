values = [3,'a',30,'p']

numbers = filter(lambda item: type(item)==int,values)

print(list(numbers))
