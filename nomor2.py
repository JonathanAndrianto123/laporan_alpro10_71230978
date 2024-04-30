list = []
while True :
    angka = input("masukkan angka = ")
    if angka.lower() == "done" :
        break
    else :
        list.append(angka)

maks = max(list)
min = min(list)
print(f"nilai maksimal dari deretan angka yang dimasukkan adalah {maks}")
print(f"nilai minimal dari deretan angka yang dimasukkan adalah {min}")