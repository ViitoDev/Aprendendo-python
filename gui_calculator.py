import tkinter as tk

def click(button):
    if button == "=":
        try:
            result  = str(eval(display.get()))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif button == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, button)

window = tk.Tk()
window.title("GUI Calculator")