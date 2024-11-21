from Public.Base import web二次封装
import  time,random

浏览器=web二次封装('chrome') #实例化 创建对象      就好像盖房子要根据之前设计的图纸来
浏览器.打开地址('https://demo.zdoo.com/sys/user-login.html')
浏览器.点击元素('xpath','/html/body/div/div/div/div[2]/div/form/button')
浏览器.点击元素('id','s-menu-dashboard')
浏览器.切换框架('xpath','/html/body/div[1]/div[5]/div/div[3]/iframe')

浏览器.点击元素('text','项目')
浏览器.点击元素('text','创建项目')

# 浏览器.切换默认框架()

# 浏览器.切换框架('xpath','/html/body/div[1]/div[5]/div[2]/div[3]/iframe')


浏览器.输入内容('id','name','shenli'+str(random.randint(1,999999999)))
time.sleep(3)

浏览器.点击元素('id','begin')
浏览器.点击元素('xpath','/html/body/div[6]/div[3]/table/tbody/tr[3]/td[2]')

浏览器.点击元素('id','end')
浏览器.点击元素('xpath','/html/body/div[7]/div[3]/table/tbody/tr[3]/td[2]')

# 浏览器.切换默认框架 ()
浏览器.切换框架('xpath','/html/body/div[4]/div/div/div[2]/form/table/tbody/tr[8]/td/div/div[2]/iframe')

浏览器.输入内容('xpath','/html','1'+str(random.randint(1,999999999)))

浏览器.切换默认框架()
浏览器.切换框架('xpath','/html/body/div[1]/div[5]/div/div[3]/iframe')

浏览器.点击元素('id','submit')

浏览器.切换默认框架()
time.sleep(5)