def soma(X,Y):
    R = X + Y
    return R

a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))
c = int(input("Digite um valor para c: "))

s = soma(a, b)
print("a + b = {0}".format(s))

s = soma(a, c)
print("a + c = {0}".format(s))

s = soma(b, c)
print("b + c = {0}".format(s))

print("Fim do programa")