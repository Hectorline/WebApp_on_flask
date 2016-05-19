def naprovats(assig,intent,curs=0,quad=0):
    """
    retorna el num d'estudiants que han aprovat la assignatura assig a la 'intent' el curs i quad
    """
    f1 = open('Fitxermegaultimdefinitiu.csv','r')
    c = 0
    for linea in f1:
        linea = linea.strip()
        l = linea.split(';')
        if len(l) < 44:
            pass
        elif l.count(assig) == intent:
                c = c+1
    return c
