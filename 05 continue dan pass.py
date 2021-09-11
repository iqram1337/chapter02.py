# pass
print("Penggunaan Pass".center(30, '='))
for i in range(1,5):
    pass # null statement
    print(i)
print('')

# continue
print("Penggunaan Continue".center(30, '='))
for i in range (1,10):
    if i == 6:
        print('enam')
        #break # untuk mengakhiri loop 
        continue # untuk melanjutkan ke step berikutnya
    print(i)
else:
    print("selesai")
print('di luar loop')