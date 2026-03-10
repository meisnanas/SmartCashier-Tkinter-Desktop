from tkinter import*
import random
import time
from tkinter import messagebox
from tkinter import filedialog

# Membuat Frame aplikasi
root = Tk()

root.geometry("1275x720+0+0")
root.resizable(0,0)
root.title("Ayam Geprek 99 Cashier")

topFrame=Frame(root,bd=20,relief=RIDGE,bg='white')
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='Ayam Geprek 99',font=('Castellar',38,'bold'),fg="#ffffff",bg="#cbae57",bd=15,width=30)  
labelTitle.grid(row=0,column=10)

root.config(bg="#cbae57")
# batas Frame aplikasi

# VARIABLE
# Menentukan variables
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()  

# variabel menu ayam geprek
e_ayamgeprekoriginal=StringVar()
e_ayamgepreksambalijo=StringVar()
e_ayamgeprekmozzarela=StringVar()
e_ayamgepreksambalmatah=StringVar()

# variabel menu minuman
e_esteh=StringVar()
e_esjeruk=StringVar()
e_airmineral=StringVar()
e_esteler=StringVar() 

# variabel Harga dalam struk
hargadariayamgeprekvar=StringVar()
hargadariminumanvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()
taxvaluevar=StringVar()

# variabel pembayaran
metodepembayaran=StringVar()
metodepembayaran.set("Cash")
jumlahdibayarvar=StringVar()
kembalianvar=StringVar()

e_ayamgeprekoriginal.set('0')
e_ayamgepreksambalijo.set('0')
e_ayamgeprekmozzarela.set('0')
e_ayamgepreksambalmatah.set('0')

e_esteh.set('0')
e_esjeruk.set('0')
e_airmineral.set('0')
e_esteler.set('0') 

# FUNGSI
# Awal fungsi perhitungan harga total
tax=(10/100)
def totalcost():

    global hargadariayamgeprek, hargadariminuman, subtotalItems, totaltax
    if (var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or
        var5.get() != 0 or var6.get() != 0 or var7.get() != 0 or var8.get() != 0):

        item1 = int(e_ayamgeprekoriginal.get())
        item2 = int(e_ayamgepreksambalijo.get())
        item3 = int(e_ayamgeprekmozzarela.get())
        item4 = int(e_ayamgepreksambalmatah.get())
        item5 = int(e_esteh.get())
        item6 = int(e_esjeruk.get())
        item7 = int(e_airmineral.get())
        item8 = int(e_esteler.get())

        hargadariayamgeprek = (item1 * 20000) + (item2 * 22000) + (item3 * 30000) + (item4 * 22000)
        hargadariminuman = (item5 * 5000) + (item6 * 6000) + (item7 * 5000) + (item8 * 7000)

        hargadariayamgeprekvar.set(str(hargadariayamgeprek))
        hargadariminumanvar.set(str(hargadariminuman))

        subtotalItems = hargadariayamgeprek + hargadariminuman
        subtotalvar.set(str(subtotalItems))
        taxvaluevar.set(str(tax))
        totaltax = round(subtotalItems * tax)
        servicetaxvar.set(totaltax)
        
        totalcost = subtotalItems + totaltax
        totalcostvar.set(str(totalcost))

    else:
        messagebox.showerror('Error', 'Tidak ada item yang dipilih')
# Batas fungsi perhitungan harga total

# Fungsi hitung kembalian
def hitungkembalian():
    global kembalian
    if totalcostvar.get() != '':
        if metodepembayaran.get() == "QR":
            kembalianvar.set('0')
            kembalian = 0
            messagebox.showinfo('Info','Pembayaran QR - Tidak ada kembalian')
        else:
            try:
                totalbayar = int(totalcostvar.get())
                jumlahdibayar = int(jumlahdibayarvar.get())
                
                if jumlahdibayar >= totalbayar:
                    kembalian = jumlahdibayar - totalbayar
                    kembalianvar.set(str(kembalian))
                else:
                    messagebox.showerror('Error','Jumlah bayar kurang!')
                    kembalianvar.set('')
            except:
                messagebox.showerror('Error','Masukkan jumlah bayar yang valid!')
    else:
        messagebox.showerror('Error','Hitung total terlebih dahulu!')

