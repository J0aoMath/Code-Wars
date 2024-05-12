#Odd March Bits 8 bits
def bit_march(n):
    s = 8-n
    padrão = ''
    liste = []
    padrão += '0' * s
    padrão += '1' * n
    liste.append(padrão)
    for f in range(s):
        f+=1
        temporario = '0'*(s-f)+'1'*n+ '0'*(f)
        liste.append(temporario)
    lista1=[]
    for l in liste:
        lista2=[]
        for c in l:
            lista2.append(int(c))
        lista1.append(lista2)
    return(lista1)
