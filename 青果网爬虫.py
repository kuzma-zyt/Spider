import re

import execjs
from bs4 import BeautifulSoup
import requests
from lxml import etree


class QGSpider:
    def __init__(self):
        self.login_url = "http://jwgl.lnc.edu.cn/_data/login_home.aspx"
        self.main_url = "http://jwgl.lnc.edu.cn/MAINFRM.aspx"
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "792",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "jwgl.lnc.edu.cn",
            "Origin":"http://jwgl.lnc.edu.cn",
            "Pragma": "no-cache",
            "Referer": "http://jwgl.lnc.edu.cn/_data/login_home.aspx",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
        }
        self.mainHeaders = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
        }
        self.cookies = {
            "myCookie":"",
            "ddrftguip087w2rjksdf":"43q34rv04tqqxt5akt1curbq"
        }


    def run(self):
        session = requests.session()
        headers = self.headers
        login_url = self.login_url
        main_url = self.main_url
        cookies = self.cookies
        mainHeaders = self.mainHeaders
        dsdsdsdsdxcxdfgfg = execjs.compile(open(r"qgLogin.js", encoding='utf-8').read()).call('chkpwd', "18601310417", "13421105659wsyt")
        # 模拟form表单的数据
        post_data = {
            "__VIEWSTATE": "/wEPDwUKLTMzNjY4NzgxOWRkSsgr+FjxqVtpp67Oxlrr12mSbPwdS/64bw4ODUzWKoE=",
            "__VIEWSTATEGENERATOR": "56911C19",
            "__EVENTVALIDATION": "/wEdAAK0g57d+yILrOivE914+2DpZ5IuKWa4Qm28BhxLxh2oFMpGASmFADAxvJB0hCDAec35e+aApr59SOtmnG/TJZZE",
            "pcInfo": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36undefined5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SN:NULL",
            "typeName": "学生",
            "dsdsdsdsdxcxdfgfg": dsdsdsdsdxcxdfgfg,
            "validcodestate": "0",
            "Sel_Type":"STU",
            "txt_asmcdefsddsd":"18601310417",
            "txt_psasas":"请输入密码"
        }
        response = session.post(login_url, headers=headers, data=post_data,cookies=cookies)
        str = response.content.decode('gbk')
        print(str)
        resultResp = session.get(main_url, headers=mainHeaders)
        result = resultResp.content.decode('gbk')
        print(result)


if __name__ == '__main__':
    qg = QGSpider()
    qg.run()