 
dizionario = {"nomi dei prodotti":"TV", }                
dizionario["Quantita"]="Disponibile"                    

for key, value in dizionario.items():
    print(key + "-" + value)

for item in dizionario.items():
    print(item)

del dizionario["nomi dei prodotti"]
print(dizionario)
       