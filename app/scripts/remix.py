def remix():
    """
    crea un nou fitxer amb una linea per alumne
    """
    c = 0
    f1 = open('NouFitxer.csv','r')
    f2 = open('Fitxermegaultimdefinitiu.csv', 'w')
    exp = ''
    s = ''
    c = 0
    for linea in f1:
        linea = linea.strip()
        l = linea.split(';')
        if l[1] == str(exp):
            for paraula in l[2:8]:
                s = s + paraula + ';'
        else:
            exp = l[1]
            f2.write(s[0:-1]+'\n')
            print(s[0:-1])
            s = l[0] +';'+l[1]+';'+l[8]+';'+l[9]+';'+l[2]+';'+l[3]+';'+l[4]+';'+l[5]+';'+l[6]+';'+l[7]+';'
    f1.close()
    f2.close()
remix()
            
