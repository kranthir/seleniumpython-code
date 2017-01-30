from xlrd import open_workbook

wb = open_workbook('C:\Users\ChandrashekarChary\Desktop\data.xlsx')
for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols

    items = []
    rows = []
    for row in range(1, number_of_rows):
        values = []
        for col in range(number_of_columns):
            value  = (sheet.cell(row,col).value)
            try:
                value = str(int(value))
            except ValueError:
                pass
            finally:
                values.append(value)
        item = str(*values)
        items.append(item)
print items.__len__()
print len(items)
print items[1]


