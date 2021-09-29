#Conversor de medidas

# tabela de conversao comprimento 

# 1 quilometro = 1000 metros
# 1 metro = 100 centrimetros
# 1 centimetro = 10 milimetros
# 1  metro = 39,3701 polegadas
# 1 centimetro =  0,393701


# tabela de conversao massa

# 1 quilograma  = 2,20462 libras

#quilogramas para libras multiplique o valor por 2,205

#centimetro para polegada divide por 2,54
#x = 10
#cent = x #um centimetro
#poleg = 2.54 #polegadas

#cent_to_poleg = (cent / poleg)

#print(cent_to_poleg)

#n = int(input("Digite um valor:"))
#print(f"O numero que vc digitou é: {n}")




#########################################################
cent = 2.54 
quilograma = 2.205
polegada = float(input("Digite o valor em polegadas que deseja converter em centimetros: "))
(convert) = cent*polegada
print(f"{cent} polegadas é igual a {convert} centimetros")

print("\n")

libra = float(input("Agora digite o valor em libras que deseja converter em quilogramas: "))
convert_2 = libra/quilograma
novo_valor = round(convert_2, 2)
print(f"{libra}s é igual a {novo_valor} quilogramas ")#round(valor),2 coloca 2 casas depois do ponto 











