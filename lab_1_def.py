# Смирнов Иван ИУ7-22Б Защита

import tkinter as tk

def from_10_to_7(n):
    if (n[0] == "0" and len(n) > 1):
        entry_out['state']=tk.NORMAL
        entry_out.delete(0, tk.END)
        entry_out.insert(0, "error")
        entry_out['state']=tk.DISABLED
        return
    n = int(n)
    s = ""
    if n == 0:
        s = "0"
    while n > 0:
        num = n % 7
        n //= 7
        s = s + str(num)
    entry_out['state']=tk.NORMAL
    entry_out.delete(0, tk.END)
    entry_out.insert(0, s[::-1])
    entry_out['state']=tk.DISABLED

def from_7_to_10(n):
    if "7" in n or "8" in n or "9" in n or (n[0] == "0" and len(n) > 1):
        entry_out['state']=tk.NORMAL
        entry_out.delete(0, tk.END)
        entry_out.insert(0, "error")
        entry_out['state']=tk.DISABLED
        return
    s = n[::-1]
    res = 0
    for i in range(len(s)):
        res += int(s[i])*(7**i)
    entry_out['state']=tk.NORMAL
    entry_out.delete(0, tk.END)
    entry_out.insert(0, str(res))
    entry_out['state']=tk.DISABLED

def add_digit(n):
    entry_in['state']=tk.NORMAL
    value = entry_in.get()
    entry_in.delete(0, tk.END)
    entry_in.insert(0, value+n)
    entry_in['state']=tk.DISABLED

def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char == "C":
        entry_in['state']=tk.NORMAL
        entry_in.delete(0, tk.END)
        entry_in['state']=tk.DISABLED
        

root = tk.Tk()
root.title("lab_01 def")
root.geometry("350x350")
root.configure(bg="lime")

root.bind('<Key>', press_key)

entry_in = tk.Entry(root, justify=tk.RIGHT, font=("Times New Roman", 30), width=15)
entry_in.grid(row=0, column=0, columnspan=2, stick="wens")
entry_in.insert(0, "")
entry_in['state']=tk.DISABLED

entry_out = tk.Entry(root, justify=tk.RIGHT, font=("Times New Roman", 30), width=15)
entry_out.grid(row=2, column=0, columnspan=2, stick="wens")
entry_out.insert(0, "")
entry_out['state']=tk.DISABLED

menu = tk.Menu(root)
root.config(menu=menu)

tk.Button(text="10->7", bg="black", fg="white", height=5, width=10, command=lambda: from_10_to_7(entry_in.get())).grid(row=1, column=0, stick="wens")
tk.Button(text="7->10", bg="black", fg="white", height=5, width=10, command=lambda: from_7_to_10(entry_in.get())).grid(row=1, column=1, stick="wens")

clear(entry_in)
clear(entry_out)

root.mainloop()