# awal fungsi cetak struk
def struk():
    global billnumber, date
    if hargadariayamgeprekvar.get() != '' or hargadariminumanvar.get() != '':
        if metodepembayaran.get() == "Cash" and kembalianvar.get() == '':
            messagebox.showerror('Error','Hitung kembalian terlebih dahulu!')
            return
            
        textStruk.delete(1.0, END)
        x = random.randint(100, 10000)
        billnumber = 'BILL' + str(x)
        date = time.strftime('%d/%m/%Y')
        textStruk.insert(END, ' Resep Ref:\t        ' + billnumber + '\t         ' + date + '\n')
        textStruk.insert(END, '******************************************************\n')
        textStruk.insert(END, '    Items\t\t             Harga Total (Rp)\n')
        textStruk.insert(END, '******************************************************\n')
        if e_ayamgeprekoriginal.get() != '0':
            textStruk.insert(END, f' Ayam geprek original\t\t\tRp{int(e_ayamgeprekoriginal.get()) * 20000}\n\n')

        if e_ayamgepreksambalijo.get() != '0':
            textStruk.insert(END, f' Ayam geprek sambal ijo\t\t\tRp{int(e_ayamgepreksambalijo.get()) * 22000}\n\n')

        if e_ayamgeprekmozzarela.get() != '0':
            textStruk.insert(END, f' Ayam geprek mozzarela\t\t\tRp{int(e_ayamgeprekmozzarela.get()) * 30000}\n\n')

        if e_ayamgepreksambalmatah.get() != '0':
            textStruk.insert(END, f' Ayam geprek sambal matah\t\t\tRp{int(e_ayamgepreksambalmatah.get()) * 22000}\n\n') 

        if e_esteh.get() != '0':
            textStruk.insert(END, f' Es teh\t\t\tRp{int(e_esteh.get()) * 5000}\n\n')

        if e_esjeruk.get() != '0':
            textStruk.insert(END, f' Es jeruk\t\t\tRp{int(e_esjeruk.get()) * 6000}\n\n')

        if e_airmineral.get() != '0':
            textStruk.insert(END, f' Air mineral\t\t\tRp{int(e_airmineral.get()) * 5000}\n\n')

        if e_esteler.get() != '0': 
            textStruk.insert(END, f' Es teler\t\t\tRp{int(e_esteler.get()) * 7000}\n\n')
        
        textStruk.insert(END, '******************************************************\n')
        if hargadariayamgeprekvar.get() != 'Rp0':
            textStruk.insert(END, f' Harga dari ayam geprek\t\t\tRp{hargadariayamgeprek}\n\n')
        if hargadariminumanvar.get() != 'Rp0':
            textStruk.insert(END, f' Harga dari minuman\t\t\tRp{hargadariminuman}\n\n')

        textStruk.insert(END, f' Sub Total\t\t\tRp{subtotalItems}\n\n')
        textStruk.insert(END, f' Service Tax\t\t\tRp{totaltax}\n\n')
        textStruk.insert(END, f' Harga total\t\t\tRp{subtotalItems + totaltax}\n\n')
        textStruk.insert(END, '******************************************************\n')
        textStruk.insert(END, f' Metode Pembayaran\t\t\t{metodepembayaran.get()}\n\n')
        
        if metodepembayaran.get() == "Cash":
            textStruk.insert(END, f' Jumlah Dibayar\t\t\tRp{jumlahdibayarvar.get()}\n\n')
            textStruk.insert(END, f' Kembalian\t\t\tRp{kembalianvar.get()}\n\n')
        else:
            textStruk.insert(END, f' Status\t\t\tLunas via QR\n\n')
            
        textStruk.insert(END, '******************************************************\n')      
    else:
        messagebox.showerror('Error','Tidak ada item yang dipilih')
# batas fungsi cetak struk

