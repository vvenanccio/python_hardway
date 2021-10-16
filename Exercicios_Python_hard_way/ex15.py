from sys import argv

script, filename = argv

txt = open(f"Templates/{filename}")

print(txt.read())

print("Digite o nome do arquivo de novo")

file_again = input("> ")

txt_again = open(f"Templates/{file_again}")

print(txt_again.read())

txt.close()
txt_again.close()
