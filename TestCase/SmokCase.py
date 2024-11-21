"""
冒烟测试用例
"""
from Public.Base import *
import time
class Test_haidaocase:#类名必须以Test_开头
    def setup_method(self):
        self.浏览器 = web二次封装('chrome')#打开浏览器



    def teardown_method(self):
        self.浏览器.关闭浏览器()#关闭浏览器

    def test_登录测试001(self):
        """验证登录成功"""
        self.浏览器.打开地址("http://39.102.208.214/haidao")
        self.浏览器.点击元素('text','登录')
        self.浏览器.输入内容('name','username','admin')
        self.浏览器.输入内容('name','password','111111')
        self.浏览器.点击元素('id','popup-submit')
        time.sleep(3)
        实际结果=self.浏览器.获取文本('xpath','/html/body/div[1]/div/ul[2]/li[1]/a')
        assert 实际结果=='admin'
   
    def test_登出测试001(self):
        self.浏览器.打开地址('http://39.102.208.214/haidao')
        self.浏览器.点击元素('text','登录')
        self.浏览器.输入内容('name','username','admin')
        self.浏览器.输入内容('name','password','1111110')
        self.浏览器.点击元素('id','popup-submit')
        实际结果=self.浏览器.获取文本('class','error')
        assert 实际结果=='用户不存在或密码错误'


    