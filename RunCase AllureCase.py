#pip install pytest
#pip install pytest-html
#-s 生成测试报告，有中文会乱码
#-v 显示详细的测试结果
#产生html格式的测试报告
#TestCase/SmokCase.py测试用例
#--self-contained-html 生成独立html文件

import pytest,time,os
from Public.SendMail import send_mail
from Public.Comm import *

if __name__ == '__main__':
    t1=time.strftime("%Y_%m_%d_%H_%M_%S")
    pytest.main(['-s','-v','TestCase/AllureCase.py',
                 '--alluredir=./Report/result',
                 '--clean-alluredir'
                 ])
    #  指明allure报告位置    --clean-alluredir  清空原有的历史数据
    #  调用allure生成报告
    allure_cmd=os.getcwd()+'//Tools//allure-2.27.0//bin//allure generate  ./Report/result -o .//Report//report_allure   --clean'
   
    os.system(allure_cmd) #  执行命令

    # 代码打压缩包 与Comm联系起来
    #zip_dir('./Report/report_allure','./Report/report_allure.zip')
    

    #代码发送邮件
   # send_mail('./Report/report_allure.zip','3068254068@qq.com')