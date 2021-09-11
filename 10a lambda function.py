# membuat anonymous function dengan lambda
print("Perkalian".center(40, "="))
perkalian = lambda a, b: a * b
a = int(input("a = "))
b = int(input("b = "))

hasil = perkalian(a, b)
print(hasil)
print('\n')


print("List Array".center(40, "="))
nums = [48, 6, 9, 21, 1]

square_all = map(lambda num: num ** 2, nums)

print(square_all)
print(list(square_all))
