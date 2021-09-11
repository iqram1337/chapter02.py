print("Operator Logika Untuk String".center(61, "="))

makanan = ['nasi goreng', 'pempek', 'bakwan', 'bakso', 
'mie ayam', 'indomie', 'pisang goreng', 'martabak', 'risol']

beli = input("tanya stok makanan = ")
beli = beli.lower()

if beli in makanan:
    print(beli + " ready, minat dm")
if beli not in makanan:
    print("maaf, " + beli + " sedang tidak ready")

