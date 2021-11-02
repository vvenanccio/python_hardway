from sys import argv

script, input_file = argv

#funcao que le o todo o arquivo e printa na tela seu resultado
def print_all(f):
    print(f.read())

#O método de arquivo Python seek () define a posição atual do arquivo no deslocamento. 
# O argumento whence é opcional e o padrão é 0, o que significa posicionamento absoluto do arquivo, 
# outros valores são 1 que significa busca em relação à posição atual e 2 significa busca em relação ao 
# final do arquivo.


def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print(line_count,f.readline(),end="")

current_file = open(input_file)
print("First let's print the whole file: \n")

print_all(current_file)
rewind(current_file)

print("now let's rewind, kind of like a tape")
rewind(current_file)

print("let's print three lines")
current_line = 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
