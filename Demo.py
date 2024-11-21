#登录之后---客户管理--客户--添加客户--填完 --保存
#UEL:https://demo.zdoo.com/sys/user-login.html
#账号密码都是demo不用填直接登录


from Public.Base import web二次封装
import  time,random

#运行10次循环
for i in range(10):

    浏览器=web二次封装('Edge') #实例化 创建对象      就好像盖房子要根据之前设计的图纸来
    浏览器.打开地址('https://demo.zdoo.com/sys/user-login.html')
    浏览器.点击元素('xpath','/html/body/div/div/div/div[2]/div/form/button')
    浏览器.点击元素('xpath','/html/body/div[1]/div[3]/div[1]/ul[1]/li[2]/button/span')
    浏览器.切换框架('xpath','/html/body/div[1]/div[5]/div[2]/div[3]/iframe')
    浏览器.点击元素('text','客户')
    浏览器.点击元素('text','添加客户')
    浏览器.切换默认框架()

    浏览器.切换框架('xpath','/html/body/div[1]/div[5]/div[2]/div[3]/iframe')
    浏览器.输入内容('id','name','李四'+str(random.randint(10000000,99999999)))  # 填写客户名称

    浏览器.点击元素('xpath','/html/body/div[2]/div[1]/div[2]/form/fieldset[1]/table/tbody/tr[3]/td[1]/div[2]/a/span')  # 填写来源类型
    浏览器.点击元素('xpath','/html/body/div[2]/div[1]/div[2]/form/fieldset[1]/table/tbody/tr[3]/td[1]/div[2]/div/ul/li[1]')  # 填写来源类型
    浏览器.输入内容('id','sourceNote','2233')  # 填写来源备注

    浏览器.点击元素('xpath','/html/body/div[2]/div[1]/div[2]/form/fieldset[1]/table/tbody/tr[4]/td[1]/div/a/span')  # 填写来源渠道
    浏览器.点击元素('xpath','/html/body/div[2]/div[1]/div[2]/form/fieldset[1]/table/tbody/tr[4]/td[1]/div/div/ul/li[2]')  # 填写来源渠道

    浏览器.点击元素('xpath','/html/body/div[2]/div[1]/div[2]/form/fieldset[1]/table/tbody/tr[4]/td[2]/div/a/span')  # 填写客户成功经理
    浏览器.点击元素('xpath','/html/body/div[2]/div[1]/div[2]/form/fieldset[1]/table/tbody/tr[4]/td[2]/div/div/ul/li[1]')  # 填写客户成功经理demo
    浏览器.输入内容('id','contact','张三')  # 填写联系人
    浏览器.输入内容('id','title','经理')  # 填写职位
    浏览器.输入内容('id','email','zh'+str(random.randint(10000000,99999999))+'@qq.com')  # 填写邮箱
    浏览器.输入内容('id','mobile','138'+str(random.randint(10000000,99999999)))  # 填写手机
    浏览器.输入内容('id','weixin','z30'+str(random.randint(10000000,99999999)))  # 填写微信
    浏览器.输入内容('id','phone','1'+str(random.randint(10000000,99999999)))  # 填写地址名称
    浏览器.输入内容('id','qq','3'+str(random.randint(10000000,99999999)))  # 填写地址位置


    浏览器.点击元素('xpath','/html/body/div[2]/div[1]/div[2]/form/fieldset[3]/table/tbody/tr[1]/td[1]/div/a/span')  # 填写客户行业
    浏览器.点击元素('xpath','/html/body/div[2]/div[1]/div[2]/form/fieldset[3]/table/tbody/tr[1]/td[1]/div/div/ul/li[3]')  # 填写客户行业


    浏览器.点击元素('xpath','/html/body/div[2]/div[1]/div[2]/form/fieldset[3]/table/tbody/tr[1]/td[2]/div/a/span')  # 填写客户状态
    浏览器.点击元素('xpath','/html/body/div[2]/div[1]/div[2]/form/fieldset[3]/table/tbody/tr[1]/td[2]/div/div/ul/li[1]')  # 填写客户状态

    浏览器.点击元素('xpath','/html/body/div[2]/div[1]/div[2]/form/fieldset[3]/table/tbody/tr[2]/td[1]/div/a/span')  # 填写类型
    浏览器.点击元素('xpath','/html/body/div[2]/div[1]/div[2]/form/fieldset[3]/table/tbody/tr[2]/td[1]/div/div/ul/li[1]')  # 填写类型


    浏览器.点击元素('xpath','/html/body/div[2]/div[1]/div[2]/form/fieldset[3]/table/tbody/tr[2]/td[2]/div/a/span')  # 填写行业
    浏览器.点击元素('xpath','/html/body/div[2]/div[1]/div[2]/form/fieldset[3]/table/tbody/tr[2]/td[2]/div/div/ul/li[7]')  # 填写行业


    浏览器.点击元素('xpath','/html/body/div[2]/div[1]/div[2]/form/fieldset[3]/table/tbody/tr[3]/td[1]/div/a/span')  # 填写规模
    浏览器.点击元素('xpath','/html/body/div[2]/div[1]/div[2]/form/fieldset[3]/table/tbody/tr[3]/td[1]/div/div/ul/li[1]')  # 填写规模


    浏览器.点击元素('xpath','/html/body/div[2]/div[1]/div[2]/form/fieldset[3]/table/tbody/tr[3]/td[2]/div/a/span')  # 填写区域
    浏览器.点击元素('xpath','/html/body/div[2]/div[1]/div[2]/form/fieldset[3]/table/tbody/tr[3]/td[2]/div/div/ul/li[2]')  # 填写区域







    浏览器.输入内容('id','addresstitle','北京市海淀区')  # 填写地址
    浏览器.输入内容('id','addresslocation','海淀区')  # 填写地址

    浏览器.点击元素('xpath','/html/body/div[2]/div[1]/div[2]/form/fieldset[3]/table/tbody/tr[6]/td[1]/div/div/a/span')  # 填写地址
    浏览器.点击元素('xpath','/html/body/div[2]/div[1]/div[2]/form/fieldset[3]/table/tbody/tr[6]/td[1]/div/div/div/ul/li[2]')  # 填写地址

    浏览器.输入内容('id','intension','买！！！！！！！！！！')  # 购买意向


    浏览器.点击元素('id','submit')
    time.sleep(1)



