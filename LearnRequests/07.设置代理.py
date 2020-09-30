'''
1.爬虫之类的场景，避免服务器认为是攻击，将IP屏蔽掉
2.代理抓包，定位问题
'''

import requests

proxy = {
    # http协议，使用"http://127.0.0.1:8888"代理，8888与fiddler的端口一致。
    "http":"http://127.0.0.1:8888",
    # https协议，使用"http://127.0.0.1:8888"代理，8888与fiddler的端口一致。
    "https":"http://127.0.0.1:8888"
}
r = requests.get("http://www.baidu.com/s?wd=123456",proxies=proxy)
print(r.text)
# requests.put()
# requests.delete()