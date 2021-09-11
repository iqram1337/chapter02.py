## menggunakan __init__()
# class
class mahasiswa():

    def __init__(self, inputNama, inputNim):
        self.nama = inputNama
        self.nim = inputNim

    def belajar(self, kondisi):
        print(self.nama, "dengan NIM", self.nim, "sedang belajar", kondisi)
    
    def tidur(self):
        print(self.nama, "sedang tidur")
# batas class

# main program
iqram = mahasiswa('Iqram Haris Fahromi', 16420057)
print(iqram.nama)
print(iqram.nim)
iqram.belajar('dengan giat')
print('')

iqbal = mahasiswa('Iqbal Hafiz Fahromi', 16420041)
print(iqbal.nama)