print("More On List".center(50, "="))
barang = ['motor', 'mobil', 'dompet']
print('barang =', barang)

## beberapa method yang bisa digunakan untuk memanipulasi list
# menambah data ke dalam list
barang.append('sepeda')
print('barang =', barang)

barang.extend('ban')
print('barang =', barang)

barang.insert(0, 'sepeda')
print('barang =', barang)


# menghitung anggota
jumlahSepeda = barang.count('sepeda')
print('banyak sepeda =', jumlahSepeda)


# menghapus data
barang.remove('sepeda')
print('barang =', barang)


# mereverse data
barang.reverse()
print('barang =', barang)
print('\n')


# menduplicate barang ke variabel baru
stuff = barang.copy()
stuff.insert(0, 'gelas')
print('barang =', barang)
print('stuff  =', stuff)
