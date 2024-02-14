import xlsxwriter

title_list_2 = [
    "Name",
    "Total HP",
    "Total ATK",
    "Total DEF",
    "Total SPD",
    "Total CRI Rate",
    "Total CRI Dmg",
    "Effective HP"
]
row = 0
col = 0

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

for title in title_list_2:
    worksheet.write(row,col, title)
    col += 1
    
workbook.close()