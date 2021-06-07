# coding=utf-8
import os
import xlwings as xw
from django.db.models import Sum
import matplotlib.pyplot as plt
from apps.simulate_test.models import Test, Result, User


def drawBarPicture():
    cnt = []
    for i in range(4):
        cnt.append(Result.objects.filter(result=i).count())

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    name_list = ['无症状','轻度焦虑', '中度焦虑', '重度焦虑']
    plt.bar(range(len(cnt)), cnt, tick_label=name_list)

    now = os.getcwd()
    plt.savefig(os.path.dirname(now) + '\\static\\images\\img.png')  # 保存图片
    plt.show()


def saveStudentsInExcel():

    results = Result.objects.filter(result=3).order_by('-score')
    app = xw.App(visible=True, add_book=False)
    wb = app.books.add()

    wb.sheets.add('重度焦虑学生')
    sheet = wb.sheets['重度焦虑学生']
    sheet.range('A1').value = '学号'
    sheet.range('B1').value = '姓名'
    sheet.range('C1').value = '得分'

    i = 1
    for res in results:
        i += 1
        sheet.range('A' + i.__str__()).value = res.tuser.id
        sheet.range('B' + i.__str__()).value = User.objects.filter(id=res.tuser.id)[0].name
        sheet.range('C' + i.__str__()).value = float(res.score)
    sheet.range("A:C").autofit()

    sheet = wb.sheets['sheet1']
    sheet.delete()
    wb.save('SeriusStudents.xlsx')
    wb.close()
    app.quit()


def analysis():
    tests = Test.objects.values('tuser').annotate(total=Sum('option'))

    for t in tests:
        x = t['total'] * 1.25
        type = 0
        if x >= 50 and x <= 59:
            type = 1
        elif x >= 60 and x <= 69:
            type = 2
        elif x > 69:
            type = 3

        Result.objects.create(tuser_id =t['tuser'], score=x, result=type)


if __name__ == '__main__':
    analysis()
    saveStudentsInExcel()
    drawBarPicture()
