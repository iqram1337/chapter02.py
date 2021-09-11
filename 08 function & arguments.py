print(50*"=")
# fungsi dengan menggunakan arguments sederhana
def siswa(nama):
    print("siswa ini bernama,", nama + ".")
siswa('iqram')
print("\n")


print(50*"=")
# fungsi dengan menggunakan keywords arguments
def sekolah(namaGuru, mataPelajaran):
    print("nama guru :", namaGuru)
    print("mengajar  :", mataPelajaran)
sekolah(namaGuru = "iqram haris", mataPelajaran = 'olahraga')
print('')
sekolah(mataPelajaran = 'olahraga', namaGuru = "iqram haris")
print('')
sekolah('olahraga', 'iqram haris') # perhatikan posisi
print('\n')


print(50*"=")
# fungsi dengan menggunakan default arguments
def penjagaSekolah(sifat, nama = 'iqram', shift = 'malam'):
    print("nama  :", nama)
    print("shift :", shift)
    print("sifat :", sifat)
penjagaSekolah('baik')
print('')
penjagaSekolah(nama = 'haris', sifat = 'galak', shift = 'siang')