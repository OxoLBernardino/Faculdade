linguagens = ["Python", "Java", "Javascript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]

#linguagens = "'Python Java Javascript C C# C++ Swift Go Kotlin'"] #Essa sintaxe produz o mesmo resultado que a linha 1

print("Antes da listacomp = ", linguagens)

linguagens = [item.lower() for item in linguagens]

print("\nDepois da listcomp= ", linguagens)





linguagens = '''Python Java Javascript C C# C++ Swift Go Kotlin'''.split()

print("Antes da listcomp = ", linguagens)

for i, item in enumerate(linguagens):
    linguagens[i] = item.lower()

print("\nDepois da listcomp = ", linguagens)


linguagens = '''Python Java Javascript C C# C++ Swift Go Kotlin'''.split()

linguagens_java = [item for item in linguagens if "Java" in item]

print(linguagens_java)



linguagens = '''Python Java Javascript C C# C++ Swift Go Kotlin'''.split()

linguagens_java = []

for item in linguagens:

    if"Java" in item:

        linguagens_java.append(item)

print(linguagens_java)



