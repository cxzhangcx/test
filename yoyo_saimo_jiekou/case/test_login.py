# coding:utf-8
import unittest
import requests
from common.logger import Log

class saimo_login(unittest.TestCase):
    log = Log()
    def login(self, username, psw):
        '''三个参数：
        账号：username，密码：psw'''
        url = "http://10.99.2.47/pub/login/ajaxLogin"
        headers = {"Accept":"application/json",
                  "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
                  "Accept-Language":"zh-CN,zh"

                 }

        json_data = {"loginNo": str(username), "password": str(psw),"captcha":"","loginedId":""}
        print(json_data)

        res = requests.post(url, headers=headers, json=json_data)
        result1 = res.content  # 字节输出
        self.log.info("赛摩登录结果：%s"%result1)
        return res.json()      # 返回json

    def setUp(self):
        pass
        # s = requests.session()
        # self.blog = Blog(s)

    def test_login1(self):
        u'''测试登录：正确账号，正确密码'''
        self.log.info("------登录成功用例：start!---------")
        username = "17621255007"
        self.log.info("输入正确账号：%s"%username)
        psw = "123456"
        self.log.info("输入正确密码：%s"%psw )
        result = self.login(username, psw)
        self.log.info("获取测试结果：%s"%result)
        self.assertEqual(result["status"], 2000)
        self.log.info("------pass!---------")

    def test_login2(self):
        u'''测试登录：正确账号，错误密码'''
        self.log.info("------登录失败用例：start!---------")
        username ="17621255007"
        self.log.info("输入正确账号：%s"%username)
        psw = "1234"
        self.log.info("输入错误密码：%s"%psw)
        result = self.login(username,psw)
        self.log.info("获取测试结果：%s"%result)
        self.assertEqual(result["status"], 4010)
        self.log.info("------pass!---------")

if __name__ == "__main__":
   unittest.main()
