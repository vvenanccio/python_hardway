#Ex 16, mudei um pouco esse exercicio add uma lib para identificar comando pressionado no teclado , no ex do livro era somente com uns prints e nem utilizava if ou um loop e nem funções ....

from sys import argv
from pynput import keyboard
import pynput


#class MyException(Exception): 
#    print("Fechando programa")
#

script, filename = argv

#print(f"Nos vamos apagar o arquivo{filename}")
#
#def on_press(key):
#    if key == keyboard.Key.enter:
#        print("Vc pressionou Enter")
#        #print(f"Abrindo o arquivo {filename} ....")
#        #print(open("Templates/"+filename).read())
#        print(f"Esvaziando o arquivo {filename}")
#        var = open(f"Templates/{filename}",'w')
#        var.truncate
#        print(F"Arquivo esvaziado com sucesso{var}")       
#    elif key == keyboard.Key.esc:
#        break
#        print("Vc pressionou Esc")        
#        
#    raise print("Fechando programa ....")


print("Se você deseja deletar o arquivo, Pressione Enter, caso não Pressione Esc")

# The event listener will be running in this block
with keyboard.Events() as events:
    var = input()
    for event in events:
        if event.key == keyboard.Key.esc:
            print("Vc pressionou Esc")        
            print("Fechando programa ... até logo")
            break
        elif event.key == keyboard.Key.enter:
            print("Vc pressionou Enter")
            print(f"Esvaziando o arquivo {filename}")
            var = open(f"Templates/{filename}",'w')
            var.truncate
            print(F"Arquivo esvaziado com sucesso{var}") 
            break
        else: 
            print("Algo deu Errado")
            break




# Escutando os eventos do teclado acontecerem 
#with keyboard.Listener(
#        on_press=on_press) as listener:
#    try:
#        print("Se você deseja deletar o arquivo, Pressione Enter, caso não Pressione Esc")
#        var = input()
#        on_press(var)
#    except MyException as e:
#        print(e)