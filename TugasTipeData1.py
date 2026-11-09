import math

peserta = int(input("Masukan jumlah peserta: "))
biayaSewaTmpt = int(input("Masukan biaya sewa tempat: "))
biayaDokumentasi = int(input("Masukan biaya dokumentasi: "))
hrgKonsumsi = int(35000)
cdgKonsumsi = float(peserta * 0.1)
jmlKonsumsi = peserta + cdgKonsumsi 
totBiayaKonsumsi = jmlKonsumsi * hrgKonsumsi   

isiRimKertas = int(500)
hrgRimKertas = int(65000)
cdgSertif = peserta * 0.05
jmlSetif = peserta + cdgSertif 
jmlKertas = jmlSetif
jmlRim = math.ceil(jmlKertas / isiRimKertas)
totBiayaKertas = jmlRim * hrgRimKertas

totBiayaAcara = totBiayaKonsumsi + totBiayaKertas + biayaSewaTmpt + biayaDokumentasi
cdgDanaAcara = totBiayaAcara * 0.1
danaYgHrsTerkumpul = totBiayaAcara + cdgDanaAcara
biayaPendaftaran = danaYgHrsTerkumpul / peserta


print("A. PERHITUNGAN BIAYA KONSUMSI")
print(f"\t- Jumlah konsumsi yang harus disediakan, termasuk 10% cadangan: {int(jmlKonsumsi)} porsi")
print(f"\t- Total biaya konsumsi: Rp.{int(totBiayaKonsumsi)}")
print("B. BIAYA CETAK SERTIFIKAT")
print(f"\t- Jumlah sertifikat yang perlu dicetak: {int(jmlSetif)} sertifikat (termasuk 5% cadangan)")
print(f"\t- Jumlah lembar kertas yang dibutuhkan: {int(jmlKertas)} kertas")
print(f"\t- Perkiraan jumlah rim kertas yang diperlukan: {jmlRim}")
print(f"\t- Total biaya pembelian kertas: Rp.{totBiayaKertas}")
print("C. PERHITUNGAN BIAYA PENDAFTARAN PESERTA")
print(f"\t- Biaya konsumsi: Rp.{totBiayaKonsumsi}")
print(f"\t- Biaya cetak sertifikat: Rp.{totBiayaKertas}")
print(f"\t- Biaya sewa tempat: Rp.{biayaSewaTmpt}")
print(f"\t- Biaya dokumentasi: Rp.{biayaDokumentasi}")
print("=================================================================================================")
print(f"\t- Total biaya penyelenggaraan acara: Rp.{totBiayaAcara}")
print(f"\t- Besar dana cadangan: Rp.{cdgDanaAcara}")
print(f"\t- Total dana yang harus dikumpulkan: Rp.{totBiayaAcara + cdgDanaAcara}")
print(f"\t- Biaya pendaftaran peserta: Rp.{biayaPendaftaran}")
print("=================================================================================================")