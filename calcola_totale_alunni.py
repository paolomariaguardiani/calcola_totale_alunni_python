import os
from datetime import date

# thanks to: https://docs.python.org/3/library/datetime.html
data_odierna = date.today()  # Mi servirà per creare il titolo del file txt

numero_giorno_settimana = data_odierna.weekday()

lista_giorni_settimana = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "venerdì", "Sabato", "Domenica"]
giorno_della_settimana = lista_giorni_settimana[numero_giorno_settimana]


dati_percorso_lettura = ""
with open('dati_percorso_lettura.txt', "r") as file:
    # readline legge solo la prima riga così al di sotto di essa puoi scrivere istruzioni
    # readlines legge tutte le linee di testo del file txt
    dati_percorso_lettura = file.readline().strip()  # .strip() è importantissimo per eliminare \n dalla prima riga

dati_percorso_scrittura = ""
with open('dati_percorso_scrittura.txt', "r") as file:
    # readline legge solo la prima riga così al di sotto di essa puoi scrivere istruzioni
    # readlines legge tutte le linee di testo del file txt
    dati_percorso_scrittura = file.readline().strip()  # .strip() è importantissimo per eliminare \n dalle linee


# Scrivo in una lista tutti i files xlsx presenti in una cartella come stringhe
# Thanks to: https://youtu.be/t4va-o5mcBs
# FOLDER_PATH_FILES_EXCEL = r'C:\\Salvataggi'  # Attenzione ci vogliono 2 backslash in Windows!
# fileNames = os.listdir(FOLDER_PATH_FILES_EXCEL)
fileNames = os.listdir(dati_percorso_lettura)

lista_files_xlsx = []
for file in fileNames:
    if file.endswith("xlsx"):
        lista_files_xlsx.append(file)


def estrai_numero(text):
    numero = text[55:]  # raccolgo i dati dal numero in poi
    numero = numero.replace(".xlsx", "")  # elimino il testo ".xlsx"
    int_numero = int(numero)
    return int_numero

lista_classi = ["1A", "1B", "2A", "2B", "3A", "3B", "4A", "4B", "5A", "5B", "M1", "M2", "M3"]
lista_numeri_alunni = []

if len(lista_files_xlsx) == 13:
    for file in lista_files_xlsx:
        numero = estrai_numero(file)
        lista_numeri_alunni.append(numero)

# def ricava_totale_alunni(lista):
#     totale = 0
#     for num in lista:
#         totale += num
#     return totale

lista_generale_alunni = []
if len(lista_files_xlsx) == 13:
    for i in range(13):
        lista_generale_alunni.append(f"Classe {lista_classi[i]}: {lista_numeri_alunni[i]:>10}")
    
# totale_generale_alunni = ricava_totale_alunni(lista_numeri_alunni)
totale_generale_alunni = sum(lista_numeri_alunni)
lista_generale_alunni.append(f"{'---':>21}")
lista_generale_alunni.append(f"Totale alunni: {totale_generale_alunni:>6}")


schema_mensa_turno_01 = []
schema_salone_turno_01 = []
schema_mensa_turno_02 = []
schema_salone_turno_02 = []

lista_classi_mensa_01 = []
lista_classi_salone_01 = []
lista_classi_mensa_02 = []
lista_classi_salone_02 = []


# Thanks to: https://docs.vultr.com/python/examples/read-a-file-line-by-line-into-a-list
if numero_giorno_settimana < 5:  # 5 corrisponde a sabato
    with open(f"dati/{numero_giorno_settimana}_mensa_01.txt") as file:
        schema_mensa_turno_01 = [line.strip() for line in file.readlines()]

    with open(f"dati/{numero_giorno_settimana}_salone_01.txt") as file:
        schema_salone_turno_01 = [line.strip() for line in file.readlines()]

    with open(f"dati/{numero_giorno_settimana}_mensa_02.txt") as file:
        schema_mensa_turno_02 = [line.strip() for line in file.readlines()]

    with open(f"dati/{numero_giorno_settimana}_salone_02.txt") as file:
        schema_salone_turno_02 = [line.strip() for line in file.readlines()]


lista_numeri_mensa_01 = []
lista_numeri_salone_01 = []
lista_numeri_mensa_02 = []
lista_numeri_salone_02 = []

# trovo il numero alunni per mensa piccola e salone
for i in schema_mensa_turno_01:
    for elemento in lista_files_xlsx:
        if i in elemento:
            lista_numeri_mensa_01.append(estrai_numero(elemento))

