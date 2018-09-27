import pymysql

global ID
ID = input("请输入用户ID:")

# 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
db = pymysql.connect("10.3.2.37", "ifa", "Ifa1234qwer", "ifa")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = "SELECT * FROM tb_employee WHERE id=ID;"

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        name = row[1]
        type = row[21]
        if type == 0:
            print("该账号未注册")
            input("是否修改为注册状态，是请输入3，退出请输入ctl+c:")
            sql1 = "UPDATE tb_employee SET type = 3 WHERE id = ID"
            try:
                # 执行SQL语句
                cursor.execute(sql1)
                # 提交到数据库执行
                db.commit()
            except:
                # 发生错误时回滚
                db.rollback()
            print("操作成功")

        elif type == 3:
            print("该账号已注册")
            input("是否修改为未注册状态，是请输入0,退出请输入ctl+c:")
            sql2 = "UPDATE tb_employee SET type = 0 WHERE id = ID"
            try:
                # 执行SQL语句
                cursor.execute(sql2)
                # 提交到数据库执行
                db.commit()
            except:
                # 发生错误时回滚
                db.rollback()
            print("操作成功")

except:
    print("Error: unable to fecth data")

# 关闭数据库连接
db.close()
