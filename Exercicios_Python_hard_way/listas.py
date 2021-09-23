from icecream import ic


minha_lista = [8,4,True,1,0]


# Ordenação menor para o maior 
ic(minha_lista)
minha_lista.sort()
ic(minha_lista)


#Imprimindo o tipo da lista

print(type(minha_lista))

#Adicionando um elemento na lista
a=1
minha_lista.append(a+1)
print(minha_lista)
minha_lista.append(a+1)
print(minha_lista)

#Adcionar varios elementos a uma lista

minha_lista.extend([1,2,3,4,45])
print(minha_lista)

# Mostrar posicão primeira aparição de um valor 
meses = ["Janeiro", "Fevereiro", "Março", "Abril"]
print(meses.index("Março"))


# Entendendo uma lista de caracteres

print("\n")


meu_nome = "Vinicius"
print(meu_nome[1])

print(type(meu_nome))

print(meu_nome[::-1])

nova_frase = "Vinicius Venancio"
def invert (nome):
    return nome[::-1]

TXT=invert(nova_frase)
ic(TXT)





    

