import os
import xlrd

class Dosya:
    def dosya_oku(f, file_name):
        try:
            py_sheet = xlrd.open_workbook(file_name).sheet_by_index(0)
            dir_path = os.path.dirname(os.path.realpath(__file__))
            config = 'config.txt'
            with open(os.path.join(dir_path, config), "r", encoding="utf-8") as file:
                data = file.readlines()
            return py_sheet, data
        except:
            f.write("Dosya islemlerinde sorun olustu!")
            return 1, 1