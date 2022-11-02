largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

area = largura * altura
tinta = area / 2

print(f"A quantidade de tinta necessária para a sua parede, com dimensão de {largura}x{altura} e área {area}m², será de: {tinta}l de tinta")
