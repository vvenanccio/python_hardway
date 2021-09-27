car = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = car - drivers
print(cars_not_driven)
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
print(carpool_capacity)
media_avarage_passagers_per_car = passengers / cars_driven
print(media_avarage_passagers_per_car)
caroppl=0
#Simulando erro do Exercicio 
carpool = caroppl - passengers

#Traceback (most recent call last):
#  File "/Users/vinicius/Documents/Dev/Projects/Pj001/python_hard_way/ex04.py", line 13, in <module>
#    carpool = caroppl - passengers
#NameError: name 'caroppl' is not defined

# Isso acontece pq a variavel caroppl não foi definida 

# 1 se mudar de 4 para 4.0 o python entende que os valores terão ponto flutuante 

