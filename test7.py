from tkinter import *

root = Tk()
root.geometry('400x400')
root.config(bg = 'magenta')
root.resizable(0,0)
root.title('PhoneBook App')
contactlist = [
    ['Jane Doe',  '123456'],
    ['John Doe',  '78910'],
    ]
Name = StringVar()
Number = StringVar()
frame = Frame(root)
frame.pack(side = RIGHT)
#scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, height=12)
#scroll.config (command=select.yview)
#scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)


def Selected():
    return int(select.curselection()[0])
def AddContact():
    contactlist.append([Name.get(), Number.get()])
    Select_set()

def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name, phone in contactlist:
        select.insert(END, name)


Select_set()


Label(root, text = 'NAME', font='arial 12 bold', bg='white', fg='#ebb434').place(x= 30, y=20)
Entry(root, textvariable = Name).place(x= 100, y=20)
Label(root, text = 'PHONE NO.', font='arial 12 bold',bg='white', fg='#ebb434').place(x= 30, y=70)
Entry(root, textvariable = Number).place(x= 130, y=70)
Button(root,text=" ADD", font='arial 12 bold',bg='white', fg='#ebb434', command = AddContact).place(x= 50, y=110)

root.mainloop()