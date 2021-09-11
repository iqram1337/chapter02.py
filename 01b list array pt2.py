# mencopy list data ke variabel baru
print("")
data = [2, 4, 21, 5, 9, 13, 54, 43, 55, 3]
data2 = [100, 200, 300, 400, 500]
print(f"data asli     = {data}")
print('')

a = data[:]
# jangan a = data!!!!
a[0] = 1
print(f"data duplikat = {a}")
print(f"data asli     = {data}")
print("")

# mengubah suatu data menggunakan metode slicing
print(f"data awal  = {data}")
data[3:5] = [100, 200]
print("data[3:5]  = [100, 200]")
print(f"data akhir = {data}")
print("")


# list dalam list
data3 = [1, 2, 3, 4, 5]
data2 = [100, 200, 300, 400, 500]
x = [data3,data2]
print(f"data         = {x}")

# mengakses list data dalam multidimensional list
subdata0 = x[0] [4]
subdata1 = x[1] [0]
subdata2 = x[1] [1]

print(f"data [0] [4] = {subdata0}")
print(f"data [1] [0] = {subdata1}")
print(f"data [1] [1] = {subdata2}")
print("")

# menambah satu integer ke dalam list
print(f"data awal   = {data}")
jd = len(data)
print("jumlah data = ", jd)

data.append(99)
jd = len(data)
print(f"data akhir  = {data}")
print("jumlah data = ", jd)