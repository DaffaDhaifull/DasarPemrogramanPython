# Nama: Daffa Dhaifullah
# NIM: 2600821


for x in range(1,50+1):
    if x %5 == 0:
        print("Pass")
    else:
        print(x)


n = int(input("Masukkan jumlah hewan yang akan diinput: "))
namaHewan = []
a=0
for x in range(n):
    namaHewan.append( input(f"Masukan Hewan ke-{x+1}: "))
for i in namaHewan:
    a += 1
    print(f"Hewan ke-{a} adalah: {i}")


n = int(input("Masukan jumlah input yang diinginkan: "))
bil = []
for x in range(n):
    bil.append(int(input(f"Bilangan ke-{x+1}: ")))
for i in bil:
    if(i %2 == 0):
        print(f"Bilangan {i} adalah genap")
    else:
        print(f"Bilangan {i} adalah ganjil")


for i in range(1,80+1):
    if (i %3==0 and i %5==0):
        print(i)

while True:
    username = input("Masukan Username anda ... ")
    password = input("Masukan Password anda ... ")
    if (username == "dasproRPL" and password == "RPLfire!123"):
        print("Login Berhasil")
        break
    else:
        print("Username atau password salah")

    