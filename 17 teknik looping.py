### macam-macam teknik looping
nama = {'Iqram', 
        'Sovia',
        'Jack',
        'Andrew',
        'Brian'}

negara = {'Indonesia',
          'Rusia',
          'Amerika',
          'Inggris',
          'Kanada'}

## enumerate
print("Enumerate".center(80, "="))
for i, n in enumerate(nama):
    print(i, ":", n)
print('')


## zip
print("||Zip||".center(80, "="))
for namax, negarax in zip(nama, negara):
    print(namax.ljust(6), ":", negarax)
print('\n')


## set
print("||Set||".center(80, "="))
benda = {'kursi', 'meja', 'angklung', 'motor'}
print("benda :", benda)
for x in sorted(benda):
    print(x)
print('\n')


## dictionary
print("Dictionary".center(80, "="))
nama = {'Iqram': 'Indonesia', 
        'Sovia': 'Rusia',
        'Jack': 'Amerika'}

for name, country in nama.items(): # x.keys | x.items | x.values
    print(name.ljust(5), ":", country)