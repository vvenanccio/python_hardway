def add (a,b):
    print(f"add: {a}+{b}")
    return a + b

soma = add(2,2) 
print(soma)  

def sub(a,b):
    print(f"sub: {a}-{b}")
    return a - b

def multi(a,b):
    print(f"multi: {a}*{b}")
    return a * b

def div (a,b):
    print(f"dev: {a}/{b}")
    return a/b

print("lets do some math wth just functions")

age = add(30,5)
heigth = sub(78,4)
weigth = multi (90,2)
iq = div(100,2)

print(f"Age: {age}, Heigth:{heigth}, Weigth:{weigth}, Iq{iq}")

# adivinhe 

print("adivinhe")

what = add(age,sub(heigth,multi(weigth,div(iq,2))))

print(what)
