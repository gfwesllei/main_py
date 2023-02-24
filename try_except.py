def readyNumber():
    try:
        valor= int(input("Digite um número"))
        return valor
    except ValueError:
        print("O valor digitado não é um número, digite valor correto:")
        return readyNumber()
    
print(F'Valor digitado foi {readyNumber()}')