import xlrd
import time
import datetime

class ExcelIslemleri():
    def __init__(self):
        #bu sütunları kendinize göre ayarlayabilirsiniz
        self.adsoyad_sutun = 0
        self.telefon_sutun = 1
        self.urunisim_sutun = 2
        self.fiyat_sutun = 3
        self.tarih_sutun = 4

        self.fiyat = 0
        self.telefon = 0
        self.urunisim = ""
        self.ad = ""
        self.soyad = ""
        self.yil = 0
        self.ay = 0
        self.gun = 0
        self.saat = ""
        self.tarih_format = ""
    
    def veri_okuma(self, f, py_sheet, satir):
        try:
            #excel veri okuma
            self.adsoyad_string =  py_sheet.cell_value(satir,self.adsoyad_sutun)
            self.telefon = int(py_sheet.cell_value(satir,self.telefon_sutun))
            self.urunisim = py_sheet.cell_value(satir,self.urunisim_sutun)

            #fiyat hesabını kendinize göre ayarlayabilirsiniz
            self.fiyat = int(py_sheet.cell_value(satir,self.fiyat_sutun))
            self.fiyat = self.fiyat/1.18
            self.fiyat = ('%.10f' % self.fiyat)

            self.tarih = py_sheet.cell_value(satir,self.tarih_sutun)
        except:
            f.write("\nExcelden veri okurken sorun oluştu.")
            return 1
    
    def veri_duzenleme(self, f):
        try:
            #adsoyad ayirma
            adsoyad_list = self.adsoyad_string.split(' ')

            self.soyad = adsoyad_list[-1]
            #büyük İ sorununu çözüyor
            try:
                self.soyad = self.soyad.replace('i','İ')
            except:
                pass
            self.soyad = self.soyad.upper()
            adsoyad_list.pop(-1)

            for i in range(len(adsoyad_list)):
                #birden fazla isme sahipse aralarına boşluk koyuyor
                if i >= 1:
                    self.ad = self.ad + ' '
                self.ad = self.ad + adsoyad_list[0]
                adsoyad_list.pop(0)
            self.ad = self.ad.title()
            
            #büyük i ile başlıyorsa
            try:
                self.ad = self.ad.replace('I','İ')
            except:
                pass
        except:
            f.write("\nİsim işlemlerinde sorun oluştu.")
            return 1

        try:
            #tarih ayirma
            self.tarih_format = datetime.datetime.strptime(self.tarih, "%d,%m,%Y  %H:%M:%S")# excelde tarihlerin arasında virgül olması gerek
            self.yil = self.tarih_format.year
            self.ay = self.tarih_format.month
            self.gun = self.tarih_format.day

            self.saat = str(self.tarih_format.hour).zfill(2) + str(self.tarih_format.minute).zfill(2) + str(self.tarih_format.second).zfill(2)
        except:
            f.write("\nTarih işlemlerinde sorun oluştu.")
            return 1

        try:
            #yazdir
            f.write(self.ad + ' ' + self.soyad + ' ' + str(self.fiyat))
            #self.f.write(soyad + ' ' + str(self.fiyat))
            f.write("**********************\n")
        except:
            f.write("\nDosya yazmada sorun oluştu.")
            return 1