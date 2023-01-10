import os
from time import sleep

import pytest

from fwv.basic import handleNumber


class TestCommon:

    @pytest.mark.smoke
    def test_add(self):
        a = 10
        b = 20
        c = 30
        assert c == handleNumber.add(a, b)

    @pytest.mark.high
    def test_muli(self):
        a = 10
        b = 20
        c = 200
        sleep(0.5)
        assert c == handleNumber.muli(a, b)


    def test_chufa(self):
        a = 10
        b = 20
        c = 20
        sleep(2)
        assert c == handleNumber.chufa(a, b)

    def test_chufa_with_zero(self):
        a = 10
        b = 0
        with pytest.raises(ZeroDivisionError) as e:
            handleNumber.chufa(a, b)
        exec_msg = e.value.args[0]
        assert e.type == ZeroDivisionError
        # print("___", exec_msg)
        assert exec_msg == 'division by zero'

    def test_minus(self):
        a = 10
        b = 20
        c = 10
        sleep(1)
        assert c == handleNumber.minus(a, b)

if __name__ == '__main__':
    pytest.main(['-s', '-q', 'test_common.py', '--alluredir', '../appreport'])
    os.system('allure generate  appreport/ -o  appreport/html --clean')
    #测试报告中的history复制到测试报告数据文件，不进行该操作首页获取不到趋势图
    os.system(r"xcopy C:\Users\thundersoft\PycharmProjects\pythonProject\appreport\html\history  C:\Users\thundersoft\PycharmProjects\pythonProject\appreport\report-history \E \Y \I")

#
#
# #测试报告生成目录
# #测试目录查找最新报告 编辑成邮件发送