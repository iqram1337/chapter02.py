# else, break, continue, pass
print("While Loop Sederhana".center(41, '='))
angka = 0

while angka < 10:
    if angka == 5:
        print("check point 1")
        #continue
        #break
        print("check point 2")
    print("nilai angka adalah =", angka)
    angka += 1
else:
    print("nilai angka akhir =", angka)
print("di luar loop")