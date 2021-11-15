def break_works(stuff):
    """Está funcao ira dividir palavras"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Ordenar as palavras"""
    return sorted(words)

def print_first_word(words):
    """imprimi a primeira palavra depois de tirar do conjunto de palavras """
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """imprime a ulta palavra depois de tirar do conjunto de palavras"""
    word = words.pop(-1)
    print(word)

def sort_setence(setence):
    """Recebe uma frase completa e retorna as palavras ordenadas"""
    words = break_works(setence)
    return sort_words(words)

def print_first_and_last(setence):
    """Imprime a primeira e a ultima palavra de uma frase """
    words = break_works(setence)
    print_first_and_last(words)
    print_last_word(words)

def print_first_and_last(setence):
    """Ordena e entao imprime a primeira e a ultima """
    words=sort_words(setence)
    print_last_word(words)
    print_last_word(words)
    