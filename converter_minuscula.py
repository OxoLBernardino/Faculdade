from traceback import FrameSummary


def converter_minuscula(texto,flag_minuscula=True):

    if flag_minuscula:

        return texto.lower()

    else:

        return texto.upper()

frase=input(f"Digite uma frase: ")

texto1 = converter_minuscula(flag_minuscula=True,texto=(frase))
texto2 = converter_minuscula(texto=(frase))

print(f"\nTexto 1 = {texto1}")

print(f"\nTexto 2 = {texto2}")
