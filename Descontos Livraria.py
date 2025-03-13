# Quantidade de livros que o cliente pega
livroscliente = 5
# Multiplica a quantidade de livros pelo preço ilustrativo de R$30,00
valortotal = livroscliente * 30.00
# Verifica se o clube está ativo fazendo mais um desconto com True(Verdadeiro) ou False(Falso)
clube = True

# Aplica os descontos multiplicando o valor total pela porcentagem de desconto
print(f"O valor SEM desconto será de R$", round(valortotal,2))
if livroscliente <= 1:
    print("Não haverá desconto")
elif livroscliente <= 3:
    valorcomdesconto = valortotal - (valortotal * 10) / 100
    print("O valor COM desconto será de R$",round(valorcomdesconto,2))
elif livroscliente <= 5:
    valorcomdesconto = valortotal -  (valortotal * 20) / 100
    print("O valor COM desconto será de R$",round(valorcomdesconto,2))
else:
    valorcomdesconto = valortotal -  (valortotal * 30) / 100
    print("O valor COM desconto será de R$",round(valorcomdesconto,2))

# Aplica desconto de 5% se o clube estiver ativo
if clube:
    valorfinal = valorcomdesconto - (valorcomdesconto * 5) / 100
    print("Com o desconto do clube ficará R$",round(valorfinal,2))
else:
    print("O deconto do Clube não está ativo")



