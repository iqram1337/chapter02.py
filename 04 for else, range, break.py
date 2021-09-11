# range loop
print("Range Loop".center(30, '='))
print("range [0, 10, 2):")

for i in range (0, 10, 2): # loop
    print(i)
print('')

# latihan loop
print("Mencari Angka Pada Range".center(50, '='))
angka = int(input('masukkan angka dengan range [0, 50]: '))

for x in range (0, 51): # loop
    if x == angka:
        print("angka", angka, "ditemukan")
        break
else:
    print("angka tidak ditemukan")
print("\nspace di luar loop")
