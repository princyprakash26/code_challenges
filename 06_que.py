# are the Xs equal to the Os?

def XorO(txt):
    X = 0
    O = 0
    for char in txt.upper():
        if char == 'X' :
            X += 1
        elif char == 'O':
            O += 1
    print(X,O)
    if X == O:
        return True
    else:
        return False

x = XorO('i play  and  game .xxxx \ oooo')
print(x)

