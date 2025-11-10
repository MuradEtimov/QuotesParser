import xlsxwriter
from Les1 import aray

def writer(parametr):
    workbook = xlsxwriter.Workbook('Quotes.xlsx')
    worksheet = workbook.add_worksheet("Quotes")

    row = 0
    column = 0

    worksheet.set_column("A:A",20)
    worksheet.set_column("B:B",20)
    worksheet.set_column("C:C", 50)
    worksheet.set_column("D:D", 20)

    for item in parametr:
        worksheet.write(row,column, item[0])
        worksheet.write(row,column + 1, item[1])
        worksheet.write(row,column + 2, item[2])
        worksheet.write(row,column + 3, item[3])
        worksheet.write(row,column + 4, item[4])
        row += 1

    workbook.close()

writer(aray())
    