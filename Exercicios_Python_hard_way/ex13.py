### PArametros, descompactação  e variaveis


from sys import argv # importando lib de argumentos do sistema 
import re


script,first,second,third = argv
nome_script = script.split("/",-1)

#print(nome_script[-1])


print("o script que vc chamou é: "+f"{nome_script[-1]}")
print("o script que vc chamou é:",first)
print("o script que vc chamou é:",second)
print("o script que vc chamou é:",third)

#Gostei do resultado , tive que mudar um pouco a saida pois estou usando uma virtual env e a saida com o nome do arquivo ficaria ruim fiz alguns tratamentos e deu certo :D