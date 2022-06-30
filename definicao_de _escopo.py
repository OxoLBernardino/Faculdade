def EstudaEscopo():
    Y = X * 2 
    print("X global existe dentro da função: valor = {0}".format (X))
    print("Y local existe dentro da função: valor = {0}".format(Y))

print("Inicio Programa")

X = 10
print("X global existe fora da função: valor = {0}".format(X))
EstudaEscopo()
print("Fim do programa")
