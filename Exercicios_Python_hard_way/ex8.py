formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("um", "dois","tres","quatro"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
    "Try your",
    "own text here",
    "Maybe a poem",
    "meu pastel"# se passar menos ou mais argumentos ta ruim 
))
