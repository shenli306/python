from  selenium  import webdriver
from  selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import WebDriverWait # 智能等待
from  selenium.webdriver.support import expected_conditions as EC # 条件
import time
from Public.Logs import 日志记录类


class  web二次封装:   # 类名     里面的成员 有函数  def就是函数
    def  __init__(self,name): # 参数控制今天用什么浏览器来做测试
        self.log= 日志记录类()  # 实例化日志类
        t1= time.time()
        if name == 'chrome':
            self.driver = webdriver.Chrome()
            self.log.info(f'启动chrome浏览器,耗时:{time.time()-t1}秒')
        elif name == 'firefox':
            self.driver = webdriver.Firefox()
            self.log.info(f'启动firefox浏览器,耗时:{time.time()-t1}秒')
        elif name == 'edge':
            self.driver = webdriver.Edge()
            self.log.info(f'启动edge浏览器,耗时:{time.time()-t1}秒')
        else:
            self.driver = webdriver.Edge()
            self.log.info(f'启动edge浏览器,耗时:{time.time()-t1}秒')


    def  打开地址(self,地址):
        t1= time.time()
        self.driver.get(地址)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.log.info(f'打开地址{地址},耗时:{time.time()-t1}秒')
    
    def  智能等待(self,定位方式,定位值):
        t1= time.time()
        if 定位方式 == 'id':
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,定位值))) #一秒检测2次
        elif 定位方式 == 'name':
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.NAME,定位值)))
        elif 定位方式 == 'class':
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,定位值)))
        elif 定位方式 == 'xpath':
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,定位值)))
        elif 定位方式 == 'text':
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,定位值)))
        else:
            raise  Exception('定位方式错误')
        self.log.info(f'等待元素{定位方式},{定位值},耗时:{time.time()-t1}秒')


    def  查找元素(self,定位方式,定位值):
        self.智能等待(定位方式,定位值)
        if 定位方式 == 'id':
            return self.driver.find_element(By.ID,定位值)
        elif 定位方式 == 'name':
            return self.driver.find_element(By.NAME,定位值)
        elif 定位方式 == 'class':
            return self.driver.find_element(By.CLASS_NAME,定位值)
        elif 定位方式 == 'xpath':
            return self.driver.find_element(By.XPATH,定位值)
        elif 定位方式 == 'text':
            return self.driver.find_element(By.LINK_TEXT,定位值)
        else:
            raise  Exception('定位方式错误')
        
    def  点击元素(self,定位方式,定位值):
        t1= time.time()
        try:
            self.查找元素(定位方式,定位值).click()
            self.log.info(f'点击元素{定位方式},{定位值},耗时:{time.time()-t1}秒')
        except Exception as e:
            self.log.error(f'点击元素{定位方式},{定位值},错误消息{e}')


    def  输入内容(self,定位方式,定位值,内容):
        t1= time.time()
        try:
            self.查找元素(定位方式,定位值).send_keys(内容)
            self.log.info(f'输入内容{定位方式},{定位值},{内容},耗时:{time.time()-t1}秒')
        except Exception as e:
            self.log.error(f'输入内容{定位方式},{定位值},{内容},错误消息{e}')



    def 清除内容(self,定位方式,定位值):
        t1= time.time()
        try:
            self.查找元素(定位方式,定位值).clear()
            self.log.info(f'清除内容{定位方式},{定位值},耗时:{time.time()-t1}秒')
        except Exception as e:
            self.log.error(f'清除内容{定位方式},{定位值},错误消息{e}')
            

    def  关闭浏览器(self):
        t1= time.time()
        self.driver.quit()
        self.log.info(f'关闭浏览器,耗时:{time.time()-t1}秒')

    def  切换框架(self,定位方式,定位值):
        t1= time.time()
        try:
            self.driver.switch_to.frame(self.查找元素(定位方式,定位值))
            self.log.info(f'切换框架{定位方式},{定位值},耗时:{time.time()-t1}秒')
        except Exception as e:
            self.log.error(f'切换框架{定位方式},{定位值},错误消息{e}')

    def  切换默认框架(self):
        t1= time.time()
        self.driver.switch_to.default_content()
        self.log.info(f'切换默认框架,耗时:{time.time()-t1}秒')
    
    def 获取文本(self,定位方式,定位值):
        t1= time.time()
        try:
            result=self.查找元素(定位方式,定位值).text
            self.log.info(f'获取文本{定位方式},{定位值},耗时:{time.time()-t1}秒')
            return result
        except Exception as e:
            self.log.error(f'获取文本{定位方式},{定位值},错误消息{e}')
    

# if __name__ == '__main__':
#     浏览器=web二次封装('chrome') #实例化 创建对象      就好像盖房子要根据之前设计的图纸来
#     浏览器.打开地址('http://39.102.208.214/haidao') # 调用方法
#     浏览器.点击元素('text','登录')
#     浏览器.输入内容('name','username','lisi')
#     浏览器.输入内容('name','password','123456')
#     浏览器.点击元素('id','popup-submit')
#     浏览器.点击元素('text','我的订单')
#     浏览器.关闭浏览器()

