def moveUp():
    print('Moving up')

def moveDown():
    print('Moving down')

moviments = {
    "u":moveUp,
    "d":moveDown
}    


key = input("Press key U or D")
function = moviments.get(key.lower())
function()