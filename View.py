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
        win2.geometry('300x300')

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
win.title('bazaar v0.1 beta')
win.resizable(False, False) # выключил масштабирование окна, на данном этапе оно не нужно.
MainApplicationView(win).grid()
win.mainloop()







