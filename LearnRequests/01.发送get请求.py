'''
发送get请求：
1.get不带参数
2.get带参数
'''

import  requests #导入包
url = "http://www.baidu.com"
r = requests.get(url) #发送get请求，使用变量r接受响应
print(r.text) #文本类型的
print(r.status_code) #状态码 200
print(r.reason) #状态原因 OK
print("r.cookies=",r.cookies) #响应信息的cookies
print(r.headers) #响应的头部信息
print(r.raw) #原始格式的  <urllib3.response.HTTPResponse object at 0x00000000034682E8> 是对象
print(r.raw.read())
# print(r.)
# print(r.raw.read(10))

# 金融项目注册
# 方法1：参数拼接在URL后面，?号后面是参数，参数之间用&拼接。 参数=值
url = "http://192.168.150.52:8089/futureloan/mvc/api/member/register?mobilephone=15229807373&pwd=123456&rename=auto"
r = requests.get(url)
print(r.text) #{"status":0,"code":"20110","data":null,"msg":"手机号码已被注册"}
print(r.json()) #{'status': 0, 'code': '20110', 'data': None, 'msg': '手机号码已被注册'}
print(type(r.json())) #<class 'dict'>

# 方法2：使用params传参
url = "http://192.168.150.52:8089/futureloan/mvc/api/member/register"
canshu = {"mobilephone":"15229807373","pwd":"123456","rename":"auto"}
r = requests.get(url,params=canshu)
print(r.json())
print(" =================================================================")

# httpbin，一个测试网站，有get、post等接口，参数任意构造，服务器将发送的请求转成json格式的返回
r = requests.get("http://httpbin.org/get?username=123&pwd=456&email=12345@qq.com")
print(r.text)

print(" ============================返回手机号码归属地===================================")
# 方法1：
url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=15229807373"
r = requests.get(url)
print(r.text)

# 方法2：
url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?"
canshu = {"tel":"15229807373"}
r = requests.get(url,params=canshu)
print(r.text)

print(" =================================================================")
# 发送的请求带请求头
# 设置User-Agent，伪装成浏览器发送请求
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}
r = requests.get("http://httpbin.org/get?username=123&pwd=456&email=12345@qq.com",headers=headers)
print(r.text)

# 既带参数，又带请求头
# requests.get(url,params=None,**kwargs)
