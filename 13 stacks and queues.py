from collections import deque
## stacks


print("STACKING".center(50, '='))
tumpukan = [1, 2, 3, 4, 5]
print(f"data sekarang : {tumpukan}")

# memasukkan data
tumpukan.append(6)
print("data masuk :", 6)
print(f"data sekarang : {tumpukan}")
tumpukan.append(7)
print("data masuk :", 7)
print(f"data sekarang : {tumpukan}")

# mengeluarkan data
out = tumpukan.pop() # mengeluarkan data dari sebelah kanan
print("data keluar :", out)
print(f"data sekarang : {tumpukan}")
out = tumpukan.pop()
print("data keluar :", out)
print(f"data sekarang : {tumpukan}")
print('\n')


## queue
print("QUEUEING".center(50, '='))
antrian = deque([1, 2, 3, 4, 5])
print(f"data sekarang : {antrian}")

# memasukkan data
antrian.append(6)
print("data masuk :", 6)
print("data sekarang :", antrian)
antrian.append(7)
print("data masuk :", 7)
print("data sekarang :", antrian)

# mengeluarkan data
x = antrian.popleft() # mengeluarkan data dari sebelah kiri
print("data keluar :", x)
print("data sekarang :", antrian)
x = antrian.popleft() # mengeluarkan data dari sebelah kiri
print("data keluar :", x)
print("data sekarang :", antrian)