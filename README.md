# PythonLastTest
万本庭老师的《Python程序设计》的期末测试(第二题)

1.项目整体为Django，util里存放纯python代码，执行纯python代码时要选择通过命令行执行

1.建立四个模型类，user，problem，test，result，分别对应四张表，可以通过模型类直接生成

2.randomdata，对于学生，随机生成学号，姓名，对于题目，只需要标号即可(当然也可以不用题目类)，对于test，每个人的选项都大致接近正态分布，但是每个人的均值和方差是不一样的，这里需要控制一下，心理正常的学生肯定占大部分，心理状况越糟糕人数越少

3.analysisdata，先读取test数据计算得到result数据，随后读取result中心理状况最差的学生写入excel，最后统计各类别人数，绘制并保存柱状图

4.网页数据由view内函数获取模型层数据，转换成字典传至前端进行展示，并通过layui进行美化