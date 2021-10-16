from sys import argv

# Carregando variaveis 
script, user_name = argv
promp = '>'

#Printando codigo 

print(f'Oi {user_name} , Eu sou o {script} script.')
print("Eu gostaria de fazer algumas perguntas ...")
print(f'Você gosta de mim {user_name} ?')
likes = input(promp)

print(f'Onde vc vive {user_name}?')
lives = input(promp)


print(f'Qual seu computador ?')

computer = input(promp)

print(f"""
Certo, então diga {likes} coisas sobre mim 
Você vive em {lives}. Não sei onde é isso !
E você tem um {computer} computador . Legalll
""")