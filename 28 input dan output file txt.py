## input dan output file

"""
w = write mode / mode menulis dan menghapus file lama,
    jika tidak ada file maka akan dibuat file baru.
r = read mode only / hanya bisa baca
a = appending mode / dapat menambahkan data di akhir baris
r+ = write and read mode
"""

# membuat file text
file = open('fTest.txt', 'w')
file.write('file text ini dibuat dengan menggunakan python')
file.write('\nini baris kedua')
file.write('\nini baris ketiga')
file.write('\nini baris keempat')
file.close()


# membaca file text
file = open('fTest.txt', 'r')
print(file.read())

#print(file.read(12)) # membaca isi file dengan argumen jumlah karakter

# print(file.readline()) # membaca baris tertentu
# print(file.readline()) # membaca baris tertentu
file.close()


# appending mode
file = open('fTest.txt', 'a')
file.write('\nbaris ini ditambahkan dengan mode append')
file.close()