
import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self,parent, *args, **kwargs)
        self.parent = parent

        self.label = tk.Label(parent, text="Give values")
        self.label.grid(row=1)

if __name__ == "__main__":
    win = tk.Tk()
    win.geometry('600x800')
    win.title('bazaar v0.1 beta')
    icon = tk.PhotoImage(file='icon.png')
    win.iconphoto(False, icon)
    win.title('bazaar v0.1 beta')
    win.resizable(False, False)
    MainApplication(win).grid
    win.mainloop()

# class ProductsGUI():





