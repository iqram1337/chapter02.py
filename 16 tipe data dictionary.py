# dictionary
# contoh = {key1: value1, key2: value2, key3: value3}
"""
list = [1, 2, 3]
tuple = (1, 2, 3)
set = {1, 2, 3}
"""
print("IDENTITAS MAHASISWA".center(80, "="))
mhs1 = {"Nama": 'Iqram',
        "NIM": 1620057,
        "Prodi": 'Teknik Geofisika'}
mhs2 = {"Nama": 'Hafizh',
        "NIM": 16420001,
        "Prodi": 'Teknik Perminyakan'}

data = {16420057: mhs1, 16420001: mhs2}

print("Data1  =", mhs1)
print("Tipe   =", type(mhs1))
print(mhs1["Prodi"]) # memanggil value dengan keys
# print("Keys   =", mhs1.keys()) # melihat keys
# print("Values =", mhs1.values()) # melihat nilai dari keys
# print("Items  =", mhs1.items()) # melihat keys secara keseluruhan
print(type(data))
print('\n')

nimx = int(input("Masukkan NIM Mahaiswa: "))
print(data[nimx])

for i in data[nimx]:
     print(i.ljust(6) + '  :', data[nimx][i])
     i=+1