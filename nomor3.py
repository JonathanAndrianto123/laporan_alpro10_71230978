with open ("file.txt","r") as file :
    konten = file.read()
    konten_pisah = konten.split(".")
    unik = []

    for kat in konten_pisah :
        kata = kat.strip().split()
        for k in kata :
            k = k.strip("!@#$%^&*.,?/';:()").lower()
            if k not in unik :
                unik.append(k)

print("=============ISI BERITA==============")
print(konten)

print("=============KATA UNIK===============")
print(unik)
