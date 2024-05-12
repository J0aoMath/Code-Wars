#Your order, Please
def order(sentence):
    lista = []
    ordem = []
    original = []
    aba = ''
    for i in sentence.split():
        for c in i:
            try:
                if int(c) + 0 == int(c):
                    ordem.append(int(c))
                    lista.append(i)   
            except:
                pass
    for i in range(len(lista)):
        original.append('a')
    f=0
    for i in ordem:
        original[i-1] = lista[f]
        f+=1
    for i in original:
        if i == original[len(original)-1]:
            aba += i
        else:
            aba += i + ' '
    return aba
