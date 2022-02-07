import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as mb


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

        self.label = tk.Label(parent, text="Данные:")
        self.label.grid(row=3)

        self.field = tk.Text(parent, height=40, width=72, wrap='word')
        self.field.grid(row=4, column=0, columnspan=3)

        #первый ряд кнопок
        self.button1 = tk.Button(parent, text='добавить')
        self.button11 = tk.Button(parent, text='удалить')
        self.button12 = tk.Button(parent, text='импорт')
        #размещение первого ряда
        self.button1.grid(row=0, column=0, stick='we')
        self.button11.grid(row=0, column=1, stick='we')
        self.button12.grid(row=0, column=2, stick='we')

        #второй ряд
        self.button2 = tk.Button(parent, text='Показать список')
        self.button2.grid(row=1, column=0, columnspan=3,stick='we')

        # третий ряд
        self.button3 = tk.Button(parent, text='мин').grid(row=2, column=0, stick='we')
        self.button31 = tk.Button(parent, text='макс').grid(row=2, column=1, stick='we')
        self.button32 = tk.Button(parent, text='Поиск?').grid(row=2, column=2, stick='we')

        # Четвертный ряд
        self.button4 = tk.Button(parent, text='О программе')
        self.button41 = tk.Button(parent, text='Закрыть')

        # размещение четверого ряда
        self.button4.grid(row=5, column=0, stick='we')
        self.button41.grid(row=5, column=1, columnspan=2, stick='we')

        self.scroller1 = tk.Scrollbar(parent, command=self.field.yview)
        self.scroller1.grid(row=2, column=3, rowspan=2, columnspan=2, stick='ns')

        #привязка действий:
        self.button1.bind("<Button-1>", self.create_window)
        #открыть файл
        self.button12.bind("<Button-1>", self.open_file)
        #закрыть окно
        self.button41.bind("<Button-1>", self.close_window)
        #информационное окно
        self.button4.bind("<Button-1>", self.about_soft)

    def create_window(self, event):
        '''второе окно'''
        win2 = tk.Toplevel(win)
        win2.geometry('220x95')
        win.title('bazaar v0.1 beta')

        icon = tk.PhotoImage(file='icon.png')  # на иконке нарисован пакетик
        win.iconphoto(False, icon)
        win.resizable(False, False)  # вы

        def get_entry():
            entry_value1 = win2entry_1.get()
            entry_value2 = win2entry_2.get()
            entry_value3 = win2entry_3.get()

            return entry_value1, entry_value2, entry_value3

        def close_window():
            """закрывает окно"""
            win2.destroy()

        win2label_1 = tk.Label(win2, text='Наименование').grid(row=0, column=0)
        win2label_2 = tk.Label(win2, text='Цена').grid(row=1, column=0)
        win2label_3 = tk.Label(win2, text='Колво').grid(row=2, column=0)

        win2entry_1 = tk.Entry(win2)
        win2entry_1.grid(row=0, column=1, stick='we')
        win2entry_2 = tk.Entry(win2)
        win2entry_2.grid(row=1, column=1, stick='we')
        win2entry_3 = tk.Entry(win2)
        win2entry_3.grid(row=2, column=1, stick='we')

        win2button_1 = tk.Button(win2, text='отмена', command=close_window)
        win2button_1.grid(row=3, column=0, stick='we')
        win2button_2 = tk.Button(win2, text='Готово', command=get_entry)
        win2button_2.grid(row=3, column=1, stick='we')







    def open_file(self, event):
        """диалоговое окно для выбора файла"""
        return askopenfilename()

    def close_window(self, event):
        """закрывает окно"""
        self.parent.destroy()

    def about_soft(self, event):
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





# параметры окна
win = tk.Tk()
win.geometry('600x800')
win.title('bazaar v0.1 beta')
icon = tk.PhotoImage(file='icon.png') # на иконке нарисован пакетик
win.iconphoto(False, icon)
win.resizable(False, False) # выключил масштабирование окна, на данном этапе оно не нужно.
MainApplicationView(win).grid()
win.mainloop()







