from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0,column=0, columnspan=4, padx=10, pady=10)

current_num = 0
current_dey = None

def btn_click(btn):
    global current_num, current_dey
    if btn == 'c':
        e.delete(0, END)
    else:
        if not all(('0' <= i <= '9' or i == '-') for i in e.get()):
            e.delete(0, END)
            e.insert(0, 'error')
        else:
            if '0' <= btn <= '9':
                print(btn)
                e.insert(END, btn)
            elif btn in ['+', '-', '*', '/']:
                if btn == '-' and not e.get():
                    e.insert(0, btn)
                    return
                current_num = int(e.get())
                e.delete(0, END)
                current_dey = btn
            elif btn == '=':
                newnum = int(e.get())
                e.delete(0, END)
                if current_dey == '+':
                    e.insert(0, str(current_num + newnum))
                elif current_dey == '-':
                    e.insert(0, str(current_num - newnum))
                elif current_dey == '*':
                    e.insert(0, str(current_num * newnum))
                elif current_dey == '/':
                    if newnum == 0:
                        e.insert(0, 'чел...')
                    else:
                        e.insert(0, str(current_num // newnum))



num_1 = Button(root, text='1', padx = 40, pady = 20, command=lambda: btn_click('1'))
num_2 = Button(root, text='2', padx = 40, pady = 20, command=lambda: btn_click('2'))
num_3 = Button(root, text='3', padx = 40, pady = 20, command=lambda: btn_click('3'))
num_4 = Button(root, text='4', padx = 40, pady = 20, command=lambda: btn_click('4'))
num_5 = Button(root, text='5', padx = 40, pady = 20, command=lambda: btn_click('5'))
num_6 = Button(root, text='6', padx = 40, pady = 20, command=lambda: btn_click('6'))
num_7 = Button(root, text='7', padx = 40, pady = 20, command=lambda: btn_click('7'))
num_8 = Button(root, text='8', padx = 40, pady = 20, command=lambda: btn_click('8'))
num_9 = Button(root, text='9', padx = 40, pady = 20, command=lambda: btn_click('9'))
num_0 = Button(root, text='0', padx = 40, pady = 20, command=lambda: btn_click('0'))

btn_plus = Button(root, text='+', padx=39, pady = 20, command=lambda: btn_click('+'))
btn_minus = Button(root, text='-', padx = 40, pady = 20, command=lambda: btn_click('-'))
btn_umnozh = Button(root, text='*', padx = 40, pady = 20, command=lambda: btn_click('*'))
btn_delit = Button(root, text='/', padx = 40, pady = 20, command=lambda: btn_click('/'))
btn_clear = Button(root, text='C', padx = 39, pady = 20, command=lambda: btn_click('c'))
btn_ravno = Button(root, text='=', padx = 39, pady = 20, command=lambda: btn_click('='))

num_1.grid(row=1, column=0)
num_2.grid(row=1, column=1)
num_3.grid(row=1, column=2)
num_4.grid(row=2, column=0)
num_5.grid(row=2, column=1)
num_6.grid(row=2, column=2)
num_7.grid(row=3, column=0)
num_8.grid(row=3, column=1)
num_9.grid(row=3, column=2)
num_0.grid(row=4, column=0)

btn_plus.grid(row=1, column=3)
btn_minus.grid(row=2, column=3)
btn_umnozh.grid(row=3, column=3)
btn_delit.grid(row=4, column=3)
btn_ravno.grid(row=4, column=1)
btn_clear.grid(row=4, column=2)





root.mainloop()