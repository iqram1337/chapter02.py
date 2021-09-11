import sys as sys

dataList = [1, 2, 3, 4, 5, 'pisang goreng', True, 3.14]
dataTuple = (1, 2, 3, 4, 5, 'pisang goreng', True, 3.14)

print("tuple :", dataTuple)
print("tipe  :", type(dataTuple))
print("ukuran:", sys.getsizeof(dataTuple)) # ukuran memori
print('')

print("list  :", dataList)
print("tipe  :", type(dataList))
print("ukuran:", sys.getsizeof(dataList)) # ukuran memori