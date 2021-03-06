import xlrd

from ebookmain.utils.search_data import SearchData


class ExcelReader:

    @staticmethod
    def get_data():
        wb = xlrd.open_workbook("../utils/Zeszyt1.xls")
        sheet = wb.sheet_by_index(0)
        data = []
        for i in range(1, sheet.nrows):
            search_data = SearchData(sheet.cell(i, 0).value)
            data.append(search_data)
        return data
