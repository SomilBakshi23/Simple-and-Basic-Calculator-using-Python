import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="black")

equation = ""

label_result = tk.Label(root, width=25, height=2, font=('arial', 30, 'bold'), anchor='se', text="0", bg="white", fg="black")
label_result.pack()

def show(value):
    global equation
    equation += str(value)
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text="0") 

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except Exception:
            result = "error"
            equation = ""
    label_result.config(text=result)
              




tk.Button(root, text="c", width=5, height=1, font=('arial', 30, 'bold'),bd=1, bg="#3697f5", fg="#fff",command=lambda:  clear()).place(x=10, y=100)  # Corrected color code
tk.Button(root, text="/", width=5, height=1, font=('arial', 30, 'bold'),bd=1, bg="#2a2d36", fg="#fff",command=lambda: show("/")).place(x=150, y=100)
tk.Button(root, text="%", width=5, height=1, font=('arial', 30, 'bold'),bd=1, bg="#2a2d36", fg="#fff",command=lambda: show("%")).place(x=290, y=100)
tk.Button(root, text="*", width=5, height=1, font=('arial', 30, 'bold'),bd=1, bg="#2a2d36", fg="#fff",command=lambda: show("*")).place(x=430, y=100)  # Corrected placement

tk.Button(root, text="7", width=5, height=1, font=('arial', 30, 'bold'),bd=1, bg="#2a2d36", fg="#fff",command=lambda: show("7")).place(x=10, y=200)
tk.Button(root, text="8", width=5, height=1, font=('arial', 30, 'bold'),bd=1, bg="#2a2d36", fg="#fff",command=lambda: show("8")).place(x=150, y=200)
tk.Button(root, text="9", width=5, height=1, font=('arial', 30, 'bold'),bd=1, bg="#2a2d36", fg="#fff",command=lambda: show("9")).place(x=290, y=200) 
tk.Button(root, text="-", width=5, height=1, font=('arial', 30, 'bold'),bd=1, bg="#2a2d36", fg="#fff",command=lambda: show("-")).place(x=430, y=200)

tk.Button(root, text="4", width=5, height=1, font=('arial', 30, 'bold'),bd=1, bg="#2a2d36", fg="#fff",command=lambda: show("4")).place(x=10, y=300)
tk.Button(root, text="5", width=5, height=1, font=('arial', 30, 'bold'),bd=1, bg="#2a2d36", fg="#fff",command=lambda: show("5")).place(x=150, y=300)
tk.Button(root, text="6", width=5, height=1, font=('arial', 30, 'bold'),bd=1, bg="#2a2d36", fg="#fff",command=lambda: show("6")).place(x=290, y=300) 
tk.Button(root, text="+", width=5, height=1, font=('arial', 30, 'bold'),bd=1, bg="#2a2d36", fg="#fff",command=lambda: show("+")).place(x=430, y=300)

tk.Button(root, text="1", width=5, height=1, font=('arial', 30, 'bold'),bd=1, bg="#2a2d36", fg="#fff",command=lambda: show("1")).place(x=10, y=400)
tk.Button(root, text="2", width=5, height=1, font=('arial', 30, 'bold'),bd=1, bg="#2a2d36", fg="#fff",command=lambda: show("2")).place(x=150, y=400)
tk.Button(root, text="3", width=5, height=1, font=('arial', 30, 'bold'),bd=1, bg="#2a2d36", fg="#fff",command=lambda: show("3")).place(x=290, y=400) 
tk.Button(root, text="0", width=11, height=1, font=('arial', 30, 'bold'),bd=1, bg="#2a2d36", fg="#fff",command=lambda: show("0")).place(x=10, y=500)

tk.Button(root, text=".", width=5, height=1, font=('arial', 30, 'bold'),bd=1, bg="#2a2d36", fg="#fff",command=lambda: show(".")).place(x=290, y=500) 
tk.Button(root, text="=", width=5, height=3, font=('arial', 30, 'bold'),bd=1, bg="orange", fg="#fff",command=lambda: calculate()).place(x=430, y=400)
 

root.mainloop()
