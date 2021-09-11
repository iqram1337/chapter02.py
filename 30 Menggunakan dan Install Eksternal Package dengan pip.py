from PIL import Image

gambar = Image.open('gmb1.jpg')

print(gambar.format)
print(gambar.size)
print(gambar.mode)

gambar.show() 