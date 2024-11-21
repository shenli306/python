#pip install pytest
#pip install pytest-html
#-s 生成测试报告，有中文会乱码
#-v 显示详细的测试结果
#产生html格式的测试报告
#TestCase/SmokCase.py测试用例
#--self-contained-html 生成独立html文件

import pytest,time
from Public.SendMail import send_mail

if __name__ == '__main__':
    pytest.main(['-s','-v', 'TestCase/SmokCase.py',
                 '--html=./Report/report_'+time.strftime('%Y_%m_%d_%H_%M_%S')+'.html','--self-contained-html'])
    


    send_mail('./Report/report_'+time.strftime('%Y_%m_%d_%H_%M_%S')+'.html','3068254068@qq.com')


    