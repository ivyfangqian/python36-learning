import pymysql.cursors

# 创建connection
connection = pymysql.connect(host="127.0.0.1",
                             port=3309,
                             user="root",
                             password="root",
                             db="sales",
                             charset="utf8mb4",
                             autocommit=True,
                             cursorclass=pymysql.cursors.DictCursor
                             )

try:
    # with connection.cursor() as cursor:
    #     sql = "INSERT INTO customer(cusno, cusname, address, tel) VALUES(%s, %s, %s, %s)"
    #     cursor.execute(sql, ("C008", '测试', '成都', '023-18923432'))
    #     cursor.close()
    # connection.commit()


    with connection.cursor() as cursor:
        sql = "SELECT * FROM customer"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
except BaseException as e:
    print("sql执行出错", e)
finally:
    connection.close()


# 在进行增删改时，需要执行完成，执行 connection.commit()提交，才会生效
# 或者可以在获取connection时，设置autocommit=True，执行结束自动提交

# 进行查询时，cursor对象可以设定获取数量
# fetchone()
# fetchmany(size)
# fetchall()


