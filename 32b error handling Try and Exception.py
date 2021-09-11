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

# contoh 2
print('program pembagian')
while True:
    try:
        penyebut = int(input("masukkan penyebut: "))
        pembilang = int(input("masukkan pembilang: "))
        hasil = penyebut / pembilang
        break
    except Exception as err:
        print(err)
    
print('akhir dari program', hasil)