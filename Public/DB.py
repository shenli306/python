"""
测试需要用到数据库
这里是MySQL数据库
增insert、删delete、改update、查select
python操作MySQL数据库需要用到第三方库pymysql pip install pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple

"""
import pymysql
from Public.Logs import 日志记录类

class DB:#数据库操作类
    def __init__(self,host,user,password,port,db):
        self.log = 日志记录类()
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.db = db
    def 连接MySQL数据库(self):#连接数据库
        try:
            self.conn = pymysql.connect(host=self.host,user=self.user,password=self.password,port=self.port,db=self.db)
            self.cur = self.conn.cursor()
            self.log.info('数据库连接成功,主机'+self.host)
        except Exception as e:
            print('数据库连接失败',e)
            self.log.error('数据库连接失败,错误信息为'+str(e))

    def 执行查询语句(self,sql):
        self.cur.execute(sql)
        data= self.cur.fetchall()
        self.log.info('执行查询语句成功,查询语句为'+sql+',查询结果为'+str(data))
        return data
        
    # def 执行增删改语句(self,sql):
    #     self.cur.execute(sql)
    #     self.conn.commit()
    #     self.log.info('执行增删改语句成功,查询语句为'+sql)

    def 关闭数据库连接(self):
        self.cur.close()
        self.conn.close()
        self.log.info('数据库连接关闭')


if __name__ == '__main__':
    db = DB('39.102.208.214','root','',"3306",'zyd')
    db.连接MySQL数据库()
    sql = 'select * from user'
    data = db.执行查询语句(sql)
    print(data)
    db.关闭数据库连接()

    """
    select 需要的列名 from 表名 where 条件
    聚合运算：
    count() 计行数 sum() 求列的和 avg() 求列平均值 max() 求列最大值 min() 求列的最小值


    海盗表：
    hd_member 注册用户表
    hd_order 订单表
    hd_goods_sku 商品表

    """