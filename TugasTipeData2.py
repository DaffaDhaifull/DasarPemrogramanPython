nilai = [88,75,63,97,82,74,91,80,81,63]

maksimum = max(nilai)
minimum = min(nilai)
rata = sum(nilai) / len(nilai)

nilai.sort(reverse=True)

print("a) Tampilkan data nilai maksimum, minimum, dan nilai rata-rata dari daftar nilai")
print(f"  - maksimum: {maksimum}")
print(f"  - minimum: {minimum}")
print(f"  - rata-rata: {rata}")
print("b) Tampilkan angka terbesar kedua dalam daftar nilai")
print(f"    Nilai terbesar kedua adalah: {nilai[1]}")


lokasi = (
    ("Jakarta", (-6.2088, 106.8456)),
    ("Bandung", (-6.9175, 107.6191)),
    ("Surabaya", (-7.2575, 112.7521))
)

print("Koordinat Bandung:", lokasi[1][1])
print("Jumlah lokasi:", len(lokasi))


nama = input("Input nama teman: ")
nama_teman = nama.split(", ")
print(nama_teman)
print(type(nama_teman))
