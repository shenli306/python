import random,time,allure
from Public.Base import web二次封装
from Public.DB import DB


@allure.feature('海盗注册模块测试')
class Testhaodao():
    def setup_method(self):
        self.浏览器 = web二次封装('chrome')


    def teardown_method(self):
        self.浏览器.关闭浏览器()


    @allure.story('注册成功测试001')#需求单个功能点
    @allure.title('验证注册成功001')#用例标题
    @allure.description('用例的描述，确保这些数据之前不存在，用例执行前的数据')
    @allure.severity(allure.severity_level.CRITICAL)#用例优先级
    def test_001(self):
        with allure.step('打开地址'):
            self.浏览器.打开地址("http://39.102.208.214/haidao")
        with allure.step('点击注册'):
            self.浏览器.点击元素('text','注册')
        with allure.step('输入用户名和密码'):
            username='admin'+str(random.randint(1000,9999))+str(random.randint(100,999))
            self.浏览器.输入内容('name','username',username)
            self.浏览器.输入内容('name','password','111111')
            self.浏览器.输入内容('name','pwdconfirm','111111')
            self.浏览器.输入内容('name','email','admin'+str(random.randint(1,100))+'@qq.com')
            self.浏览器.输入内容('name','mobile','176'+str(random.randint(10000000,99999999)))
            self.浏览器.点击元素('name','dosubmit')
            time.sleep(2)
        with allure.step('断言'):
            实际结果=self.浏览器.获取文本('xpath','/html/body/div[1]/div/ul[2]/li[1]/a')
            期望结果=username
            assert 实际结果==期望结果
        #数据库里面有吗？
        # with allure.step('断言数据库存在'):
        #     mysql = DB("39.102.208.214", "root", "",3306, "zyd")
        #     mysql.连接MySQL数据库()
        #     sql = "select count(1) from hd_member where username = '"+username+"'"
        #     result = mysql.执行查询语句(sql)
        #     mysql.关闭数据库连接()
        #     assert result[0][0] == 1
            

    @allure.story('注册成功测试002')#需求单个功能点
    @allure.title('验证注册错误002')#用例标题
    @allure.severity(allure.severity_level.NORMAL)#用例优先级
    def test_002(self):
        with allure.step('打开地址'):
            self.浏览器.打开地址("http://39.102.208.214/haidao")
        with allure.step('点击注册'):
            self.浏览器.点击元素('text','注册')
        with allure.step('输入用户名和密码'):
            
            self.浏览器.输入内容('name','username','aa')
            self.浏览器.点击元素('name','password')
            time.sleep(3)
        with allure.step('断言'):
            实际结果=self.浏览器.获取文本('class','validform_checktip')
            期望结果='用户名长度在3-15个字符'
            assert 实际结果==期望结果


    # def test_登录测试003(self):
    #     with allure.step('步骤一：打开浏览器'):
    #         self.浏览器.打开地址('http://39.102.208.214//haidao/')
    #     with allure.step('步骤二：点击注册按钮'):
    #         self.浏览器.点击元素('text','注册')
    #     with allure.step('步骤三：输入错误的密码注册信息'):
    #         self.浏览器.输入内容('name','username','aa1')
    #         self.浏览器.输入内容('name','password','12345')
    #         self.浏览器.点击元素('name','pwdconfirm')
    #         time.sleep(2)
    #     with allure.step('步骤四：断言注册成功'):
    #         实际结果 = self.浏览器.获取文本('xpath','/html/body/div[3]/div[2]/div/form/div[2]/div/span')
    #         期望结果 = '密码至少为 6 位字符'
    #         assert 实际结果 == 期望结果
    # @allure.story('注册测试004')
    # @allure.title("验证错误的重复密码注册信息")
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_登录测试004(self):
    #     with allure.step('步骤一：打开浏览器'):
    #         self.浏览器.打开地址('http://39.102.208.214/haidao/')
    #     with allure.step('步骤二：点击注册按钮'):
    #         self.浏览器.点击元素('text','注册')
    #     with allure.step('步骤三：输入错误的密码注册信息'):
    #         self.浏览器.输入内容('name','username','aa1')
    #         self.浏览器.输入内容('name','password','123456')
    #         self.浏览器.输入内容('name','pwdconfirm','1')
    #         self.浏览器.点击元素('name','email')
    #         time.sleep(2)
    #     with allure.step('步骤四：断言注册成功'):
    #         实际结果 = self.浏览器.获取文本('xpath','/html/body/div[3]/div[2]/div/form/div[3]/div/span')
    #         time.sleep(7)
    #         期望结果 = '两次输入的内容不一致！'
    #         assert 实际结果 == 期望结果
    # @allure.story('注册测试005')
    # @allure.title("验证错误的注册邮箱信息")
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_登录测试005(self):
    #     with allure.step('步骤一：打开浏览器'):
    #         self.浏览器.打开地址('http://39.102.208.214/haidao')
    #     with allure.step('步骤二：点击注册按钮'):
    #         self.浏览器.点击元素('text','注册')
    #     with allure.step('步骤三：输入错误的邮箱注册信息'):
    #         self.浏览器.输入内容('name','username','aa1')
    #         self.浏览器.输入内容('name','password','123456')
    #         self.浏览器.输入内容('name','pwdconfirm','123456')
    #         self.浏览器.输入内容('name','email','1')
    #         self.浏览器.点击元素('name','mobile')
    #         time.sleep(2)
    #     with allure.step('步骤四：断言注册成功'):
    #         实际结果 = self.浏览器.获取文本('xpath','/html/body/div[3]/div[2]/div/form/div[4]/div/span')
    #         time.sleep(7)
    #         期望结果 = '邮箱地址格式不对！'
    #         assert 实际结果 == 期望结果
    # @allure.story('注册测试006')
    # @allure.title("验证错误的密码注册信息")
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_登录测试006(self):
    #     with allure.step('步骤一：打开浏览器'):
    #         self.浏览器.打开地址('http://39.102.208.214/haidao')
    #     with allure.step('步骤二：点击注册按钮'):
    #         self.浏览器.点击元素('text','注册')
    #     with allure.step('步骤三：输入错误的用户名注册信息'):
    #         self.浏览器.输入内容('name','username','aa1')
    #         self.浏览器.输入内容('name','password','123456')
    #         self.浏览器.输入内容('name','pwdconfirm','123456')
    #         self.浏览器.输入内容('name','email','30389665@qq.com')
    #         self.浏览器.输入内容('name','mobile','123')
    #         self.浏览器.点击元素('name','dosubmit')
    #         time.sleep(2)
    #     with allure.step('步骤四：断言注册成功'):
    #         实际结果 = self.浏览器.获取文本('xpath','/html/body/div[3]/div[2]/div/form/div[5]/div/span')
    #         time.sleep(7)
    #         期望结果 = '请填写正确的手机号码！'
    #         assert 实际结果 == 期望结果
    # @allure.story('注册测试007')
    # @allure.title("验证错误的密码注册信息")
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_登录测试007(self):
    #     with allure.step('步骤一：打开浏览器'):
    #         self.浏览器.打开地址('http://39.102.208.214/haidao')
    #     with allure.step('步骤二：点击注册按钮'):
    #         self.浏览器.点击元素('text','注册')
    #     with allure.step('步骤三：输入正确的注册信息'):
    #         username = 'laowang'+str(random.randint(1000, 9999))+str(random.randint(100, 999))
    #         self.浏览器.输入内容('name','username',username)
    #         self.浏览器.输入内容('name','password','123456')
    #         self.浏览器.输入内容('name','pwdconfirm','123456')
    #         self.浏览器.输入内容('name','email','123'+str(random.randint(1000,9999))+'@qq.com')
    #         self.浏览器.输入内容('name','mobile','176'+str(random.randint(10000000,99999999)))
    #         self.浏览器.点击元素('name','dosubmit')
    #         time.sleep(2)
    #     with allure.step('步骤四：断言注册成功'):
    #         实际结果 = self.浏览器.获取文本('xpath','/html/body/div[1]/div/ul[2]/li[1]/a')
    #         time.sleep(7)
    #         期望结果 = username
    #         assert 实际结果 == 期望结果
