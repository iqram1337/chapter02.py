print("Membuat Fungsi".center(50, "="))

# membuat fungsi
def fungsi():
    print("test 123")
fungsi() # memanggil fungsi
fungsi()
fungsi()
print('\n')


print("Latihan Fungsi".center(50, "="))

def hitungayam(x):
    hargaAyam = 20000

    akhir = x*hargaAyam
    return akhir

hargaAyam = 20000
print(f"harga ayam per 1 kg = {hargaAyam}")

x = int(input("masukkan banyak ayam (kg) = "))
akhir = hitungayam(x)
print(f"harga bayar = Rp.{akhir:,}")