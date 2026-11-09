# Nama: Daffa Dhaifullah
# Nim: 2600821
# kelas 1C

# Latihan 1, no 1
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        a, b = b,a + b
jumlah = int(input("Masukan jumlah deret fibboncci: "))
fibonacci(jumlah)



# latihan 1, no 2
def volume_tabung(r,t):
    volume = 22/7*r*r*t
    return volume
print(volume_tabung(7,10))



# latihan 1, no 3
input_angka = []

jumlah_angka = int(input("Masukan jumlah angka yang akan dimasukan: "))
for i in range(jumlah_angka):
    input_angka.append(int(input(f"Masukan angka ke-{i+1}: ")))

def nilai_total(*angka):
    total = sum(angka)
    return total

def nilai_rata2(*angka):
    jumlah_angka = len(angka)
    rata2 = nilai_total(*input_angka) / jumlah_angka
    return rata2

print("Total: ",nilai_total(*input_angka))
print("Rata-rata: ",nilai_rata2(*input_angka))



# latihan 2
jkesempatan = 3
def kesempatan(password):
    if password == "Latihan":
        return True
    else:
        return False

while jkesempatan > 0:
    username = input("Username: ")
    password = kesempatan(input("Password: "))
    if not password:
        print("Password salah")
        jkesempatan -= 1
        if jkesempatan > 0:
            print(f"sisa kesempatan login {jkesempatan}x lagi")
    else:
        print("LOGIN BERHASIL")
        break
else:
    print("Kesempatan login HABIS")



# latihan 3
def konversi_detik(jam, menit, detik):
    return (jam * 3600) + (menit * 60) + detik

def selisih(jMulai, mMulai, dMulai, jSelesai, mSelesai, dSelesai):
    tDetikMulai = konversi_detik(jMulai,mMulai,dMulai)
    tDetikSelesai = konversi_detik(jSelesai,mSelesai,dSelesai)
    selisih = tDetikSelesai - tDetikMulai

    jam = selisih // 3600
    sisa = selisih % 3600
    menit = sisa // 60
    detik = sisa % 60

    return jam, menit, detik

jMulai = int(input("Masukan Jam Mulai: "))
mMulai = int(input("Masukan Menit Mulai: "))
dMulai = int(input("Masukan Detik Mulai: "))

jSelesai = int(input("Masukan Jam Selesai: "))
mSelesai = int(input("Masukan Menit Selesai: "))
dSelesai = int(input("Masukan Detik Selesai: "))

selisih_jam, selisih_menit, selisih_detik = selisih(jMulai,mMulai,dMulai,jSelesai,mSelesai,dSelesai)
print(f"{selisih_jam} jam - {selisih_menit} menit - {selisih_detik} detik")