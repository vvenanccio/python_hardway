tipos_de_pessoa = 10

x = f"Existem {tipos_de_pessoa} tipos de pessoa"

print(x)

binario = "binario"
nao_e = "nao é "
y = f" Those who know {binario} and those who {nao_e}."
print(y)


print(f"I said: {x}")
print(f"E depois eu disse {y}")

muito_engracado = False
evolucao_da_piada = "Isso nao é tao engraçado ?{}"

print(evolucao_da_piada.format(muito_engracado))


# Concate de strings

w = "isso é do lado esquerdo"
e = "isso é do lado direito "

print( w + e)