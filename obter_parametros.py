def imprimir_parametros(*args):

    qtd_parametros = len(args)

    print(f"Quantidade de parametros = {qtd_parametros}")

    for i, valor in enumerate(args):

        print(f"Posição = {i}, valor = {valor}")

print("\nChamada 1")

imprimir_parametros("São Paulo",10,23.78, "João")

print("\nChamada 2")

imprimir_parametros(10,"São Paulo")
