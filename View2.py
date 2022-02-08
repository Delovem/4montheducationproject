import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as mb
from Model import Product

#ГУИ ТУТ
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

        #поле
        self.field = tk.Text(parent, height=40, width=72, wrap='word')
        self.field.grid(row=5, column=0, columnspan=5)


        #надписи
        self.label1 = tk.Label(parent, text="наименование:")
        self.label1.grid(row=0, column=0, stick='we')
        self.label1 = tk.Label(parent, text="цена:")
        self.label1.grid(row=1, column=0, stick='we')
        self.label1 = tk.Label(parent, text="количество:")
        self.label1.grid(row=2, column=0, stick='we')

        #поля ввода
        self.entry1 = tk.Entry(parent)
        self.entry1.grid(row=0, column=1, columnspan=1, stick='we')
        self.entry2 = tk.Entry(parent)
        self.entry2.grid(row=1, column=1, columnspan=1, stick='we')
        self.entry3 = tk.Entry(parent)
        self.entry3.grid(row=2, column=1, columnspan=1, stick='we')

        #кнопки
        self.button1 = tk.Button(parent, text='Добавить', command=self.add_product_to_bd)
        self.button1.grid(row=3, column=0, columnspan=2, stick='we')

        self.button2 = tk.Button(parent, text='Удалить')
        self.button2.grid(row=4, column=0, columnspan=2, stick='we')

        self.button3 = tk.Button(parent, text='Импорт', command=self.open_file)
        self.button3.grid(row=0, column=2, columnspan=3, stick='we')

        self.button4 = tk.Button(parent, text='Поиск')
        self.button4.grid(row=1, column=2, columnspan=3, stick='we')

        self.button5 = tk.Button(parent, text='Вывод')
        self.button5.grid(row=2, column=2, columnspan=3, rowspan=3, sticky='nswe')

        self.button6 = tk.Button(parent, text='О программе', command=self.about_soft)
        self.button6.grid(row=6, column=0, stick='we')

        self.button7 = tk.Button(parent, text='Закрыть', command=self.close_window)
        self.button7.grid(row=6, column=3, columnspan=2, stick='we')

        #полоса прокрутки
        self.scroller1 = tk.Scrollbar(parent, command=self.field.yview)
        self.scroller1.grid(row=4, column=5, rowspan=5, stick='ns')



    def open_file(self):
        """диалоговое окно для выбора файла"""
        return askopenfilename()

    def close_window(self):
        """закрывает окно"""
        self.parent.destroy()

    def about_soft(self):
        """информационное окно"""
        mb.showinfo(
            title="О Программе",
            message='Версия 0.1 beta'
                    '\n  '
                    '\nИсходный код: https://github.com/Delovem/4montheducationproject'
                    '\n  '
                    '\nДанная программа является учебным проектом и разработана в рамках обучения в компании Forgstream на курсе "Основы Python Сентябрь" в 2021 году'
                    '\n  '
                    '\nCopyright (c) Delovem software 2021-2022')


    def get_entry1(self):
        entry_value1 = self.entry1.get()
        return entry_value1

    def get_entry2(self):
        entry_value2 = self.entry2.get()
        return entry_value2

    def get_entry3(self):
        entry_value3 = self.entry3.get()
        return entry_value3

    def add_product_to_bd(self):
        name = self.get_entry1()
        price = self.get_entry2()
        count = self.get_entry3()

        new_product = Product(name, price, count)
        new_product.add_product()

# параметры окна
win = tk.Tk()
win.geometry('600x800')
win.title('bazaar v0.1 beta')
icon = tk.PhotoImage(file='icon.png') # на иконке нарисован пакетик
win.iconphoto(False, icon)
win.resizable(False, False) # выключил масштабирование окна, на данном этапе оно не нужно.
MainApplicationView(win).grid()
win.mainloop()
