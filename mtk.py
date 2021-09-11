## contoh modul
import math
def tambah(x, y):
    print("operasi penjumlahan")
    print(f"{x} + {y} = {x + y}")


def kurang(x, y):
    print("operasi pengurangan")
    print(f"{x} - {y} = {x - y}")


def persamaanKuadrat(a, b, c): # ax^2 + bx + c = 0
    d = math.sqrt((b**2) - 4*a*c)
    x1 = (-b + d) / 2
    x2 = (-b - d) / 2
    print(f"{a}x^2 + {b}x + {c} = 0")
    print(f"x1 = {x1}  V  x2 = {x2}")
    return x1, x2

def fungsiUtama():
    print("ini adalah fungsi utama dari file mtk")

if __name__ == '__main__':
    fungsiUtama()

x1, x2 = persamaanKuadrat(1, 2, -3)
print('')
print(x1, x2)