def matriculats(assig,quadri,an):
    """
    retorna el nombre de matriculats per a un aassignatura, quadrimestre, any
    """
    f1 = open('NouFitxer.csv','r')
    c = 0
    for linea in f1:
        linea = linea.strip()
        l = linea.split(';')
        if l[2] == assig:
            if l[3] == an:
                if l[4] == quadri:
                    c = c + 1
    return c
def aprovats(assig,quadri,an):
    """
    retorna el nombre d'aprovats per assignatura, quadrimestre i any
    """
    f1 = open('NouFitxer.csv','r')
    c = 0
    for linea in f1:
        linea = linea.strip()
        l = linea.split(';')
        if l[2] == assig:
            if l[3] == an:
                if l[4] == quadri:
                    if l[5] == 'S':
                        c = c + 1
    return c

def percentatge(assig,quad,an):
    return (aprovats(assig,quad,an)/matriculats(assig,quad,an))*100

def aprovats1a(assig):
    f = open('NouFitxer.csv','r')
    exp = []
    la = []
    c = 0
    ctot = 0
    for linea in f:
        l = linea.split(';')
        if exp != l[1]:
            exp = l[1]
            ctot = ctot + 1
            for e in la:
                if e == 'N':
                    pass
                else:
                    c = c+1
            la = []
        if l[2] == assig:
            la.append(l[5])
    return (c/ctot)*100


        
