
import tkinter as tk

class MainApplicationView(tk.Frame):
    '''основное окно, кнопки, поля и прочее'''
    def __init__(self, parent, *args, **kwargs):
        '''инициализация класса и содержимое окна
        label - надписи, некликабельные
        field - поле вывода
        button - кнопки
        scroller1 - полоса прокрутки справа от поля field. на win 11 может выглядеть криво

        '''
        tk.Frame.__init__(self,parent, *args, **kwargs)
        self.parent = parent

        self.label = tk.Label(parent, text="Give values")
        self.label.grid(row=1)

        self.field = tk.Text(win, height=45, width=72, wrap='word')
        self.field.grid(row=3, column=0, columnspan=3)

        self.button1 = tk.Button(text='...').grid(row=0, column=2, stick='we')
        self.button2 = tk.Button(text='Готово').grid(row=1, column=2,stick='we')
        self.button3 = tk.Button(text='О программе').grid(row=4, column=0, stick='we')
        self.button4 = tk.Button(text='Закрыть').grid(row=4, column=1, columnspan=2, stick='we')

        self.scroller1 = tk.Scrollbar(win, command=self.field.yview)
        self.scroller1.grid(row=2, column=3, rowspan=2, columnspan=2, stick='ns')



# параметры окна
win = tk.Tk()
win.geometry('600x800')
win.title('bazaar v0.1 beta')
icon = tk.PhotoImage(file='icon.png') # на иконке нарисован пакетик
win.iconphoto(False, icon)
win.title('bazaar v0.1 beta')
win.resizable(False, False) # выключил масштабирование окна, на данном этапе оно не нужно.
MainApplicationView(win).grid()
win.mainloop()

# class ProductsGUI():





