# membuat while loop
print("While Loop Sederhana".center(41, '='))
angka = 0
while angka < 5:
    print("nilai angka adalah =", angka)
    angka += 1
print("di luar loop\n")


# membuat while loop 2
print("While Loop Boolean".center(41, '='))
awal = True
angka = 0
while awal:
    if(angka == 5):
        awal = False
    print(angka, "- di dalam loop")
    angka+=1
print("di luar loop")