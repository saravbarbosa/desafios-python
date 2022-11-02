preco = float(input("Digite o preço: R$"))

desconto = preco * 0.05
novo_preco = preco - desconto

print(f"O preço que custava R${preco:.2f}, agora passa a custar R${novo_preco:.2f} com o desconto de 5%.")
