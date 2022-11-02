dias = int(input("Digite a quantidade de dias alugados: "))
km = float(input("Digite a quantidade de Km rodados: "))

valor_dias = 60  
valor_km = 0.15
total = (dias * valor_dias) + (km * valor_km)

print(f"O  valor total a ser pago é: R${total:.2f}")
