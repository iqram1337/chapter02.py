# contoh scope local
print("Scope Local".center(50, "="))
namaKucing = 'kattie' # scope global
print(f"nama kucing awal = {namaKucing}")

def ubahNamaKucing(namaBaru):
    namaKucing = namaBaru # scope local
    print(f"nama kucing diubah = {namaKucing}")

ubahNamaKucing('garry')
print(f"nama kucing akhir = {namaKucing}")
print('\n')


# contoh scope global
print("Scope Global".center(50, "="))
namaKelinci = 'momon' # scope global
print(f"nama kelinci awal = {namaKelinci}")

def ubahNamaKelinci(namaBaru):
    global namaKelinci # pemanggilan variabel di scope global 
    namaKelinci = namaBaru # scope global
    print(f"nama kelinci diubah = {namaKelinci}")

ubahNamaKelinci('kasparov')
print(f"nama kelinci akhir = {namaKelinci}")