# awal fungsi simpan dalam perangkat
def save():
    if textStruk.get(1.0, END) == '\n':
        pass
    else:
        # HANYA DALAM EXTENSION FILE .txt
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt') 
        if url == None:
            pass
        else:
            bill_data = textStruk.get(1.0, END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Informasi','Struk Anda berhasil disimpan')
# Batas fungsi simpan dalam perangkat 

# awal fungsi reset
def reset():
    textStruk.delete(1.0, END)
    e_ayamgeprekoriginal.set('0')
    e_ayamgepreksambalijo.set('0')
    e_ayamgeprekmozzarela.set('0')
    e_ayamgepreksambalmatah.set('0')

    e_esteh.set('0')
    e_esjeruk.set('0')
    e_airmineral.set('0')
    e_esteler.set('0')  

    # batas untuk variables
    textayamgeprekoriginal.config(state=DISABLED)
    textayamgepreksambalijo.config(state=DISABLED)
    textayamgeprekmozzarela.config(state=DISABLED)
    textayamgepreksambalmatah.config(state=DISABLED)

    textesteh.config(state=DISABLED)
    textesjeruk.config(state=DISABLED)
    textairmineral.config(state=DISABLED)
    textesteler.config(state=DISABLED)  

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)  

    hargadariminumanvar.set('')
    hargadariayamgeprekvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')
    taxvaluevar.set('')
    
    # Reset pembayaran
    metodepembayaran.set("Cash")
    jumlahdibayarvar.set('')
    kembalianvar.set('')
# batas fungsi reset

# mengaktifkan fungsi entry menu ayam geprek
def ayamgeprekoriginal():
    if var1.get() == 1:
        textayamgeprekoriginal.config(state=NORMAL)
        textayamgeprekoriginal.delete(0, END)
        textayamgeprekoriginal.focus()
    else:
        textayamgeprekoriginal.config(state=DISABLED)
        e_ayamgeprekoriginal.set('0')

def ayamgepreksambalijo():
    if var2.get() == 1:
        textayamgepreksambalijo.config(state=NORMAL)
        textayamgepreksambalijo.delete(0, END)
        textayamgepreksambalijo.focus()
    else:
        textayamgepreksambalijo.config(state=DISABLED)
        e_ayamgepreksambalijo.set('0')

def ayamgeprekmozzarela():
    if var3.get() == 1:
        textayamgeprekmozzarela.config(state=NORMAL)
        textayamgeprekmozzarela.delete(0, END)
        textayamgeprekmozzarela.focus()
    else:
        textayamgeprekmozzarela.config(state=DISABLED)
        e_ayamgeprekmozzarela.set('0')

def ayamgepreksambalmatah():
    if var4.get() == 1:
        textayamgepreksambalmatah.config(state=NORMAL)
        textayamgepreksambalmatah.delete(0, END)
        textayamgepreksambalmatah.focus()
    else:
        textayamgepreksambalmatah.config(state=DISABLED)
        e_ayamgepreksambalmatah.set('0')
# batas mengaktifkan entry menu ayam geprek

# mengaktifkan entry menu minuman
def esteh():
    if var5.get() == 1:
        textesteh.config(state=NORMAL)
        textesteh.delete(0, END)
        textesteh.focus()
    else:
        textesteh.config(state=DISABLED)
        e_esteh.set('0')

def esjeruk():
    if var6.get() == 1:
        textesjeruk.config(state=NORMAL)
        textesjeruk.delete(0, END)
        textesjeruk.focus()
    else:
        textesjeruk.config(state=DISABLED)
        e_esjeruk.set('0')

def airmineral():
    if var7.get() == 1:
        textairmineral.config(state=NORMAL)
        textairmineral.delete(0, END)
        textairmineral.focus()
    else:
        textairmineral.config(state=DISABLED)
        e_airmineral.set('0')

def esteler(): 
    if var8.get() == 1:
        textesteler.config(state=NORMAL)
        textesteler.delete(0, END)
        textesteler.focus()
    else:
        textesteler.config(state=DISABLED)
        e_esteler.set('0')
# batas mengaktifkan entry minuman

# FRAME KIRI
# Membuat frame kiri untuk menu
menuFrame = Frame(root, bd=10, relief=RIDGE, bg='white')
menuFrame.pack(side=LEFT)

hargaFrame = Frame(menuFrame, bd=9, relief=RIDGE, bg="#eee7e7", pady=12)
hargaFrame.pack(side=BOTTOM)

ayamgeprekFrame = LabelFrame(menuFrame, text=' Ayam Geprek ', font=('Castellar', 19, 'bold'),
                             bd=10, relief=RIDGE, fg="#4b5125", bg='#f6f6f6')
ayamgeprekFrame.pack(side=LEFT)

minumanFrame = LabelFrame(menuFrame, text=' Minuman ', font=('Castellar', 19, 'bold'),
                          bd=10, relief=RIDGE, fg="#4b5125", bg='#f6f6f6')
minumanFrame.pack(side=RIGHT)
# batas frame kiri (menu cafe)

