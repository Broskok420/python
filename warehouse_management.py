warehouse = { "Elettronica": {"Laptop": 10, "Smartphone": 20}, "Abbigliamento": {"Maglietta": 50, "Jeans": 30}, "Cibo": {"Mela": 30, "Pane": 25}}  #CATEGORIE E PRODOTTI

def visualizza_prodotti():
    #PRODOTTI DISPONIBILI DIVISI IN CATEGORIE
    for categoria, prodotti in warehouse.items():
        print(f"Categoria: {categoria}")
        for prodotto, quantita in prodotti.items():
            print(f"  - {prodotto}: {quantita} disponibili")
        print()



def aggiungi_prodotto():
    #AGGIUNGE O AGGIORNA LA QUANTITA DEL PRODOTTO
    categoria = input("Inserisci la categoria del prodotto: ")
    prodotto = input("Inserisci il nome del prodotto: ")
    quantita = int(input("Inserisci la quantità da aggiungere: "))

    if categoria not in warehouse:
        warehouse[categoria] = {}

    if prodotto in warehouse[categoria]:
        warehouse[categoria][prodotto] += quantita
    else:
        warehouse[categoria][prodotto] = quantita

    print(f"Prodotto '{prodotto}' aggiunto/aggiornato con {quantita} unità nella categoria '{categoria}'.")




def rimuovi_prodotto():
    #RIMUOVE UN PRODOTTO DI UNA CATEGORIA SCELTA
    categoria = input("Inserisci la categoria del prodotto da rimuovere: ")
    prodotto = input("Inserisci il nome del prodotto da rimuovere: ")

    if categoria in warehouse and prodotto in warehouse[categoria]:
        del warehouse[categoria][prodotto]
        print(f"Prodotto '{prodotto}' rimosso dalla categoria '{categoria}'.")
    else:
        print("Prodotto non trovato nel magazzino.")




def aggiorna_quantita():
    #MODIFICA QUANTITA DI UN PRODOTTO DI UNA CATEGORIA SCELTA
    categoria = input("Inserisci la categoria del prodotto da aggiornare: ")
    prodotto = input("Inserisci il nome del prodotto da aggiornare: ")
    nuova_quantita = int(input("Inserisci la nuova quantità disponibile: "))

    if categoria in warehouse and prodotto in warehouse[categoria]:
        warehouse[categoria][prodotto] = nuova_quantita
        print(f"La quantità di '{prodotto}' è stata aggiornata a {nuova_quantita}.")
    else:
        print("Prodotto non trovato nel magazzino.")       



def menu():
    print("SELEZIONA UN NUMERO PER CONTINUARE:")
    print("1-VISUALIZZA PRODOTTI")
    print("2-AGGIUNGI PRODOTTI")
    print("3-RIMUOVI PRODOTTI")
    print("4-AGGIORNA QUANTITA PRODOTTI")
    print("5-ESCI")


while True:
    menu()
    scelta = input("SELEZIONA UN NUMERO PER CONTINUARE:")

    if scelta == "5":
        break
    elif scelta == "1":
        print(visualizza_prodotti())
    elif scelta == "2":
        print(aggiungi_prodotto())
    elif scelta == "3":
        print(rimuovi_prodotto())
    elif scelta == "4":
        print(aggiorna_quantita())




