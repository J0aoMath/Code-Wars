#Does my number look big in this?
def narcissistic( value ):
    lista = []
    soma = 0
    for v in str(value):
        lista.append(int(v))
    for l in lista:
        soma += l ** len(lista)
    if soma == value:
        return(True)
    else:
        return(False)
