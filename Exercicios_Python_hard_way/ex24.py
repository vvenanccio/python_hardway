print("Vamos praticr mais")
print('vc\'deveria precisa saber\'sobre os scapes com \\ :')
print( '\n novas linhas and \t tab.')
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love nor comprehend passion from intituition 
and requires an explanation
\n\t\twhere the is none.
"""

print("-----------------")
print(poem)
print("-----------------")

five = 10 - 2 + 3 - 6

print(f"this should be five : {five}")

def secret_formula (started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans,jars,crates

start_point = 10000
beans,jars,crates = secret_formula(start_point)

### lembre-se de que essa é outra maneira de formatar uma string

print("com o stating point :{}".format(start_point))
# é como usar o f 

print(f"nos nao temos {beans}feijoes, {jars}, e {crates} crates.")

