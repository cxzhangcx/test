# coding:utf-8
import unittest
import requests
from common.logger import Log
from requests.auth import HTTPBasicAuth
from case import test_login

class yuangong_query(unittest.TestCase):
    log = Log()
    def yuangong_query(self, employeeName, phone):
        '''三个参数：
        账号：username，密码：psw'''
        url = "http://10.99.2.47/pub/employees/list"
        headers = {"Accept":"application/json",
                  "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
                  "Accept-Language":"zh-CN,zh"

                 }

        json_data = {"deptCode":0,"employeeName":employeeName,"phone":phone,"page":1,"pageSize":15,"status":1}
        print(json_data)



        res = requests.get(url, headers=headers, json=json_data,auth=("17621255007",'123456'))
        result1 = res.content  # 字节输出
        self.log.info("员工查询结果：%s"%result1)
        return res.json()      # 返回json

    def setUp(self):
        pass
        # s = requests.session()
        # self.blog = Blog(s)

    def test_query(self):
        u'''测试aa'''
        self.log.info("------查询成功用例：start!---------")
        employeeName = ""
        self.log.info("输入员工姓名：%s"%employeeName)
        phone = ""
        self.log.info("输入电话号码：%s"%phone )
        result = self.yuangong_query(employeeName, phone)
        self.log.info("获取测试结果：%s"%result)
        self.assertEqual(result["status"], 2000)
        self.log.info("------pass!---------")



if __name__ == "__main__":
   unittest.main()
