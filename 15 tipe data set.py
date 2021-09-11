### set atau himpunan (tidak mementingkan posisi atau index data)

## contoh 1
print("Contoh Pertama".center(80, "="))
hero = {'superman', 'ironman', 'batman'}
print(f"hero : {hero}")
print("tipe   :", type(hero))

print("menambah hulk")
hero.add('hulk')
print(f"hero : {hero}")
print("menambah thor")
hero.add('thor')
print(f"hero : {hero}")
print('\n')


## contoh 2
print("Contoh Kedua".center(80, "="))
pahlawan = set()
print(f"pahlawan : {pahlawan}")
print("tipe   :", type(pahlawan))
print("menambah hulk")
pahlawan.add('hulk')
print(f"pahlawan : {pahlawan}")
print("menambah wonder woman")
pahlawan.add('wonder woman')
print(f"pahlawan : {pahlawan}")
print("menambah thor")
pahlawan.add('thor')
print(f"pahlawan : {pahlawan}")
print("menambah spiderman")
pahlawan.add('spiderman')
print(f"pahlawan : {pahlawan}")
print('')
print("urut :", sorted(pahlawan))
print('\n')


## contoh 3
print("Contoh Ketiga".center(80, "="))
ganjil = {1, 3, 5, 7, 9}
genap = {2, 4, 6, 8, 10}
prima = {2, 3, 5, 7, 11}
print("ganjil :", ganjil)
print("genap  :", genap)
print("prima  :", prima)
print("tipe   :", type(prima))
print('')

# gabungan
print("ganjil U genap :", ganjil.union(genap))
# irisan
print("ganjil ( prima :", ganjil.intersection(prima))
print("genap ( prima :", genap.intersection(prima))