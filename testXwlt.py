import xlwt
workbook = xlwt.Workbook(encoding="utf-8")    # initiate a workbook subject
worksheet = workbook.add_sheet('sheet1')
i = 0
j = 0
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,str(j+1)+"*"+ str(i+1)+"="+str((i+1)*(j+1)))

workbook.save("student.xls")