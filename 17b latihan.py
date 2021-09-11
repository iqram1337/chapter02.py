print("Database Teknik Geofisika 2020".center(90, '='))

def mahasiswa(mhsx):
    mhs1 = {'Nama': 'Iqram Haris Fahromi', 'NIM': 16420057, 'Prodi': 'Teknik Geofisika'}
    mhs2 = {'Nama': 'Arif Nur Rohman', 'NIM': 16420097, 'Prodi': 'Teknik Geofisika'}
    mhs3 = {'Nama': 'Abisha Caesaruli M Simanjuntak', 'NIM': 16420006, 'Prodi': 'Teknik Geofisika'}
    mhs4 = {'Nama': 'Muhammad Zaky Ramadhani', 'NIM': 16420007, 'Prodi': 'Teknik Geofisika'}
    mhs5 = {'Nama': 'Nadya Cindy Putri', 'NIM': 16420012, 'Prodi': 'Teknik Geofisika'}
    mhs6 = {'Nama': 'Moh. Ubaidillah Arisahbana', 'NIM': 16420018, 'Prodi': 'Teknik Geofisika'}
    mhs7 = {'Nama': 'Tsamrotul Jannah', 'NIM': 16420022, 'Prodi': 'Teknik Geofisika'}
    mhs8 = {'Nama': 'Nur Iksannurdin Fitranto S', 'NIM': 16420027, 'Prodi': 'Teknik Geofisika'}

    data_base = {16420057: mhs1, 16420097: mhs2, 16420006: mhs3, 16420007: mhs4, 16420012: mhs5, 
    16420018: mhs6, 16420022: mhs7, 16420027: mhs8}

    return  data_base[mhsx]

nimx = int(input('Masukkan NIM Mahasiswa: '))
mhsx = mahasiswa(nimx)
# print(mhsx)
# print(type(mhsx))

print(90*"-")
for nama, datanya in mhsx.items():
    print(nama.ljust(5), ':', datanya)