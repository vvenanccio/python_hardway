from sys import argv
from keyboard import *

script, filename = argv

print(f"Nos vamos apagar o arquivo{filename}")

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            break  # finishing the loop
    except:
        break  # if user pressed a key other than the given key the loop will break

print("Se você não quer isso, digite o comando CTRL + C (ˆC) ")
print("Se vc deseja continuar, precione Enter")
