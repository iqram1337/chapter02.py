## class
class mahasiswa():
    jurusan = 'Teknik Geofisika' # variabel di dalam class
    jumlahMahasiswa = 0       # public

    def __init__(self, inputNama, inputNim):
        self.nama = inputNama # public
        self.nim = inputNim   # public
        mahasiswa.jumlahMahasiswa += 1

## main program

# mahasiswanya
iqram = mahasiswa('Iqram Haris Fahromi', 16420057)
ucup = mahasiswa(inputNim = 16420057, inputNama = 'Michael Ucup')
otong = mahasiswa('Otong Surotong', 16420023)

# print atau output
print('Nama'.ljust(9) + ':', ucup.nama)
print('jurusan'.ljust(9) + ':', ucup.jurusan)
print('Jumlah Mahasiswa: ', mahasiswa.jumlahMahasiswa)

ucup.jurusan = 'Teknik Perminyakan' # mengubah jurusan ucup
print('jurusan'.ljust(9) + ':', ucup.jurusan)
print(ucup.__dict__) # melihat data dari ucup
