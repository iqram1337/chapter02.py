import timeit as waktu

dataList = waktu.timeit(stmt="[1, 2, 3, 4, 5, 'pisang goreng', True, 3.14]", number=1000000)
dataTuple = waktu.timeit(stmt="(1, 2, 3, 4, 5, 'pisang goreng', True, 3.14)", number=1000000)

print("tuple :", dataTuple)
print("list  :", dataList)