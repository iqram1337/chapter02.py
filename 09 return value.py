# fungsi dengan return value
print(50*"=")
def kuadrat(argumen1):
    hasil = argumen1**2
    print("kuadrat dari 3 =", hasil)
    return hasil

a = kuadrat(3)
print(a) # menampilkan a(9)
print('\n')


# fungsi dengan return value dan multiple arguments
print("Penjumlahan & Perkalian".center(50, "="))
def penjumlahan(argumen1, argumen2):
    hasil = argumen1 + argumen2
    print(f"{argumen1} + {argumen2} = {hasil}")
    return hasil

def perkalian(argumen1, argumen2):
    hasil = argumen1 * argumen2
    print(f"{argumen1} x {argumen2} = {hasil}")
    return hasil
arg1 = int(input('argumen1 : '))
arg2 = int(input('argumen2 : '))
x = penjumlahan(arg1, arg2)
y = perkalian(arg1, x)
print(x)
print(y)