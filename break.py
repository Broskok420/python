def somma_a():
    a=1
    while a :
        print(a+a)

        print ('Inserisci numero:')

        a = int(input())

        if (a==0):
            print("Fine programma")
            break
            
        a+=a
somma_a()