# membuat tampilan daftar menu ayam geprek
ayamgeprekoriginal = Checkbutton(ayamgeprekFrame, text=' Ayam Geprek Original (Rp20000) ',
                                 font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var1,
                                 command=ayamgeprekoriginal, bg='#f6f6f6')
ayamgeprekoriginal.grid(row=0, column=0, sticky=W)

ayamgepreksambalijo = Checkbutton(ayamgeprekFrame, text=' Ayam Geprek Sambal Ijo (Rp22000) ', 
                                  font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var2,
                                  command=ayamgepreksambalijo, bg='#f6f6f6')
ayamgepreksambalijo.grid(row=1, column=0, sticky=W)

ayamgeprekmozzarela = Checkbutton(ayamgeprekFrame, text=' Ayam Geprek Mozzarela (Rp30000) ',
                                  font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var3,
                                  command=ayamgeprekmozzarela, bg='#f6f6f6')
ayamgeprekmozzarela.grid(row=2, column=0, sticky=W)

ayamgepreksambalmatah = Checkbutton(ayamgeprekFrame, text=' Ayam Geprek Sambal Matah (Rp22000) ', 
                                  font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var4,
                                  command=ayamgepreksambalmatah, bg='#f6f6f6')
ayamgepreksambalmatah.grid(row=3, column=0, sticky=W)

# menambahkan fields entri untuk item ayam geprek
textayamgeprekoriginal = Entry(ayamgeprekFrame, font=('Calibri', '16', 'bold'),
                               bd=7, width=8, state=DISABLED, textvar=e_ayamgeprekoriginal)
textayamgeprekoriginal.grid(row=0, column=1)

textayamgepreksambalijo = Entry(ayamgeprekFrame, font=('Calibri', '16', 'bold'),
                               bd=7, width=8, state=DISABLED, textvar=e_ayamgepreksambalijo)
textayamgepreksambalijo.grid(row=1, column=1)

textayamgeprekmozzarela = Entry(ayamgeprekFrame, font=('Calibri', '16', 'bold'),
                               bd=7, width=8, state=DISABLED, textvar=e_ayamgeprekmozzarela)
textayamgeprekmozzarela.grid(row=2, column=1)

textayamgepreksambalmatah = Entry(ayamgeprekFrame, font=('Calibri', '16', 'bold'), 
                                bd=7, width=8, state=DISABLED, textvar=e_ayamgepreksambalmatah)
textayamgepreksambalmatah.grid(row=3, column=1)

# membuat tampilan daftar menu minuman
esteh = Checkbutton(minumanFrame, text='Es Teh (Rp5000)', font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var5,
                        command=esteh, bg='#f6f6f6')
esteh.grid(row=0, column=0, sticky=W)

esjeruk = Checkbutton(minumanFrame, text='Es Jeruk (Rp6000)', font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var6,
                        command=esjeruk, bg='#f6f6f6')
esjeruk.grid(row=1, column=0, sticky=W)

airmineral = Checkbutton(minumanFrame, text='Air Mineral (Rp5000)', font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var7,
                        command=airmineral, bg='#f6f6f6')
airmineral.grid(row=2, column=0, sticky=W)

esteler = Checkbutton(minumanFrame, text='Es Teler (Rp7000)', font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var8, 
                        command=esteler, bg='#f6f6f6')
esteler.grid(row=3, column=0, sticky=W)

# menambahkan fields entri untuk item minuman
textesteh = Entry(minumanFrame, font=('Calibri', '16', 'bold'), bd=7, width=8, state=DISABLED, textvar=e_esteh)
textesteh.grid(row=0, column=1)

textesjeruk = Entry(minumanFrame, font=('Calibri', '16', 'bold'), bd=7, width=8, state=DISABLED, textvar=e_esjeruk)
textesjeruk.grid(row=1, column=1)

textairmineral = Entry(minumanFrame, font=('Calibri', '16', 'bold'), bd=7, width=8, state=DISABLED, textvar=e_airmineral)
textairmineral.grid(row=2, column=1)

textesteler = Entry(minumanFrame, font=('Calibri', '16', 'bold'), bd=7, width=8, state=DISABLED, textvar=e_esteler)
textesteler.grid(row=3, column=1)

