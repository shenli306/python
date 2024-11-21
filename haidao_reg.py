"""selenium主要是用于模拟用户对浏览器操作行为，进行自动化测试"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time,random

br=webdriver.Chrome()
br.get("http://39.102.208.214/haidao")
br.maximize_window()
br.implicitly_wait(10)
t1=time.time()
#点击注册
username='laowang'+str(random.randint(1000,9999))+str(random.randint(100,999))
br.find_element(By.LINK_TEXT,"注册").click() #点击
br.find_element(By.NAME,"username").send_keys(username)# 输入
br.find_element(By.NAME,"password").send_keys("123456")
br.find_element(By.NAME,"pwdconfirm").send_keys("123456")
br.find_element(By.NAME,"email").send_keys(str(random.randint(1000,9999))+"123456@qq.com")
br.find_element(By.NAME,"mobile").send_keys("176"+str(random.randint(10000000,99999999)))
br.find_element(By.NAME,"dosubmit").click()
#
br.find_element(By.LINK_TEXT,"返回商城首页").click() #点击
br.find_element(By.XPATH,'/html/body/div[5]/div[1]/div/ul/li/div[1]/a/img').click()
br.find_element(By.ID,'adjust-add').click() #点击
br.find_element(By.LINK_TEXT,"立即购买").click() #点击
br.find_element(By.LINK_TEXT,"添加新地址").click() #点击
# 添加地址
br.switch_to.frame(br.find_element(By.XPATH,'/html/body/div[7]/div/table/tbody/tr[2]/td/div/iframe'))# 进入框架
br.find_element(By.XPATH,"/html/body/form/div[1]/ul/li[1]/div/div/div[2]/div[1]").click()
br.find_element(By.LINK_TEXT,"广西").click() #点击
br.find_element(By.LINK_TEXT,"南宁").click() #点击
br.find_element(By.LINK_TEXT,"西乡塘").click() #点击
br.find_element(By.LINK_TEXT,"西乡塘街道").click() #点击
br.find_element(By.NAME,"address").send_keys("融华大厦313")
br.find_element(By.NAME,"name").send_keys("张三")
br.find_element(By.NAME,"mobile").send_keys("176"+str(random.randint(10000000,99999999)))
br.find_element(By.NAME,"zipcode").send_keys('123456') #点击
br.find_element(By.ID,"hold").click() #点击
br.switch_to.default_content() #退出框架
time.sleep(2)
br.find_element(By.LINK_TEXT,"货到付款").click() #点击
br.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[1]/div/div[1]/div/input").send_keys("速速发货")
br.find_element(By.LINK_TEXT,"提交订单").click() #点击
orderid=br.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[1]/p[1]/span").text #点击
print(orderid)
print('耗时：',time.time()-t1)
br.quit()


