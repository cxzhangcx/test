# coding:utf-8
import xlrd


class ExcelUtil(object):

    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # get titles
        self.row = self.table.row_values(0)
        self.col = self.table.col_values(0)
        # get rows number
        self.rowNum = self.table.nrows
        # get columns number
        self.colNum = self.table.ncols
        # the current column
        self.curRowNo = 1

    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo :
            return False
        else:
            return True

    def next(self):
        r = []
        while self.hasNext():
            s = {}
            col = self.table.row_values(self.curRowNo)
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = col[x]
            r.append(s)
            self.curRowNo += 1
        return r

    def rowlist(self, i):
        # 按行读取存为list,去除空字符
        rowlist = self.table.row_values(i)
        n = rowlist.count("")
        for i in range(n):
            rowlist.remove(u'')
        return rowlist

    def readasdict(self):
        d = {}
        col = self.table.col_values(0)
        nrows = self.table.nrows
        for i in range(nrows):
            val = self.rowlist(i)[1:]
            if len(val) == 1:
                 d[col[i]] = val[0]
            else:
                d[col[i]] = val
        return d

    def readaslitbyrow(self, i, j):
        l = []
        s = self.rowlist(i)
        e = self.rowlist(j)
        for i in range(1, len(s)):
            d = {}
            d[s[0]] = s[i]
            d[e[0]] = e[i]
            l.append(d)
        return l

if __name__=="__main__":
    import config
    import os
    excelPath = os.path.join(config.data_path, "login_data.xlsx")
    excel = ExcelUtil(excelPath, 'myaccount')
    print(excel.readaslitbyrow(2,3))
    print(excel.rowlist(3))
    # u = excel.readasdict()
    # s = u["locator"]
    # for i in s:
    #     print i
