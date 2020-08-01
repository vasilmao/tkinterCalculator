from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0,column=0, columnspan=4, padx=10, pady=10)

last_num = 0
current_operator = None

def parse(s):
    cur = ""
    digits = []
    operations = []
    if s.startswith("-"):
        s = "0" + s
    i = 0
    while i < len(s):
        if s[i] == '(':
            if cur:
                digits.append(float(cur) if '.' in cur else int(cur))
                cur = ""
                operations.append('*')
            skobcnt = 1
            endd = -1
            for j in range(i + 1, len(s)):
                if s[j] == '(':
                    skobcnt += 1
                elif s[j] == ')':
                    skobcnt -= 1
                if skobcnt == 0:
                    endd = j
                    break
            if endd == -1:
                endd = len(s)
            res = parse(s[i + 1 : endd])
            digits.append(res)
            i = endd + 1
        elif s[i].isdigit() or s[i] == '.':
            cur += s[i]
            if s[i - 1] == ')':
                operations.append('*')
            i += 1
        elif s[i] in ['+', '-', '*', '/']:
            if cur:
                digits.append(float(cur) if '.' in cur else int(cur))
            operations.append(s[i])
            cur = ""
            i += 1
    if cur:
        digits.append(float(cur) if '.' in cur else int(cur))
    print(digits)
    print(operations)
    cur = digits[0]
    flags = [False for i in range(len(digits))]
    for i in range(len(operations)):
        if operations[i] in '*/':
            flags[i] = True
    j = -1
    cur = 0
    cur_operation = '+'
    while j < len(operations):
        if j >= 0:
            cur_operation = operations[j]
        if flags[j + 1] == True:
            j += 1
            cur1 = digits[j]
            while j < len(operations) and operations[j] in '*/':
                if operations[j] == '*':
                    cur1 *= digits[j + 1]
                elif operations[j] =='/':
                    cur1 /= digits[j + 1]
                j += 1
            if cur_operation == '+':
                cur += cur1
            elif cur_operation == '-':
                cur -= cur1
        else:
            x = digits[j + 1]
            if cur_operation == '+':
                cur += x
            elif cur_operation == '-':
                cur -= x
            j += 1
    return cur

def btn_click(btn):
    if btn in '0123456789+-*/().':
        e.insert(END, btn)
    elif btn == 'del':
        e.delete(len(e.get()) - 1, END)
    elif btn == 'c':
        e.delete(0, END)
    elif btn == '=':
        ss = e.get()
        e.delete(0, END)
        result = parse(ss)
        e.insert(0, str(result))



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

btn_skobka1 = Button(root, text='(', padx=40, pady=20, command=lambda: btn_click('('))
btn_skobka2 = Button(root, text=')', padx=40, pady=20, command=lambda: btn_click(')'))
btn_point = Button(root, text='.', padx=40, pady=20, command=lambda: btn_click('.'))

btn_plus = Button(root, text='+', padx=39, pady = 20, command=lambda: btn_click('+'))
btn_minus = Button(root, text='-', padx = 40, pady = 20, command=lambda: btn_click('-'))
btn_multiply = Button(root, text='*', padx = 40, pady = 20, command=lambda: btn_click('*'))
btn_div = Button(root, text='/', padx = 40, pady = 20, command=lambda: btn_click('/'))
btn_clear = Button(root, text='C', padx = 39, pady = 20, command=lambda: btn_click('c'))
btn_calculate = Button(root, text='=', padx = 39, pady = 20, command=lambda: btn_click('='))
btn_del_one = Button(root, text='←', padx=39, pady=20, command=lambda: btn_click('del'))

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
btn_skobka1.grid(row=4, column=1)
btn_skobka2.grid(row=4, column=2)

btn_plus.grid(row=1, column=3)
btn_minus.grid(row=2, column=3)
btn_multiply.grid(row=3, column=3)
btn_div.grid(row=4, column=3)
btn_calculate.grid(row=5, column=0)
btn_clear.grid(row=5, column=1)
btn_point.grid(row=5, column=2)
btn_del_one.grid(row=5, column=3)

root.mainloop()
