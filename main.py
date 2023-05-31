import hashlib as hasher
import os
import sys
from tkinter import *
from tkinter import filedialog, messagebox

from PIL import Image
from PIL import ImageTk
from stegano import lsb  # pip install stegano
from reedsolo import RSCodec, ReedSolomonError

root = Tk()
root.title("Abdullah Keskin Bitirme Projesi")
root.geometry("700x500+250+180")
root.resizable(False, False)
root.configure(bg="#2f4155")


def showImage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Resim Seçiniz",
                                          filetypes=(("PNG File", "*.png"),
                                                     ("All File", "*.txt")))

    img = Image.open(filename)
    new_image = img.resize((250, 250))
    my_img = ImageTk.PhotoImage(new_image)
    lbl.configure(image=my_img)
    lbl.image = my_img

def Hide():
    global secret
    message = text1.get(1.0, END)

    # Hascode Üretilmesi ve Yazılması
    hashcode = hasher.sha256()
    metin = message
    hashcode.update((metin.encode("utf-8")))
    hash = hashcode.hexdigest()
    print(hash)

    if message == '\n':
        messagebox.showinfo("Dikkat","Mesaj Kutusuna Metin Giriniz ")
    else:
        secret = lsb.hide(str(filename), message + ' ' + hash)
        messagebox.showinfo("Başarili","Encoding Başarılı\nDosya aynı dizinde kaydedildi")
        print("Girilen metinin boyutu: ", sys.getsizeof(message))

def Show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)

    """
        ----- REED SOLOMON DENEME
    rsc = RSCodec(10)  # 10 ecc symbols
    tampered_msg = clear_message
    decoded_msg, decoded_msgecc, errata_pos = rsc.decode(tampered_msg)

    print(decoded_msg)

    print(decoded_msgecc)

    print(errata_pos)

    print(list(errata_pos))
    """

def save():
    secret.save("Görüntü Yakalama/new_img.png")

Label(root, text="Steganografi Final Proje", bg="#2d4155", fg="white", font="arial 25 bold").place(x=10, y=10)

# First Label
f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)

lbl = Label(f, bg="black")
lbl.place(x=40, y=10)

# Second Frame
frame2 = Frame(root, bd=3, width=340, height=280, bg="white", relief=GROOVE)
frame2.place(x=350, y=80)

text1 = Text(frame2, font="Robote 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Third Frame
frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3, text="Resim Seç", width=10, height=2, font="arial 14 bold", command=showImage).place(x=20, y=30)
Button(frame3, text="Resim Kaydet", width=10, height=2, font="arial 14 bold", command=save).place(x=180, y=30)
Label(frame3, text="Resim Dosyası", bg="#2f4155", fg="yellow").place(x=20, y=5)

# Fourth Frame
frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)

Button(frame4, text="Metin Gizle", width=10, height=2, font="arial 14 bold", command=Hide).place(x=20, y=30)
Button(frame4, text="Metin Göster", width=10, height=2, font="arial 14 bold", command=Show).place(x=180, y=30)
Label(frame4, text="Resim Dosyası", bg="#2f4155", fg="yellow").place(x=20, y=5)

root.mainloop()
