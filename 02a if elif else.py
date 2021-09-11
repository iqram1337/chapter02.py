# operator kondisi percabangan if elif else
# latihan if elif else
print("Memeriksa Nilai Mata Kuliah".center(50, '='))
n = int(input('masukkan nilai mata kuliah anda: '))

if n < 35:
    print("\nindeks anda adalah E")
elif 35 <= n <= 44:
    print("indeks anda adalah D")
elif 45 <= n <= 54:
    print("indeks anda adalah C")
elif 55 <= n <= 64:
    print("indeks anda adalah BC")
elif 65 <= n <= 74:
    print("indeks anda adalah B")
elif 75 <= n <= 84:
    print("indeks anda adalah AB")
else:
    print("indeks anda adalah A")