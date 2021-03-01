from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Driver:
    def driver(f):
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())

            driver.get("https://earsivportal.efatura.gov.tr/intragiris.html")
            driver.set_window_size(1024, 600)
            driver.maximize_window()
            return driver
        except:
            f.write("\nDriverda sorun oluştu.")
            return 1
