import pymysql
class Mysql(object):
    def __init__(self):
        try:
            self.db = pymysql.connect(host="10.0.60.86",user="dba",password="123456",database="test")
            #游标对象
            self.cursor = self.db.cursor()
            print("连接成功！")
        except:
            print("连接失败！")
 	#查询数据函数
    def getdata(self):
        #sql = "select * from xzz_kq order by 单位名称 desc,部门 desc"
        sql = "select id,单位名称,部门,岗位名称,姓名,工号,上班时间,下班时间,create_time from xzz_kq order by create_time desc,单位名称 desc,部门 desc"
        #执行sql语句
        self.cursor.execute(sql)
        #获取所有的记录
        results = self.cursor.fetchall()
        return results

    def getdata_kaoqin(self,results):
        sql = "call test.xuzaizhen_20221118('%s','%s');"% (results['开始日期'],results['结束日期'])
        #sql = "call test.xuzaizhen_20221118('2022-07-01','2022-07-02');"
        #执行sql语句
        self.cursor.execute(sql)
        #获取所有的记录
        results = self.cursor.fetchall()
        return results
    
    def getdata_kaoqin_gonghao(self,results):
        sql = "call test.xuzaizhen_20221118_gonghao('%s','%s','%s');"% (results['开始日期'],results['结束日期'],results['导出员工号'])
        #sql = "call test.xuzaizhen_20221118_gonghao('2022-07-01','2022-07-02','100048');"
        #执行sql语句
        self.cursor.execute(sql)
        #获取所有的记录
        results = self.cursor.fetchall()
        return results

    def insertdata(self,results):
        sql = "insert into xzz_kq(单位名称,部门,岗位名称,姓名,工号,上班时间,下班时间)values('%s','%s','%s','%s','%s','%s','%s')" % (results['单位名称'].strip(),results['部门'].strip(),results['岗位名称'].strip(),results['姓名'].strip(),results['工号'],results['上班时间'].strip(),results['下班时间'].strip())
        sql1 = "ALTER TABLE xzz_kq DROP id"
        sql2 = "ALTER TABLE xzz_kq ADD id int NOT NULL FIRST"
        sql3 = "ALTER TABLE xzz_kq MODIFY COLUMN id int NOT NULL AUTO_INCREMENT,ADD PRIMARY KEY(id)"
        try:
            self.cursor.execute(sql)
            self.cursor.execute(sql1)
            self.cursor.execute(sql2)
            self.cursor.execute(sql3)
            self.db.commit()
        except:
            # 如果发生错误就回滚,建议使用这样发生错误就不会对表数据有影响
            self.db.rollback()
        return

    def updatedata(self,results):
        sql = "update xzz_kq set 单位名称='%s',部门='%s',岗位名称='%s',姓名='%s',工号='%s' where id='%s'" % (results['单位名称'],results['部门'],results['岗位名称'],results['姓名'],results['工号'])
        sql1 = "ALTER TABLE xzz_kq DROP id"
        sql2 = "ALTER TABLE xzz_kq ADD id int NOT NULL FIRST"
        sql3 = "ALTER TABLE xzz_kq MODIFY COLUMN id int NOT NULL AUTO_INCREMENT,ADD PRIMARY KEY(id)"
        try:
            self.cursor.execute(sql)
            self.cursor.execute(sql1)
            self.cursor.execute(sql2)
            self.cursor.execute(sql3)
            self.db.commit()
        except:
            # 如果发生错误就回滚,建议使用这样发生错误就不会对表数据有影响
            self.db.rollback()
        return

    def deletedata(self,id):
        sql = "delete from xzz_kq where id=" + str(id)
        sql1 = "ALTER TABLE xzz_kq_test DROP id"
        sql2 = "ALTER TABLE xzz_kq_test ADD id int NOT NULL FIRST"
        sql3 = "ALTER TABLE xzz_kq_test MODIFY COLUMN id int NOT NULL AUTO_INCREMENT,ADD PRIMARY KEY(id)"
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            self.cursor.execute(sql1)
            self.cursor.execute(sql2)
            self.cursor.execute(sql3)
            # 提交数据
            self.db.commit()
        except:
            # 如果发生错误就回滚,建议使用这样发生错误就不会对表数据有影响
            self.db.rollback()
        return 

    def getdata_lijuan(self):
        sql = "select * from lijuan_kq"
        #执行sql语句
        self.cursor.execute(sql)
        #获取所有的记录
        results = self.cursor.fetchall()
        return results
    
    def getdata_kaoqin_lijuan(self,results):
        sql = "call test.lijuan_20220729('%s','%s');"% (results['开始日期'],results['结束日期'])
        #sql = "call test.lijuan_20220729('2022-07-01','2022-07-02');"
        #执行sql语句
        self.cursor.execute(sql)
        #获取所有的记录
        results = self.cursor.fetchall()
        return results

    def deletedata_lijuan(self,id):
        sql = "delete from lijuan_kq where id=" + str(id)
        sql1 = "ALTER TABLE lijuan_kq DROP id"
        sql2 = "ALTER TABLE lijuan_kq ADD id int NOT NULL FIRST"
        sql3 = "ALTER TABLE lijuan_kq MODIFY COLUMN id int NOT NULL AUTO_INCREMENT,ADD PRIMARY KEY(id)"
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            self.cursor.execute(sql1)
            self.cursor.execute(sql2)
            self.cursor.execute(sql3)
            # 提交数据
            self.db.commit()
        except:
            # 如果发生错误就回滚,建议使用这样发生错误就不会对表数据有影响
            self.db.rollback()
        return 

    def insertdata_lijuan(self,results):
        sql = "insert into lijuan_kq(单位名称,部门,岗位名称,姓名,工号)values('%s','%s','%s','%s','%s')" % (results['单位名称'].strip(),results['部门'].strip(),results['岗位名称'].strip(),results['姓名'].strip(),results['工号'])
        sql1 = "ALTER TABLE lijuan_kq DROP id"
        sql2 = "ALTER TABLE lijuan_kq ADD id int NOT NULL FIRST"
        sql3 = "ALTER TABLE lijuan_kq MODIFY COLUMN id int NOT NULL AUTO_INCREMENT,ADD PRIMARY KEY(id)"
        try:
            self.cursor.execute(sql)
            self.cursor.execute(sql1)
            self.cursor.execute(sql2)
            self.cursor.execute(sql3)
            self.db.commit()
        except:
            # 如果发生错误就回滚,建议使用这样发生错误就不会对表数据有影响
            self.db.rollback()
        return


    #关闭
    def __del__(self):
        self.db.close()