for i in schema_salone_turno_01:
    for elemento in lista_files_xlsx:
        if i in elemento:
            lista_numeri_salone_01.append(estrai_numero(elemento))

for i in schema_mensa_turno_02:
    for elemento in lista_files_xlsx:
        if i in elemento:
            lista_numeri_mensa_02.append(estrai_numero(elemento))

for i in schema_salone_turno_02:
    for elemento in lista_files_xlsx:
        if i in elemento:
            lista_numeri_salone_02.append(estrai_numero(elemento))



totale_mensa_01 = sum(lista_numeri_mensa_01)
totale_salone_01 = sum(lista_numeri_salone_01)
totale_mensa_02 = sum(lista_numeri_mensa_02)
totale_salone_02 = sum(lista_numeri_salone_02)


# Per l'allineamento del testo a destra: Thanks to https://www.geeksforgeeks.org/python/string-alignment-in-python-f-string/

lista_mensa_turno_01 = []
for i in range(len(schema_mensa_turno_01)):
    lista_mensa_turno_01.append(f"Classe {schema_mensa_turno_01[i]}: {lista_numeri_mensa_01[i]:>10}")
lista_mensa_turno_01.append(f"{'---':>21}")
lista_mensa_turno_01.append(f"Totale: {sum(lista_numeri_mensa_01):>13}")

lista_salone_turno_01 = []
for i in range(len(schema_salone_turno_01)):
    lista_salone_turno_01.append(f"Classe {schema_salone_turno_01[i]}: {lista_numeri_salone_01[i]:>10}")
lista_salone_turno_01.append(f"{'---':>21}")
lista_salone_turno_01.append(f"Totale: {sum(lista_numeri_salone_01):>13}")

lista_mensa_turno_02 = []
for i in range(len(schema_mensa_turno_02)):
    lista_mensa_turno_02.append(f"Classe {schema_mensa_turno_02[i]}: {lista_numeri_mensa_02[i]:>10}")
lista_mensa_turno_02.append(f"{'---':>21}")
lista_mensa_turno_02.append(f"Totale: {sum(lista_numeri_mensa_02):>13}")

lista_salone_turno_02 = []
for i in range(len(schema_salone_turno_02)):
    lista_salone_turno_02.append(f"Classe {schema_salone_turno_02[i]}: {lista_numeri_salone_02[i]:>10}")
lista_salone_turno_02.append(f"{'---':>21}")
lista_salone_turno_02.append(f"Totale: {sum(lista_numeri_salone_02):>13}")

### Messaggio di benvenuto ###
print(f"\n\n\nBuongiono, oggi è {giorno_della_settimana} - {data_odierna}\n")
print("Grazie per aver utilizzato il programma 'Calcola Totale Alunni' realizzato in Python!\n")

### Scrivo il file ###
# Thanks to google
nome_file = f"{data_odierna} - calcolo del totale degli alunni.txt"
testo_pagina = []

testo_data = f"Data odierna: {data_odierna} - {giorno_della_settimana}"
testo_pagina.append(testo_data)

testo_di_spiegazione_lista_alunni = "\n\nEcco il totale degli alunni che si fermano a mensa oggi:"
testo_pagina.append(testo_di_spiegazione_lista_alunni)
testo_pagina.extend(lista_generale_alunni)

testo_mensa_piccola_primo_turno = "\n\nMENSA PICCOLA - primo turno"
testo_pagina.append(testo_mensa_piccola_primo_turno)
testo_pagina.extend(lista_mensa_turno_01)

testo_salone_primo_turno = "\n\nSALONE - primo turno"
testo_pagina.append(testo_salone_primo_turno)
testo_pagina.extend(lista_salone_turno_01)


testo_mensa_piccola_secondo_turno = "\n\nMENSA PICCOLA - secondo turno"
testo_pagina.append(testo_mensa_piccola_secondo_turno)
testo_pagina.extend(lista_mensa_turno_02)

testo_salone_secondo_turno = "\n\nSALONE - secondo turno"
testo_pagina.append(testo_salone_secondo_turno)
testo_pagina.extend(lista_salone_turno_02)


try:
    with open(f"{dati_percorso_scrittura}{nome_file}", "w") as file:
        for elemento in testo_pagina:
            file.write(str(elemento) + '\n')
        print(f"Il testo è stato scritto nel file '{nome_file}'\n\n")
except Exception as e:
    print(f"Si è verificato un errore {e}")


# Questa riga di testo permette di mantenere la shell sullo schermo
# E di far chiudere il programma dopo la pressione di tasto
tasto_premuto = input("Premere Invio per terminare il programma")