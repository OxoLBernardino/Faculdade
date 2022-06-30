def calcular_desconto(valor,desconto=0): # O parâmetro desconto possui valor 0 default.

    valor_com_desconto=valor-(valor*desconto)

    return valor_com_desconto

valor1=calcular_desconto(100) # Não aplicar desconto.
valor2=calcular_desconto(100,0.25) # Aplicar desconto de 25%.

print(f"\nPrimeiro valor a ser pago = {valor1}")

print(f"\nSegundo valor a ser pago = {valor2}")