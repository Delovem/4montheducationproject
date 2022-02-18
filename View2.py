import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as mb

import Model
from Model import Product

import logging
import datetime

#logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('MyLog')


# ГУИ ТУТ
class MainApplicationView(tk.Frame):
    """основное окно, кнопки, поля и прочее"""

    def __init__(self, parent, *args, **kwargs):
        """инициализация класса и содержимое окна
        label - надписи, некликабельные
        field - поле вывода
        button - кнопки
        scroller1 - полоса прокрутки справа от поля field. на win 11 может выглядеть криво

        """
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # поле
        self.field = tk.Text(parent, height=39, width=72, wrap='word')
        self.field.grid(row=6, column=0, columnspan=5)

        # надписи
        self.label1 = tk.Label(parent, text="наименование:")
        self.label1.grid(row=0, column=0, stick='we')
        self.label2 = tk.Label(parent, text="цена:")
        self.label2.grid(row=1, column=0, stick='we')
        self.label3 = tk.Label(parent, text="количество:")
        self.label3.grid(row=2, column=0, stick='we')
        self.label4 = tk.Label(parent, text='Сортировать:')
        self.label4.grid(row=5, column=0, sticky='we')

        # поля ввода
        self.entry1 = tk.Entry(parent)
        self.entry1.grid(row=0, column=1, columnspan=1, stick='we')
        self.entry2 = tk.Entry(parent)
        self.entry2.grid(row=1, column=1, columnspan=1, stick='we')
        self.entry3 = tk.Entry(parent)
        self.entry3.grid(row=2, column=1, columnspan=1, stick='we')

        # кнопки
        self.button1 = tk.Button(parent, text='Добавить', command=self.add_product_to_bd)
        self.button1.grid(row=3, column=0, columnspan=2, stick='we')

        self.button2 = tk.Button(parent, text='Удалить', command=self.delete_product_from_bd)
        self.button2.grid(row=4, column=0, columnspan=2, stick='we')

        self.button3 = tk.Button(parent, text='Поиск', command=self.search_by_name)
        self.button3.grid(row=0, column=2, columnspan=3, stick='we')

        self.button4 = tk.Button(parent, text='Импорт', command=self.open_file)
        self.button4.grid(row=1, column=2, columnspan=3, stick='we')

        self.button5 = tk.Button(parent, text='Вывод', command=self.field_output)
        self.button5.grid(row=2, column=2, columnspan=3, rowspan=3, sticky='nswe')

        self.button6 = tk.Button(parent, text='О программе', command=self.about_soft)
        self.button6.grid(row=7, column=0, stick='we')

        self.button7 = tk.Button(parent, text='Закрыть', command=self.close_window)
        self.button7.grid(row=7, column=3, columnspan=2, stick='we')

        self.button8 = tk.Button(parent, text='цена \/', command=self.sort_by_price_desc)
        self.button8.grid(row=5, column=1, sticky='we')

        self.button9 = tk.Button(parent, text='цена /\\', command=self.sort_by_price_asc)
        self.button9.grid(row=5, column=2, sticky='we')

        self.button10 = tk.Button(parent, text='кол-во \/', command=self.sort_by_count_desc)
        self.button10.grid(row=5, column=3, sticky='we')

        self.button11 = tk.Button(parent, text='кол-во /\\', command=self.sort_by_count_asc)
        self.button11.grid(row=5, column=4, sticky='we')

        # полоса прокрутки
        self.scroller1 = tk.Scrollbar(parent, command=self.field.yview)
        self.scroller1.grid(row=4, column=5, rowspan=5, stick='ns')

    def open_file(self):
        """диалоговое окно для выбора файла"""
        askopenfilename()

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
                    '\nДанная программа является учебным проектом и разработана в рамках обучения в компании '
                    'Forgstream на курсе "Основы Python Сентябрь" в 2021 году '
                    '\n  '
                    '\nCopyright (c) Delovem software 2021-2022')

    # 3 функции для захвата текста с полей ввода
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
        """создает экземпляр класса Product и сразу добавляет в таблицу в БД"""
        name = self.get_entry1()
        price = self.get_entry2()
        count = self.get_entry3()

        if price.isdigit() == False:
            msg = 'В поле цена должно быть целое число'
            mb.showwarning("Предупреждение", msg)

        if count.isdigit() == False:
            msg = 'В поле колво должно быть целое число'
            mb.showwarning("Предупреждение", msg)

        new_product = Product(name, price, count)
        new_product.add_product()
        Model.session.commit()

        logger.info(f'{datetime.datetime.now()} Product {new_product.name} added')

    def delete_product_from_bd(self):
        """удаляет из БД по имени введенному в entry1 (Наименование, Product.title)"""

        name = self.get_entry1()

        if name == '':
            msg = ' введите наименование'
            mb.showwarning("Предупреждение", msg)

        i = Model.session.query(Model.DBproduct).filter(Model.DBproduct.title == name).one()
        Model.session.delete(i)
        Model.session.commit()

        logger.info(f'{datetime.datetime.now()} Product {name} deleted')

    def field_output(self):
        """выводит таблицу из БД в поле field"""
        textoutput = Model.session.query(Model.DBproduct).all()
        Model.session.commit()
        self.field.delete(1.0, tk.END)
        self.field.insert(1.0, textoutput)

    def search_by_name(self):
        """поиск по значению с поля ввода entry1 (наименование, Product.title)
        РАБОТАЕТ по нажатию на кнопку поиск, если что-нибудь введено в поле etnry1"""
        self.entry2.delete(0, tk.END)  # очистка поля ввода цена
        self.entry3.delete(0, tk.END)  # очистка поля ввода колво
        name = self.get_entry1()
        textoutput = Model.session.query(Model.DBproduct).filter(Model.DBproduct.title == name).all()
        self.field.delete(1.0, tk.END)
        self.field.insert(1.0, (textoutput))

    def search_by_count(self):
        """поиск по значению с поля ввода entry2 (Кол-во, Product.count)
        ПОКА НЕ РАБОТАЕТ"""
        name = self.get_entry2()
        textoutput = Model.session.query(Model.DBproduct).filter(Model.DBproduct.count == name).all()
        self.field.delete(1.0, tk.END)
        self.field.insert(1.0, (textoutput))

    def search_by_price(self):
        """поиск по значению с поля ввода entry3 (Цена, Product.price)
        ПОКА НЕ РАБОТАЕТ"""
        name = self.get_entry3()
        textoutput = Model.session.query(Model.DBproduct).filter(Model.DBproduct.price == name).all()
        self.field.delete(1.0, tk.END)
        self.field.insert(1.0, (textoutput))

    # сортировки
    def sort_by_price_asc(self):
        '''по цене по возрастанию'''
        textoutput = Model.session.query(Model.DBproduct).order_by(Model.DBproduct.price).all()
        self.field.delete(1.0, tk.END)
        self.field.insert(1.0, (textoutput))

    def sort_by_price_desc(self):
        '''по цене по убыванию'''
        textoutput = Model.session.query(Model.DBproduct).order_by(Model.desc(Model.DBproduct.price)).all()
        self.field.delete(1.0, tk.END)
        self.field.insert(1.0, (textoutput))

    def sort_by_count_asc(self):
        '''по количству по возрастанию'''
        textoutput = Model.session.query(Model.DBproduct).order_by(Model.DBproduct.count).all()
        self.field.delete(1.0, tk.END)
        self.field.insert(1.0, (textoutput))

    def sort_by_count_desc(self):
        '''по количеству по убыванию'''
        textoutput = Model.session.query(Model.DBproduct).order_by(Model.desc(Model.DBproduct.count)).all()
        self.field.delete(1.0, tk.END)
        self.field.insert(1.0, (textoutput))


def start_gui():
    '''запуск GUI с заданными параметрами
    geomerty - размер
    title - название
    '''

    win = tk.Tk()
    win.geometry('600x805')
    win.title('bazaar v0.1 beta')
    icon = tk.PhotoImage(file='icon.png')  # на иконке нарисован пакетик
    win.iconphoto(False, icon)
    win.resizable(False, False)  # выключил масштабирование окна, на данном этапе оно не нужно.
    MainApplicationView(win).grid()
    win.mainloop()


if __name__ == "__main__":
    start_gui()
