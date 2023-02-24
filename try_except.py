def readyNumber():
    try:
        valor= int(input("Please type a number: "))
        return valor
    except ValueError:
        print("Value typed is not a number, please try a number")
        return readyNumber()
    
print(F'Value is {readyNumber()}')