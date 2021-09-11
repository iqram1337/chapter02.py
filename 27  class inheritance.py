## class inheritance // turunan dari class

class ojek():
    def __init__(self, nama, kendaraan, daerah):
        self.nama = nama
        self.kendaraan = kendaraan
        self.daerah = daerah
    
    def cekBiodata(self):
        print('nama:', self.nama, '\nkendaraan:', self.kendaraan, '\ndaerah:', self.daerah)

class gojek(ojek): # class turunan
    def cekBiodata(self): # mengubah isi fungsi
        print('iqram ganteng')

driver1 = ojek('Iqram', 'Sepeda Motor', 'Bandung Selatan')
driver2 = gojek('Haris', 'Sepeda Motor', 'Palembang')

driver1.cekBiodata()
print('')
driver2.cekBiodata()