#hide the credit card number:

def hide(num):
    
    print( '*'* (len(num) - 4) +num[-4:])

hide('6337279198956')

