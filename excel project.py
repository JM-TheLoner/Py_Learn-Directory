# import openpyxl as xl   #package for working on excel spreadsheets
 
# def new_prices(filename):
#     wb = xl.load_workbook(filename)   #loads the workbook
#     sheet = wb["Sheet1"]   #Assigns "Sheet1" to "sheet" and use capital "S"
#     cell = sheet["a1"]  #or sheet.cell(1, 1)---(row, column)--- returns same thing..... this line is just for demonstrations
#                         #cell.value - self explanatory
#                         #sheet.max_row - number of rows
#                         #sheet.max_column - number of columns

#     for row in range(2, sheet.max_row + 1):     #we use 2 cuz we dont want to use the first rows string value
#         cell = sheet.cell(row, 3)
#         new_price = cell.value * 0.9
#         new_price_cell = sheet.cell(row, 4)
#         new_price_cell.value = (f"${new_price}")
#         empty = sheet.cell(row, 5)
#         empty.value = ""
#     name = sheet.cell(1, 4)             
#     name.value = ("new prices")    
#     new = sheet.cell(1, 5)     
#     new.value = ""


#     #to make a chart
#     from openpyxl.chart import BarChart, Reference

#     values = Reference(sheet, 
#     min_row = 2, 
#     max_row = sheet.max_row, 
#     min_col = 3, 
#     max_col = 3)

#     chart = BarChart()
#     chart.add_data(values)
#     sheet.add_chart(chart, "a9")

#     wb.save(filename)

from pathlib import Path

path = Path("Py_Learn Directory")
for file in path.glob("*.xlsx"):
    print(file)
    