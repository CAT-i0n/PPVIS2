from tkinter import *
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(2)

class View(Tk):
    def __init__(self, park):
        super().__init__()
        self.park = park    
        root = Toplevel()
        
        root.geometry("1920x1080")
        root.attributes('-fullscreen',True)
        root.minsize(1920, 1080)
        back = PhotoImage(file = "park.png")
        canvas1 = Canvas(root, width = 1920,
                         height = 1080)
        canvas1.pack(fill = "both", expand = True)
        canvas1.create_image(0, 0, image = back, 
                             anchor = "nw")
        canvas1.create_text(960, 30, text = "Welcome", font=('Helvetica','30','bold'))
          
        button1 = Button(root, text = "Начать новую сессию", height = 3, width=20, 
                         command =  self.new_session)
        button2 = Button(root, text = "Загрузить сессию", height = 3, width=20, 
                         command = self.load_session)
        button3 = Button(root, text = "Сохранить и выйти", height = 3, width=20, 
                         command = self.save_and_quit)
        button4 = Button(root, text = "Выйти", height = 3, width=20,
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
        print(root.winfo_screenwidth(), root.winfo_screenheight())
        root.mainloop()
    
    def new_session(self):
        pass
    
    def load_session(self):
        pass
    
    def save_and_quit(self):
        pass
    
    def no_save_quit(self):
        self.destroy()
        