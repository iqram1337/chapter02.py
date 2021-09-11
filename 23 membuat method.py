## class
class mahasiswa():
    nama = 'x'

    def belajar(self, kondisi):
        print(self.nama, 'sedang belajar', kondisi)
    
    def tidur(self):
        print(self.nama, 'sedang tidur')


## main program
iqram = mahasiswa()
iqbal = mahasiswa()

iqram.nama = "Iqram Haris Fahromi"
iqbal.nama = "Iqbal Hafiz Fahromi"

iqram.belajar('dengan giat sekali') # print
iqbal.tidur() # print