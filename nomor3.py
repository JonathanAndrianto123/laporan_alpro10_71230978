with open ("file.txt","r") as file :
    konten = file.read()
    konten_pisah = konten.split(".")
    unik = []

    for x in konten_pisah :
        kata = x.strip().split()
        for y in kata :
            y = y.strip("!@#$%^&*.,?/';:()").lower()
            if y not in unik :
                unik.append(y)

print("=============ISI BERITA==============")
print(konten)

print("=============KATA UNIK===============")
print(unik)
