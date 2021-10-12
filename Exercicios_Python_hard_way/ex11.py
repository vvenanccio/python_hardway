### trabalhando com inputs

print("Qual seu nome ? ")# veja a diferença na saida do print que tinha end  na linha 7 

nome = input()
print("Quantos anos vc tem ", end="")# lembrando que o end vai para a liinha de baixo no terminal 

age = input()

resposta = "Sua idade é: "
print(resposta,str(age))#convertendo em string a idade para poder juntar aqui 
print("\n")
print("Printando diferente")

print(resposta + str(age))

print("Mas o resulta vai ser o mesmo")

print(f"Seu nome é {nome}, e sua idade é {age}")# nao esquece do f de format para formatar as string da sequencia 
