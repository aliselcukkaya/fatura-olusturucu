import tkinter as tk
from tkinter import filedialog, Text
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import datetime
import os
from driver import Driver
from dosya import Dosya
from site_giris import SiteGiris
from veri_giris import VeriGiris



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(root, height=100, width=150)
        self.canvas.pack()
        self.open_file = tk.Button(root, text="Dosyayı aç", padx=10, pady=5, fg="white", bg="#263D42")
        self.open_file["command"] = self.add_app
        self.open_file.pack()
        self.quit = tk.Button(root, text="Çıkış", fg="white", bg="red",
                              command=self.quit_app)
        self.quit.pack(side="bottom")

    def quit_app(self):
        self.master.destroy()
        self.driver.quit()
        self.f.close()

    def add_app(self):
        self.file_name = filedialog.askopenfilename(initialdir="/", title="Dosya Seç",
        filetypes=[("Excel", ".xls .xlsx")])
        self.fatura_olustur()
    
    def fatura_olustur(self):
        #log dosyasi
        now = datetime.datetime.now()
        now_string = now.strftime("%d %m %Y %H_%M_%S")
        now_string = now_string + '.txt'
        dir_path = os.path.dirname(os.path.realpath(__file__))
        f = open(os.path.join(dir_path, now_string), "w",encoding="utf-8")

        py_sheet, data = Dosya.dosya_oku(f, self.file_name)
        if py_sheet == 1:
            self.quit_app()
        
        self.driver = Driver.driver(f)
        if self.driver == 1:
            self.quit_app()

        site_giris = SiteGiris(f, data, self.driver)
        if site_giris == 1:
            self.quit_app()

        veri_giris = VeriGiris.veri_gir(f, py_sheet, self.driver)
        if veri_giris == 1:
            self.quit_app()

            

root = tk.Tk()
app = Application(master=root)
app.mainloop()