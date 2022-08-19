def acm(A, n, i):
    i /= 12
    ni = (1 + i) ** n
    Pk = A * i * ni / (ni - 1)
    I = Pk * n - A
    Iks = []
    Aks = []
    for k in range(n):
        Ik = (A - sum(Aks)) * i
        Ak = Pk - Ik
        Iks.append(Ik)
        Aks.append(Ak)
    return Pk, Aks, Iks


def apm(A, n, i):
    i /= 12
    Ak = A / n
    Iks = []
    Pks = []
    for k in range(n):
        Ik = (A - Ak * k) * i
        Pk = Ak + Ik
        Iks.append(Ik)
        Pks.append(Pk)
    return Pks, Ak, Iks


##A = 500000
##i = 0.059
##n = 360
##Pk1,Aks,Iks1 = acm(A,n,i)
##Pk2,Ak,Iks2 = apm(A,n,i)

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win = Tk()
win.update()
w, h = 600, 400
win.geometry("600x400")
win.title("还款计算器")

win_w, win_h = win.winfo_width(), win.winfo_height()
uframe = Frame(win, height=int(win_h / 2), width=int(win_w / 2))
uframe.pack(side=TOP, fill=Y)
dframe = Frame(win, height=int(win_h / 2))
dframe.pack(side=BOTTOM, fill=BOTH, expand=1)

loan_label = Label(uframe, text="贷款金额:")
loan_entry = Entry(uframe, width=15, bg="cyan")
unit_label = Label(uframe, text="万元")
loan_label.grid(row=0)
loan_entry.grid(row=0, column=1)
unit_label.grid(row=0, column=2)

years_label = Label(uframe, text="贷款年限:")
noy = IntVar()
noy.set(1)
years_combobox = ttk.Combobox(uframe, width=12, textvariable=noy)
years_combobox["value"] = list(range(1, 31))

text = StringVar()
text.set("12期")
term_label = Label(uframe, width=4, textvariable=text)

years_label.grid(row=1, column=0)
years_combobox.grid(row=1, column=1)
term_label.grid(row=1, column=2)


def change_combobox(*args):
    num = years_combobox.get()
    num = 12 * int(num)
    string = str(num) + "期"
    text.set(string)


years_combobox.bind("<<ComboboxSelected>>", change_combobox)

intetrest_label = Label(uframe, text="贷款利率:")
intetrest_entry = Entry(uframe, width=15, bg="cyan")
sign_label = Label(uframe, text="%")

intetrest_label.grid(row=2)
intetrest_entry.grid(row=2, column=1)
sign_label.grid(row=2, column=2)

v = IntVar()
v.set(1)
acmr = Radiobutton(uframe, text="等额本息", value=1, variable=v, bg="yellow")
apmr = Radiobutton(uframe, text="等额本金", value=2, variable=v, bg="yellow")
acmr.grid(row=3, column=0, sticky=E)
apmr.grid(row=3, column=2, sticky=W)

button = Button(uframe, text="计算", bg="grey")
button.grid(row=4, column=1)

tree = ttk.Treeview(dframe, show="headings")
scroll = Scrollbar(command=tree.yview)
tree.config(yscrollcommand=scroll.set)
names = ("terms", "payment", "interest", "principal")
tree["columns"] = names
tree.column("terms", width=4, anchor="center")
tree.column("payment", width=30, anchor="center")
tree.column("interest", width=30, anchor="center")
tree.column("principal", width=30, anchor="center")

tree.heading("terms", text="期数")
tree.heading("payment", text="还款总额")
tree.heading("interest", text="还款本金")
tree.heading("principal", text="还款利息")
tree.pack(side=TOP, fill=BOTH, expand=1)


def press_button(*args):
    A = loan_entry.get()
    i = intetrest_entry.get()
    n = years_combobox.get()
    contents = tree.get_children()
    for item in contents:
        tree.delete(item)

    if A and i and n:
        A = int(A) * 10000
        i = float(i) / 100
        n = int(n) * 12
        choice = v.get()
        if choice == 1:
            Pk, Aks, Iks = acm(A, n, i)
            Pk = round(Pk, 2)
            sAks, sIks = round(sum(Aks), 2), round(sum(Iks), 2)
            values = ("总金额", Pk * n, sAks, sIks)
            tree.insert("", 0, values=values)
            for k in range(n):
                term = str(k + 1) + "期"
                Ak = round(Aks[k], 2)
                Ik = round(Iks[k], 2)
                values = (term, Pk, Ak, Ik)
                tree.insert("", k + 1, values=values)

        if choice == 2:
            Pks, Ak, Iks = apm(A, n, i)
            Ak = round(Ak, 2)
            sPks, sIks = round(sum(Pks), 2), round(sum(Iks), 2)
            values = ("总金额", sPks, Ak * n, sIks)
            tree.insert("", 0, values=values)
            for k in range(n):
                term = str(k + 1) + "期"
                Pk = round(Pks[k], 2)
                Ik = round(Iks[k], 2)
                values = (term, Pk, Ak, Ik)
                tree.insert("", k + 1, values=values)

    else:
        messagebox.showinfo('提示', '请输入正确的信息')


button.bind('<Button-1>', press_button)

win.mainloop()
