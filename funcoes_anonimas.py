conta = (lambda x: x+1)(x=3)
print(conta)

conta1 = (lambda x,y: x+y)(x=3, y=2)
print(conta1)

somar = lambda x,y: x+y
conta2 = somar(x=5,y=3)
print(conta2)