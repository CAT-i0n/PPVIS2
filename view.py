import tkinter
from tkinter import *
from tkinter import ttk
import ctypes
from random import randint
ctypes.windll.shcore.SetProcessDpiAwareness(2)

class View(Tk):
    def __init__(self, park):
        super().__init__()
        self.park = park    
        self.menu()
        
        
    def menu(self):
        self.root = Toplevel()
        self.root.geometry("1920x1080")
        self.root.attributes('-fullscreen',True)
        self.root.minsize(1920, 1080)
        back = PhotoImage(file = "park.png")
        canvas1 = Canvas(self.root, width = 1920,
                         height = 1080)
        canvas1.pack(fill = "both", expand = True)
        canvas1.create_image(0, 0, image = back, 
                             anchor = "nw")
        canvas1.create_text(960, 30, text = "Главное меню", font=('Helvetica','30','bold'))
          
        def new():
            root = Toplevel()
            root.title("")
            Label(root, text  = "Введите название сессии").grid(row = 0, column = 0)
            e1 = Entry(root)
            e1.grid(row = 1, column = 0)
            def save():
                data = e1.get()
                root.destroy()
                self.park.name = data
                self.show_park_model()
            button1 = Button(root, text = "Ok", command = save)
            button1.grid(row = 2, column = 0)
            root.mainloop()
        button1 = Button(self.root, text = "Начать новую сессию", height = 3, width=20, 
                         command = new)
        button2 = Button(self.root, text = "Загрузить сессию", height = 3, width=20, 
                         command = self.load_session)
        button3 = Button(self.root, text = "Сохранить и выйти", height = 3, width=20, 
                         command = self.save_and_quit)
        button4 = Button(self.root, text = "Выйти", height = 3, width=20,
                         command=self.no_save_quit)
        
        button1_canvas = canvas1.create_window(880, 100, anchor = "nw",
                                               window = button1)
        button2_canvas = canvas1.create_window(880, 200, anchor = "nw",
                                               window = button2)
        button3_canvas = canvas1.create_window(880, 300, anchor = "nw",
                                               window = button3)
        button4_canvas = canvas1.create_window(880, 400, anchor = "nw",
                                               window = button4)
        
        self.lower()
        print(self.root.winfo_screenwidth(), self.root.winfo_screenheight())
        self.root.mainloop()
    
    def show_park_model(self):
        self.root.destroy()
        self.root = Toplevel()
        self.root.geometry("1920x1080")
        self.root.attributes('-fullscreen',True)
        self.root.minsize(1920, 1080)
        back = PhotoImage(file = "park.png")
        canvas1 = Canvas(self.root, width = 1920,
                         height = 1080)
        canvas1.pack(fill = "both", expand = True)
        canvas1.create_image(0, 0, image = back, 
                             anchor = "nw")
        canvas1.create_text(960, 30, text = "Аттракционы и посетители", font=('Helvetica','30','bold'))

        columns = ("",)
        tables = []
        for i in range(0, 6):

            tree = ttk.Treeview(self.root, columns=columns, show='headings', height = 25)
            
            for j,name in enumerate(columns):
                tree.column(name,anchor=CENTER)
                tree.heading(name, text=name)
            
            data = self.park.attractions[i].queue.visitors
            data = [i.id for i in data]
            for record in data:
                tree.insert('', tkinter.END, values=record)
            
            canvas1.create_window(i*300 + 100, 200, anchor = "nw",
                                                   window = tree)
            
            button = Button(self.root, text = self.park.attractions[i].name, 
                            height = 3, width=24, 
                             command = None)
            canvas1.create_window(i*300 + 100, 150, anchor = "nw",
                                                   window = button)
        
        
        button1 = Button(self.root, text = "Добавить посетителя", height = 3, width=20, 
                         command =  self.add_visitor)
        button2 = Button(self.root, text = "Удалить посетителя", height = 3, width=20, 
                         command = self.del_visitor)
        button3 = Button(self.root, text = "Добавить в очередь", height = 3, width=20, 
                         command = self.add_to_queue)
        button4 = Button(self.root, text = "Удалить из очереди", height = 3, width=20,
                         command=self.del_from_queue)
        button5 = Button(self.root, text = "Добавить поездки", height = 3, width=20, 
                         command = self.add_tickets)
        button6 = Button(self.root, text = "Список посетителей", height = 3, width=20,
                         command=self.show_visitors)
        button7 = Button(self.root, text = "Запуск аттракциона", height = 3, width=20,
                         command=self.run_attraction)
        def to_menu():
            self.root.destroy()
            self.menu()
        button8 = Button(self.root, text = "Выход в меню", height = 3, width=20,
                         command= to_menu)
        
        
        button1_canvas = canvas1.create_window(200, 900, anchor = "nw",
                                               window = button1)
        button2_canvas = canvas1.create_window(400, 900, anchor = "nw",
                                               window = button2)
        button3_canvas = canvas1.create_window(600, 900, anchor = "nw",
                                               window = button3)
        button4_canvas = canvas1.create_window(800, 900, anchor = "nw",
                                               window = button4)
        button5_canvas = canvas1.create_window(1000, 900, anchor = "nw",
                                               window = button5)
        button6_canvas = canvas1.create_window(1200, 900, anchor = "nw",
                                               window = button6)
        button7_canvas = canvas1.create_window(1400, 900, anchor = "nw",
                                               window = button7)
        button8_canvas = canvas1.create_window(1600, 900, anchor = "nw",
                                               window = button8)
        
        
        self.lower()
        self.root.mainloop()
    
    def run_attraction(self):
        root = Toplevel()
        root.title("Запустить аттракцион")
        Label(root, text  = "Аттракцион").grid(row = 0, column = 0)
        e2 = ttk.Combobox(root)
        atts = self.park.attractions
        atts = tuple([i.name for i in atts])
        e2['values'] = atts
        e2['state'] = 'readonly'
        e2.grid(row = 0, column = 1)
        def save():
            data = [e2.get()]
            root.destroy()
            self.park.run_attraction(data)
            root2 = Toplevel()
            Label(root2, text  = "аттракцион запущен").grid(row = 0, column = 0)
            button1 = Button(root2, text = "Ок", command = root2.destroy).grid(row = 1, column = 0)
        button1 = Button(root, text = "запустить", command = save)
        button1.grid(row = 2, column = 0)
        root.mainloop()
    
    def add_visitor(self):
        columns = ( "name",
                    "weight",
                    "height",
                    "tickets",
                    )
        root = Toplevel()
        root.title("")
        entries = []
        for i in range(4):
            Label(root, text  = columns[i]).grid(row = i, column = 0)
            e1 = Entry(root)
            e1.grid(row = i, column = 1)
            entries.append(e1)
        def get_data():
            data = []
            for i in entries:
                data.append(i.get())
            root.destroy()
            self.park.add_visitor(data)
            root2 = Toplevel()
            Label(root2, text  = f"Посетитель добавлен, id - {randint(0,10000)}").grid(row = 0, column = 0)
            button1 = Button(root2, text = "Ок", command = root2.destroy).grid(row = 1, column = 0)
            
        button1 = Button(root, text = "Add", command = get_data)
        button1.grid(row = 11, column = 1)
        root.mainloop()
    
    def del_visitor(self):
        root = Toplevel()
        root.title("")
        Label(root, text  = "id").grid(row = 0, column = 0)
        e1 = Entry(root)
        e1.grid(row = 1, column = 0)
        def save():
            root.destroy()
            root2 = Toplevel()
            def end():
                data = e1.get()
                self.park.del_visitor(data)
            Label(root2, text  = "Посетитель удален").grid(row = 0, column = 0)
            button1 = Button(root2, text = "Ок", command = root2.destroy).grid(row = 1, column = 0)
        button1 = Button(root, text = "Удалить", command = save)
        button1.grid(row = 2, column = 0)
        root.mainloop()
    
    def add_to_queue(self):
        root = Toplevel()
        root.title("Добавить в очередь")
        Label(root, text  = "id").grid(row = 0, column = 0)
        Label(root, text  = "Аттракцион").grid(row = 1, column = 0)
        e1 = Entry(root)
        e1.grid(row = 0, column = 1)
        e2 = ttk.Combobox(root)
        atts = self.park.attractions
        atts = tuple([i.name for i in atts])
        
        e2['values'] = atts
        e2['state'] = 'readonly'
        e2.grid(row = 1, column = 1)
        def save():
            data = [e1.get(),e2.get()]
            root.destroy()
            self.park.add_to_queue(data)
            root2 = Toplevel()
            Label(root2, text  = "посетитель добавлен").grid(row = 0, column = 0)
            button1 = Button(root2, text = "Ок", command = root2.destroy).grid(row = 1, column = 0)
        button1 = Button(root, text = "add", command = save)
        button1.grid(row = 2, column = 0)
        root.mainloop()
    
    def del_from_queue(self):
        root = Toplevel()
        root.title("Удалить из очереди")
        Label(root, text  = "id").grid(row = 0, column = 0)
        Label(root, text  = "Аттракцион").grid(row = 1, column = 0)
        e1 = Entry(root)
        e1.grid(row = 0, column = 1)
        e2 = ttk.Combobox(root)
        atts = self.park.attractions
        atts = tuple([i.name for i in atts])
        
        e2['values'] = atts
        e2['state'] = 'readonly'
        e2.grid(row = 1, column = 1)
        def save():
            data = [e1.get(),e2.get()]
            root.destroy()
            self.park.del_from_queue(data)
            root2 = Toplevel()
            Label(root2, text  = "посетитель удален").grid(row = 0, column = 0)
            button1 = Button(root2, text = "Ок", command = root2.destroy).grid(row = 1, column = 0)
        button1 = Button(root, text = "удалить", command = save)
        button1.grid(row = 2, column = 0)
        root.mainloop()
    
    def add_tickets(self):
        root = Toplevel()
        root.title("Добавление поездок")
        Label(root, text  = "id").grid(row = 0, column = 0)
        Label(root, text  = "количество").grid(row = 1, column = 0)
        e1 = Entry(root)
        e1.grid(row = 0, column = 1)
        e2 = Entry(root)
        e2.grid(row = 1, column = 1)
        def save():
            data = [e1.get(),e2.get()]
            root.destroy()
            self.park.add_tickets(data)
            root2 = Toplevel()
            Label(root2, text  = "Поездки добавлены").grid(row = 0, column = 0)
            button1 = Button(root2, text = "Ок", command = root2.destroy).grid(row = 1, column = 0)
        button1 = Button(root, text = "add", command = save)
        button1.grid(row = 2, column = 0)
        root.mainloop()
    
    def show_visitors(self):
        
        root = Toplevel()
        
        root.title('')
        
        
        columns = ( "id",
                    "name",
                    'tickets',
                    "height",
                    "weight",
                    )
        
        tree = ttk.Treeview(root, columns=columns, show='headings')
        
        size = [150,150,150, 150, 150]
        
        root.geometry(f'{sum(size)+20}x225')
        for i,name in enumerate(columns):
            tree.column(name,anchor=CENTER, width=size[i])
            tree.heading(name, text=name)
        
        
        data = self.park.visitors
        data = [(i.id, i.name, i.tickets, i.stats.height, i.stats.weight) for i in data]
        for record in data:
            tree.insert('', tkinter.END, values=record)
            
        tree.grid(row=0, column=0, sticky='ns')
        
        scrollbar = ttk.Scrollbar(root, orient = VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        root.mainloop()
    
    
    def load_session(self):
        root = Toplevel()

        columns = ( "",)
        
        tree = ttk.Treeview(root, columns=columns, show='headings')
        
        root.geometry('150x100')
        for i,name in enumerate(columns):
            tree.column(name,anchor=NW)
            tree.heading(name, text=name)
        
        
        data = (('первое_сохранение'), ('второе_сохранение'), ('третье_сохранение'))
        for record in data:
            tree.insert('', tkinter.END, values=record)

        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']
                self.park.prepare_data(record)
                self.root.destroy()
                root.destroy()
                self.show_park_model()
                
        
        tree.bind('<<TreeviewSelect>>', item_selected)        
        tree.grid(row=0, column=0, sticky='ns')
        
        scrollbar = ttk.Scrollbar(root, orient = VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        root.mainloop()
    
    def save_and_quit(self):
        root = Toplevel()
        root.title("Сохранения")
        Label(root, text  = "Введите название сессии").grid(row = 0, column = 0)
        e1 = Entry(root)
        e1.grid(row = 1, column = 0)
        def save():
            def end():
                data = e1.get()
                root.destroy()
                self.park.save_data(data)
                self.destroy()
            root2 = Toplevel()
            Label(root2, text  = "Сессия сохранена").grid(row = 0, column = 0)
            button1 = Button(root2, text = "Ок", command = end).grid(row = 1, column = 0)
        button1 = Button(root, text = "Cохранить", command = save)
        button1.grid(row = 2, column = 0)
        root.mainloop()
    
    def no_save_quit(self):
        self.destroy()
        
        
        
