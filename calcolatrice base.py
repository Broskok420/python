from math import sqrt


def somma():
    print("Somma\n")

    print("Inserisci il valore di a:\t")

    a = int(input())

    print("Inserisci il valore di b:\t")

    b = int(input())

    print(f"Risultato della somma:\t {a+b}")
    
somma()

    
    
def sottrazione():
    print("Sottrai\n")

    print("Inserisci il valore di a:\t")

    a = int(input())

    print("Inserisci il valore di b:\t")

    b = int(input())

    print(f"Risultato della sottrazione:\t {a-b}")
    
sottrazione()



def moltiplicazione():
    print("Moltiplica\n")

    print("Inserisci il valore di a:\t")

    a = int(input())

    print("Inserisci il valore di b:\t")

    b = int(input())

    print(f"Risultato della moltiplicazione:\t {a*b}")
    
moltiplicazione()



def divisione():
    print("Dividi\n")

    print("Inserisci il valore di a:\t")

    a = int(input())

    print("Inserisci il valore di b:\t")

    b = int(input())
    
    if b == 0:
        print("NOPE")
    else:
        print(f"Risultato della divisione:\t {a/b}")
    
divisione()


numero = float(input("Inserisci un numero:"))
risultato = sqrt(numero)
print(f"La radice quadrata di{numero} è {risultato}")




   


