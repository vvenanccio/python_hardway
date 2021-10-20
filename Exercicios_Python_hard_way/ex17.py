from sys import argv
from os.path import exists
from pynput import keyboard

script, from_file, to_file = argv

print(f"Copiando arquivo {from_file} para {to_file}")

in_file = open("./Templates/"+from_file)

dados = in_file.read()

print(f"O {from_file} arquivo tem {len(dados)} bytes")
path_file = "./Templates/"+to_file
print(path_file)
print(str(exists(path_file)) + " para a existencia do arquivo " + to_file)
print("Certo ... Para continuar precione enter para sair digite esc")



with keyboard.Events() as events:
    var = input()
    for event in events:
        if event.key == keyboard.Key.esc:
            print("Vc pressionou Esc")        
            print("Fechando programa ... até logo")
            in_file.close()
            break
        elif event.key == keyboard.Key.enter:
            print("Vc pressionou Enter")
            out_file = open("./Templates/"+to_file,'w')
            out_file.write(dados)
            print("Pronto, tudo feito")
            out_file.close()
            in_file.close()
            break
        else: 
            print("Algo deu Errado")
            break

