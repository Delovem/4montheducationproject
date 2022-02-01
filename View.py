import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as mb

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

        self.label = tk.Label(parent, text="Данные:")
        self.label.grid(row=3)

        self.field = tk.Text(win, height=40, width=72, wrap='word')
        self.field.grid(row=4, column=0, columnspan=3)


        self.button1 = tk.Button(text='добавить').grid(row=0, column=0, stick='we')
        self.button11 = tk.Button(text='удалить').grid(row=0, column=1, stick='we')
        self.button12 = tk.Button(text='импорт').grid(row=0, column=2, stick='we')

        self.button2 = tk.Button(text='Показать список').grid(row=1, column=0, columnspan=3,stick='we')

        self.button3 = tk.Button(text='мин').grid(row=2, column=0, stick='we')
        self.button31 = tk.Button(text='макс').grid(row=2, column=1, stick='we')
        self.button32 = tk.Button(text='Поиск?').grid(row=2, column=2, stick='we')


        self.button4 = tk.Button(text='О программе').grid(row=5, column=0, stick='we')
        self.button41 = tk.Button(text='Закрыть').grid(row=5, column=1, columnspan=2, stick='we')

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





