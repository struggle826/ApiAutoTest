'''
两种超时的场景：
1.接口耗时比较久，设置耗时时间，避免还没有执行完，超时退出了
2.接口性能，比如接口要求在500ms内执行完成
'''

import requests

for i in range(10):
    try:
        url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=15229807373"
        ret = requests.get(url,timeout=0.005)
        print(ret.status_code) # requests.exception.ConnectTimeout
    except Exception as e:
        print(e)

# 如果在规定时间内，返回200，超时返回time out
