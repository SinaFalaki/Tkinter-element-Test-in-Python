from tkinter import *
from tkinter import scrolledtext, messagebox, filedialog 
from tkinter.ttk import *

window = Tk()
window.geometry('1000x600')
window.title('مدیریت ')
########################################################################             لیبل گنده

lbl = Label(window, text='سلام', font=('B Nazanin', 20))
lbl.grid(column=8, row=1)
 
############################################################################            تکست باکس

txt = Entry(window, width=40)
txt.grid(column=50, row=50)
txt.focus()
txt.get()

############################################################################               کومبو باکس

combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, 'Sample')
combo.current(4)
combo.grid(column=500, row=500)
print(combo.get())
############################################################################               چک باکس

chk1_state = IntVar()
chk1_state.set(0)
chk1 = Checkbutton(window, text='Choose', var=chk1_state)
chk1.grid(column=1, row=3)

chk1_state = IntVar()
chk1_state.set(0)
chk1 = Checkbutton(window, text='Choose', var=chk1_state)
chk1.grid(column=2, row=3)


chk1_state = IntVar()
chk1_state.set(0)
chk1 = Checkbutton(window, text='Choose', var=chk1_state)
chk1.grid(column=3, row=3)

############################################################################      رایدیو باتن

selected = IntVar()

def rad_clicked():
    print('Radio Button was clicked!')

rad1 = Radiobutton(window, text='First', value=1, command=rad_clicked, variable=selected )
rad2 = Radiobutton(window, text='Second', value=2, variable=selected)
rad3 = Radiobutton(window, text='Third', value=3, variable=selected)

rad1.grid(column=0, row=4)
rad2.grid(column=1, row=4)
rad3.grid(column=2, row=4)

selected.get()

############################################################################ متن زیااااد 

text_area = scrolledtext.ScrolledText(window, width=40, height=10)
text_area.grid(column=1, row=5)

text_area.insert(INSERT, 'Write everything you want...')



############################################################################ 

#messagebox.showinfo("sina", "salam")
#messagebox.showerror   ("sina", "salam")
#messagebox.showwarning   ("sina", "salam")
 


#answer=messagebox.askquestion("sina", "bye") 
#print(answer)

#messagebox.askyesno("sina", "bye")

##############################################################################      مثل اونیه که عین تکست باکسه ولی فقط عدد میگیره
var = IntVar()
var.set(55)

spin = Spinbox(window, from_=0, to_=60, width=19, textvariable=var)
spin.grid(column=0, row=6)

###############                     عین همون بالایی است فقط مقادیرش رو خودت مشخص میکنی


spin = Spinbox(window, values=(5, 12, 23), width=5)
spin.grid(column=3, row=6)

################################################################################# استایل میده به کل کار


#Style = Style()
#Style.theme_use('default')
#Style.configure("black.Horizontal.TProgressbar", background="black")


#################################################################################         نوار لودینگ

bar = Progressbar(window, length=200, style="white.Horizontal.TProgressbar")
bar['value'] = 99
bar.grid(column=1, row=9)
#################################################################################   تیتری به شکل دکمه

menu = Menu(window)
 
new_item = Menu(menu)
new_item.add_command(label='خود خودشه')
new_item.add_command(label='بیا اینجا')
menu.add_cascade(label="!منو کلیک کن لطفا", menu=new_item)



window.config(menu=menu)


#####################################################################

def btn_clicked():
       lbl.configure(text='Button was clicked!!!')
       res = f'Hello, {txt.get()}!'
       res = f'Selected item is {combo.get()}!'
       lbl.configure(text=res)
 
       print(selected.get())
 
       file = filedialog.askopenfilename()
       print(file)
 
       files = filedialog.askopenfilenames()
       print(files)
 
       file = filedialog.askopenfilename(filetypes = (("Text files", "*.txt"), ("all files", "*.*")))
       print(file)
 
       dir = filedialog.askdirectory()
       print(dir)
       pass

def off():
    window.destroy()


#btn = Button(window, text='Click me!', bg='purple', fg='orange', command=btn_clicked)
btn = Button(window, text='Click me!', command=off)                                         # دکمه
btn.grid(column=9, row=9)

#_____________________________________________________________________________________________________




window.mainloop()