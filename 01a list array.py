## array
print("")
data = [2, 4, 21, 5, 9, 13, 54, 43, 55, 3]
data2 = [100, 200, 300, 400, 500]
banyak_data = len(data)

print(data)
print(f"banyak data = {banyak_data}")
print("")

subdata0 = data[0]
subdata1 = data[1]
subdata4 = data[4]
subdatamin = data[-2]
subdata5 = data[-2:]
subdata6 = data[:2]
subdata04 = data[0:4]
subdata0102 = data[0:10:2]


print(f"""subdata ke-0    = {subdata0}
subdata ke-1    = {subdata1}
subdata ke-4    = {subdata4}
subdata ke-(-2) = {subdatamin}
subdata [-2:]   = {subdata5}
subdata [:2]   = {subdata6}
subdata [0:4]   = {subdata04}
subdata [0:10:2]= {subdata0102}
""")

data3 = data + data2
print(f"data 1 = {data}")
print(f"data 2 = {data2}")
print(f"data 1 + data 2 = {data3}")
print('')

# mengubah suatu data dari list data
data = [2, 4, 21, 5, 9, 13, 54, 43, 55, 3]
print(data)
print(f"data awal[4] = {data[4]}")
data[4] = 100
print(f"data akhir[4] = {data[4]}")
print(data)