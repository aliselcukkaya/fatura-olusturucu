from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SiteGiris:
    def __init__(self, f, data, driver):
        try:
            #panele giriş
            username_box = driver.find_element_by_id('userid')
            username_box.send_keys(data[0])

            password_box = driver.find_element_by_id('password')
            password_box.send_keys(data[1])
            
            driver.find_element_by_css_selector('.btn').click()


            time.sleep(5)
            #e-arsiv portal
            driver.find_element_by_css_selector('#gen__1006 > option:nth-child(2)').click()
            #fatura olustur
            #5000/3000 uzeri fatura olusturma kismina gidiyor
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/ul/li[2]/a')))
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/ul/li[2]/a').click()
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/ul/li[2]/ul/li[1]/a').click()
        except:
            f.write("\nSiteye giriş yaparken sorun oluştu.")
            return 1