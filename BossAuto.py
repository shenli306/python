#Boss自动化海投简历

from Public.Base import web二次封装
import time

if __name__ == '__main__':
    #初始化
    浏览器= web二次封装('chrome')
    浏览器.打开地址('https://www.zhipin.com/?ka=header-home-logo') #打开boss直聘
    浏览器.点击元素('text','登录/注册')#点击登录/注册
    time.sleep(10)#等待10秒扫码登录
    浏览器.点击元素('text','校园')#点击校园
    # 浏览器.点击元素('xpath','/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/span')#点击职业类型下拉框
    # 浏览器.点击元素('xpath','/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div[3]/ul/li[1]/span')
    浏览器.输入内容('xpath','/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div[2]/input' ,'python')#输入职业类型
    浏览器.点击元素('xpath','/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[1]/a')#点击搜索
    

    time.sleep(5)
    #关闭浏览器
    浏览器.关闭浏览器()