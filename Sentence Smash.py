#Sentence Smash
def smash(words):
    lista = ''
    for n in range(len(words)):
        if n+1 == len(words):
            lista += words[n]
        else:
            lista += words[n]+' '
    return lista
