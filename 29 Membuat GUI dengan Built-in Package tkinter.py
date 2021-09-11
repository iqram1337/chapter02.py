import tkinter

def ditekan():
    label2 = tkinter.Label(jendelaUtama, text = 'aku ditekan')
    label2.pack()


jendelaUtama = tkinter.Tk()
label1 = tkinter.Label(jendelaUtama, text='membuat GUI dengan menggunakan tkinter')
tombol = tkinter.Button(jendelaUtama, text='tekan tombol ini', command = ditekan)

label1.pack()
tombol.pack()
jendelaUtama.mainloop()