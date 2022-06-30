vogais = ['a','e','i','o','u'] #tambem poderia ter sido usado aspas duplas

for vogal in vogais:

    print(f'Posição = {vogais.index(vogal)}, valor = {vogal}')



vogais = []

print(f"Tipo do objeto vogais = {type(vogais)}")

#objeto.append(valor)

vogais.append('a')
vogais.append('e')
vogais.append('i')
vogais.append('o')
vogais.append('u')

for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")



frutas = ["maçã", "banana", "uva", "mamão", "maçã"]

notas = [8.7, 5.2, 10, 3.5]

print("maçã" in frutas) #True
print("abacate" in frutas) #False
print("abacate" not in frutas) #True
print(min(frutas)) #banana
print(max(notas)) #10
print(frutas.count("maçã")) #2
print(frutas + notas)
print(2*frutas)



lista = ['Python', 30.61, "Java" ,51 ,['a','b',20],"maçã"]

print(f"Tamanho da lista = {len(lista)}")

for i, item in enumerate(lista):
    print(f"Posição = {i},\t valor = {item}-----------------------> tipo individual = {type(item)}")

    

    print("\nExemplos de slices:\n")

    print("lista[1] = ", lista[1])
    print("Lista[0:2] = ", lista[0:2])
    print("Lista [:2]", lista[:2])
    print("Lista [3:5]", lista[3:5])
    print("Lista = [3:6]", lista[3:6])
    print("Lista[3:]", lista[3:])
    print("Lista [-2]", lista[-2])
    print("Lista [-1]", lista[-1])
    print("Lista[4][1]", lista[4][1])


