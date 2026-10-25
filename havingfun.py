from random import *
from math import *
media = []
numero = float(input("inserisci un numero, esso può essere: decimale, reale, intero, etc..."))
velocita = 2
peso = uniform(-10,10)
dataset = (
    [2, 4],[1, 2],[6, 12],[3, 6],[4.5, 9],[15, 30],[7.1, 14.2],[8, 16]
)
for i in range(5000):
    errore = 0
    for x,y in dataset:
        peso *= x / y 
        previsione = peso * (velocita**numero) + velocita
        previsione = previsione**numero


        risultato = numero * (y/x)


        errore = previsione - risultato
        
        if errore < numero:
            previsione = previsione+errore
            print(previsione)
            media.append(previsione)
            
        else:
            previsione = previsione-errore
            print(previsione)
            media.append(previsione)

for l in range(int(len(media)) -1):
    a = media[l] + media[l + 1]
    print(a)

