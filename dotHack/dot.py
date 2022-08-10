from random import choice

def createpass(data):
    password = ''
    char = '0123456789abcdefghijklmnopqrsvuwxyz'
    for i in range(data):
        password += choice(char)
    return password

print(createpass(8))    
