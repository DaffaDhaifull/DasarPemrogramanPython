# Nama: Daffa Dhaifullah
# NIM 2600821

# LATIHAN-1
numbers = [10, 20, 20, 30, 40, 50, 50, 60]

unique_numbers = list(set(numbers))
unique_numbers.sort()

print(numbers)
print(unique_numbers)



# LATIHAN-2
students = {
    "Alice" : "Computer science",
    "Bob" : "Mathematics",
    "Charlie" : "Physics",
    "David" : "Computer science",
    "Eva" : "Mathematics"
}

jumlah_per_jurusan = {}

for jurusan in students.values():
    jurusan_lower = jurusan.lower()

    if jurusan_lower in jumlah_per_jurusan:
        jumlah_per_jurusan[jurusan_lower] += 1
    else:
        jumlah_per_jurusan[jurusan_lower] = 1

user_input = input("Masukkan nama prodi yang dicari: ").lower()

if user_input in jumlah_per_jurusan:
    print(f"prodi {user_input} sebanyak {jumlah_per_jurusan[user_input]}")
else:
    print(f"prodi {user_input} tidak ditemukan")



# LATIHAN-3
student_info= {
    "Alice": {"age": 20, "major": "Computer Science"},
    "Bob": {"age": 21, "major": "Mathematics"},
    "Charlie": {"age": 19, "major": "Physics"}
}

cari = input("Masukan nama siswa untuk mencari infromasi: ")
if cari in student_info:
    print(f"Umur {cari} adalah {student_info.get(cari).get("age")} dan Prodi nya adalah {student_info.get(cari).get("major")}")
else:
    print(f"Nama {cari} Tidak ditemukan")