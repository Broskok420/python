def confronta():
    print("Inserisci numero a:")
    a = int(input())
    print("Inserisci numero b:")
    b = int(input())
    if a>b:
        print("Hai scelto un numero maggiore di A")
        print(1)
    else:
        print("Hai scelto un numero minore di A")
        print(0)
    if a == b:
        print("NON PUOI CARO")
        
confronta()
