## belajar menangkap error

"""
type of exception errors:
1. IOError
2. ValueError
3. ImportError
4. Division by Zero
5. Keyboard Interupted
6. Syntax Error
7. EOFError
"""
# contoh 1
print('program pembagian')
while True:
    try:
        penyebut = int(input("masukkan penyebut: "))
        pembilang = int(input("masukkan pembilang: "))
        hasil = penyebut / pembilang
        break
    except ValueError:
        print('yang anda masukkan adalah string')
    except ZeroDivisionError:
        print('hasil tidak ditemukan, silahkan masukkan angka lain')


print('akhir dari program', hasil)