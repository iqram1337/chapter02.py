# list sebagai iterable
print("Loop Pertama".center(50, '='))
gorengan = ['bakwan', 'pempek', 'pisang goreng', 'tempe goreng', 'cireng', 'tahu isi']
print('gorengan:')
print(gorengan)
i = 1
for g in gorengan:
    print(f"{i}) {g}")
    i+=1
    print('  panjang str =', len(g))
print('\n')


# string sebagai iterable
print("Loop Kedua".center(50, '='))
b = "bakwan"
print(b)
for j in b:
    print(j)
print('\n')


# for di dalam for
print("Loop Ketiga".center(50, '='))
buah = ['apel', 'mangga', 'pisang', 'durian']
sayur = ['kangkung', 'bayam', 'wortel', 'kentang']
gorengan = ['bakwan', 'tempe', 'cireng', 'tahu']
gabungan = [buah, sayur, gorengan]

x = 1
for jenisMakanan in gabungan:
    print(jenisMakanan)
    for namaMakanan in jenisMakanan:
        print(f"{x}) {namaMakanan}")
        x+=1
    x = 1
    print('')