# FRAME KANAN
# Membuat frame kanan untuk (Struk)
rightFrame = Frame(root, bd=12, relief=RIDGE)
rightFrame.pack(side=RIGHT)
strukFrame = Frame(rightFrame, bd=1, relief=RIDGE, bg='#f0f0f0')
strukFrame.pack()
buttonFrame = Frame(rightFrame, bd=2, relief=RIDGE)
buttonFrame.pack(side=BOTTOM)
# Batas frame kanan (Struk)

# membuat label harga dan kolom entrinya
LabelHargadariAyamGeprek = Label(hargaFrame, text='  HARGA DARI AYAM GEPREK', font=('Constantia',12,'bold'),fg="#675a49")
LabelHargadariAyamGeprek.grid(row=0, column=0)

textHargadariAyamGeprek = Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargadariayamgeprekvar)
textHargadariAyamGeprek.grid(row=0,column=1,padx=41)

LabelHargadariMinuman = Label(hargaFrame,text='HARGA DARI MINUMAN', font=('Constantia',12,'bold'),fg="#675a49")
LabelHargadariMinuman.grid(row=1,column=0)

textHargadariMinuman = Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargadariminumanvar)
textHargadariMinuman.grid(row=1,column=1,padx=41)

# Frame untuk Metode Pembayaran
LabelMetodePembayaran = Label(hargaFrame,text='METODE PEMBAYARAN', font=('Constantia',12,'bold'),fg="#675a49")
LabelMetodePembayaran.grid(row=2,column=0)

radioCash = Radiobutton(hargaFrame, text='Cash', font=('Calibri',10,'bold'), variable=metodepembayaran, value="Cash", bg="#eee7e7")
radioCash.grid(row=2, column=1, sticky=W, padx=10)

radioQR = Radiobutton(hargaFrame, text='QR', font=('Calibri',10,'bold'), variable=metodepembayaran, value="QR", bg="#eee7e7")
radioQR.grid(row=2, column=1, sticky=E, padx=10)

# Input Jumlah Dibayar
LabelJumlahDibayar = Label(hargaFrame,text='JUMLAH DIBAYAR', font=('Constantia',12,'bold'),fg="#675a49")
LabelJumlahDibayar.grid(row=3,column=0)

textJumlahDibayar = Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,textvariable=jumlahdibayarvar)
textJumlahDibayar.grid(row=3,column=1,padx=41)

LabelSubTotal=Label(hargaFrame,text='SUB TOTAL', font=('Constantia',12,'bold'),fg="#675a49")
LabelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

LabelTax=Label(hargaFrame,text='PAJAK'+' '+ str(tax*100)+ '%', font=('Constantia',12,'bold'),fg="#675a49")
LabelTax.grid(row=1,column=2)

textTax=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=servicetaxvar)
textTax.grid(row=1,column=3,padx=41)

LabelHargaTotal=Label(hargaFrame,text='HARGA TOTAL', font=('Constantia',12,'bold'),fg="#675a49")
LabelHargaTotal.grid(row=2,column=2)

textHargaTotal=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=totalcostvar)
textHargaTotal.grid(row=2,column=3,padx=41)

# Kembalian
LabelKembalian=Label(hargaFrame,text='KEMBALIAN', font=('Constantia',12,'bold'),fg="#675a49")
LabelKembalian.grid(row=3,column=2)

textKembalian=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=kembalianvar)
textKembalian.grid(row=3,column=3,padx=41)

# Membuat tampilan Buttons struk (Tombol-tombol pada frame kanan)
buttonTotal= Button(buttonFrame,text='Total',font=('arial',10,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=6,
                    command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonKembalian= Button(buttonFrame,text='Kembalian',font=('arial',10,'bold'),fg='#fefefe',bg='#6a994e',bd=3,padx=6,
                    command=hitungkembalian)
buttonKembalian.grid(row=0,column=1)

buttonStruk= Button(buttonFrame,text='Struk',font=('arial',10,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=6,
                    command=struk)
buttonStruk.grid(row=0,column=2)

buttonSimpan= Button(buttonFrame,text='Simpan',font=('arial',10,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=6,
                    command=save)
buttonSimpan.grid(row=0,column=3)

buttonReset= Button(buttonFrame,text='Reset',font=('arial',10,'bold'),fg='#fefefe',bg='red',bd=3,padx=6,
            command=reset)
buttonReset.grid(row=0,column=4)

# menentukan teks pada frame struk
textStruk=Text(strukFrame,font=('arial',12,'bold'),bd=3,width=36,height=26)
textStruk.grid(row=0,column=0)

root.mainloop()