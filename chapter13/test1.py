import openpyxl

wb = openpyxl.load_workbook('/home/liuzibo/code/python/AutoBoringStuff/chapter13/example.xlsx')
sheet = wb['Sheet1']
print(sheet['A1'].value)