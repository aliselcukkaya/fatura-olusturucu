from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from excel_islemleri import ExcelIslemleri
import datetime
import time


class VeriGiris:
    def veri_gir(f, py_sheet, driver):
        excel_islemleri = ExcelIslemleri()
        for satir in range(1,py_sheet.nrows):

            if excel_islemleri.veri_okuma(f, py_sheet, satir) == 1:
                return 1

            if excel_islemleri.veri_duzenleme(f) == 1:
                return 1

            try:
                #tarih
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'ui-datepicker-trigger')))
                driver.find_element_by_class_name('ui-datepicker-trigger').click()
                time.sleep(0.5)
                #yil
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'ui-datepicker-year')))
                select_year = Select(driver.find_element_by_class_name('ui-datepicker-year'))
                select_year.select_by_value(str(excel_islemleri.yil))
                time.sleep(0.5)
                #ay
                select_month = Select(driver.find_element_by_class_name('ui-datepicker-month'))
                select_month.select_by_value(str(excel_islemleri.ay - 1))#site kodlarında değerler 0 dan başlıyor
                time.sleep(0.5)
                #gun
                driver.find_element_by_link_text(str(excel_islemleri.gun)).click()
                time.sleep(0.5)
            except:
                f.write("\nTarih girerken sorun oluştu.")
                return 1

            try:
                #saat
                #WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'date-gen__1027')))
                saat_box = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/fieldset/table/tr[4]/td[2]/div/input')
                saat_box.send_keys(excel_islemleri.saat)
                #kontrol
                sayac = 0
                time.sleep(1)
                while(saat_box.get_attribute('value') != (str(excel_islemleri.tarih_format.hour).zfill(2) + ':' + str(excel_islemleri.tarih_format.minute).zfill(2) + ':' + str(excel_islemleri.tarih_format.second).zfill(2)) and sayac < 5):
                    saat_box.send_keys(excel_islemleri.saat)
                    sayac +=1
                    time.sleep(1)
                if(sayac == 5):
                    f.write("\n#####saat_box girilemedi#####")
                    return 1
                    
                time.sleep(0.5)

            except:
                f.write("\nSaat girerken sorun oluştu.")
                return 1


            try:
                #tc
                #WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'gen__1033')))
                tc_box = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/fieldset/table/tr[1]/td[2]/input')
                tc_box.send_keys('11111111111')
                #kontrol
                sayac = 0
                while(tc_box.get_attribute('value') != '11111111111' and sayac < 5):
                    time.sleep(1)
                    tc_box.send_keys('11111111111')
                    sayac +=1
                if(sayac == 5):
                    f.write("\n#####tc_box girilemedi#####")
                    return 1

                time.sleep(0.25)

                
                #ad
                #WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'gen__1035')))
                ad_box = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/fieldset/table/tr[3]/td[2]/input')
                ad_box.send_keys(excel_islemleri.ad)
                #kontrol
                sayac = 0
                time.sleep(1)
                while(ad_box.get_attribute('value') != excel_islemleri.ad and sayac < 5):
                    ad_box.send_keys(excel_islemleri.ad)
                    sayac +=1
                    time.sleep(1)
                if(sayac == 5):
                    f.write("\n#####ad_box girilemedi#####")
                    return 1
                
                time.sleep(0.5)

                #soyad
                #WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'gen__1036')))
                soyad_box = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/fieldset/table/tr[4]/td[2]/input')
                soyad_box.send_keys(excel_islemleri.soyad)
                #kontrol
                sayac = 0
                while(soyad_box.get_attribute('value') != excel_islemleri.soyad and sayac < 5):
                    time.sleep(1)
                    soyad_box.send_keys(excel_islemleri.soyad)
                    sayac += 1
                if(sayac == 5):
                    f.write("\n#####soyad_box girilemedi#####")
                    return 1
                
                time.sleep(0.25)


                #ulke
                #WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'gen__1042-i')))
                ulke_box = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/fieldset/table/tr[6]/td[2]/select')
                ulke_box.send_keys('Türkiye')
                #kontrol
                sayac = 0
                while(ulke_box.get_attribute('value') != 'Türkiye' and sayac < 5):
                    time.sleep(1)
                    ulke_box.send_keys('Türkiye')
                    sayac +=1
                if(sayac == 5):
                    f.write("\n#####ulke_box girilemedi#####")
                    return 1
                
                time.sleep(0.25)

                #adres kutusuna telefon numarasi
                #WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'gen__1043')))
                adres_box = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/fieldset/table/tr[7]/td[2]/textarea')
                adres_box.send_keys(str(excel_islemleri.telefon))
                #kontrol
                sayac = 0
                while(adres_box.get_attribute('value') != str(excel_islemleri.telefon) and sayac < 5):
                    time.sleep(1)
                    adres_box.send_keys(str(excel_islemleri.telefon))
                    sayac +=1
                if(sayac == 5):
                    f.write("\n#####adres_box girilemedi#####")
                    return 1

                time.sleep(0.25)

            except:
                f.write("\nFormun üst kısmını girerken sorun oluştu.")
                return 1

            try:
                #satir ekle
                #WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'gen__1093')))
                driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[3]/div/div/fieldset/div/div[3]/div/div/div/div[1]/div/div/input').click()
                #time.sleep(0.25)

                #hizmet adi
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[3]/div/div/fieldset/div/div[2]/div/div/table/tbody/tr[1]/td[4]/input')))
                hizmet_adi_box = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[3]/div/div/fieldset/div/div[2]/div/div/table/tbody/tr[1]/td[4]/input')
                hizmet_adi_box.send_keys(excel_islemleri.urunisim)
                #kontrol
                sayac = 0
                while(hizmet_adi_box.get_attribute('value') != excel_islemleri.urunisim and sayac < 5):
                    time.sleep(1)
                    hizmet_adi_box.send_keys(excel_islemleri.urunisim)
                    sayac += 1
                if(sayac == 5):
                    f.write("\n#####hizmet_adi_box girilemedi#####")
                    return 1

                time.sleep(0.25)

                #adet
                adet_box = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[3]/div/div/fieldset/div/div[2]/div/div/table/tbody/tr[1]/td[5]/input')
                adet_box.clear()
                adet_box.send_keys('1')
                #kontrol
                sayac = 0
                while(adet_box.get_attribute('value') != '1' and sayac < 5):
                    time.sleep(1)
                    adet_box.send_keys('1')
                    sayac += 1
                if(sayac == 5):
                    f.write("\n#####adet_box girilemedi#####")
                    return 1

                time.sleep(0.25)

                #birim
                birim_box = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[3]/div/div/fieldset/div/div[2]/div/div/table/tbody/tr[1]/td[6]/select')
                birim_box.send_keys('adet')
                birim_box.send_keys(Keys.RETURN)
                #kontrol
                sayac = 0
                while(birim_box.get_attribute('value') != 'C62' and sayac < 5):
                    time.sleep(1)
                    birim_box.send_keys('adet')
                    birim_box.send_keys(Keys.RETURN)
                    sayac += 1
                if(sayac == 5):
                    f.write("\n#####birim_box girilemedi#####")
                    return 1

                time.sleep(0.25)

                #fiyat
                fiyat_box = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[3]/div/div/fieldset/div/div[2]/div/div/table/tbody/tr[1]/td[7]/input')
                fiyat_box.clear()
                fiyat_box.send_keys(str(excel_islemleri.fiyat).replace('.', ','))
                #kontrol
                sayac = 0
                while(fiyat_box.get_attribute('value') != (str(excel_islemleri.fiyat).replace('.', ',')) and sayac < 5):
                    time.sleep(1)
                    fiyat_box.clear()
                    fiyat_box.send_keys(str(excel_islemleri.fiyat).replace('.', ','))
                    sayac += 1
                if(sayac == 5):
                    f.write("\n#####fiyat_box girilemedi#####")
                    return 1

                time.sleep(0.25)

                #kdv orani
                kdv_box = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[3]/div/div/fieldset/div/div[2]/div/div/table/tbody/tr[1]/td[11]/select')
                kdv_box.send_keys('18')
                kdv_box.send_keys(Keys.RETURN)
                #kontrol
                sayac = 0
                while(kdv_box.get_attribute('value') != '18' and sayac < 5):
                    time.sleep(1)
                    kdv_box.send_keys('18')
                    kdv_box.send_keys(Keys.RETURN)
                    sayac += 1
                if(sayac == 5):
                    f.write("\n#####kdv_box girilemedi#####")
                    return 1

                time.sleep(0.25)
            except:
                f.write("\nSatır ekleme ve sonrasında sorun oluştu.")
                return 1

            time.sleep(1)
            
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[6]/div/div/div/div[1]/div/div/div/div/div/div/input').click()
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/input').click()
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/ul/li[2]/ul/li[1]/a').click()