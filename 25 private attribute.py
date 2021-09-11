## class
class mahasiswa():
    prodi = 'Teknik Geofisika' # variabel public
    __nilai = 0 # variabel private, tidak bisa diakses

    def __init__ (self, inputNama, inputNim):
        self.nama = inputNama
        self.nim = inputNim

    def uts(self, inputNilai):
        self.__nilai += inputNilai
    
    def uas(self, inputNilai):
        self.__nilai += inputNilai
    
    def cekKelulusan(self):
        self.__nilai = self.__nilai / 2
        if self.__nilai < 50:
            print(self.nama + ' dari Teknik Geofisika (' + str(self.nim) + '), dinyatakan tidak lulus.')
        else:
            print(self.nama + ' dengan Geofsika (' + str(self.nim) + '), dinyatakan lulus.')
        
        print('nilai akhir:', self.__nilai)

## main program
iqram = mahasiswa('Iqram Haris Fahromi', 16420057)

iqram.uts(50)
iqram.uas(60)
iqram.cekKelulusan()
