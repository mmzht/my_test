import tkinter as tk

win = tk.Tk()
win.title("python练习标题")
win.geometry("600x400+500+100")
label = tk.Label(win, text="请输入数字：")
label.pack()

entryValve = tk.Variable()  # 获取输入框的内容
entryValve.set("默认值")
entry1 = tk.Entry(win, show="", textvariable=entryValve, width=50, bg="pink")
entry1.pack()
show_label1 = tk.Label(win, textvariable=entryValve, width=50, bg="pink")
show_label1.pack()


def func():
    print(entryValve.get())


button1 = tk.Button(win, text="执行程序", command=func, width=20)  # button1执行func
button1.pack()

button2 = tk.Button(win, text="点击显示")
button2.pack()

entry2 = tk.Entry(win, width=10, bg="pink")
entry2.pack()
text = tk.StringVar()
text.set("0")
show_label2 = tk.Label(win, textvariable=text)
show_label2.pack()


def press_button(*args):
    value = entry2.get()
    text.set(value)


button2.bind('<Button-1>', press_button)  # 绑定button2左击鼠标时的动作

button3 = tk.Button(win, text="退出窗口", command=win.quit)
button3.pack()

win.mainloop()

if __name__ == '__main__':
    pass
