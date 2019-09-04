import openpyxl
import random 
xfile = openpyxl.load_workbook('supplier.xlsx')
sheet = xfile.active
# sheet['I1'] = 'Finance'

# ch = 'A'
# for i in range(2,10001):
# 	sheet['I'+str(i)] = random.randint(1, 10)
# xfile.save('supplier.xlsx') 
sheet.delete_cols(2, 1)
xfile.save('supplier.xlsx')