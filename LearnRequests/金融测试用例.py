'''
注册
'''
import requests
# 验证用户不输入手机号时，注册失败
proxy = {
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
}
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register?mobilephone= &pwd=123456&rename=lemo"
r = requests.get(url,proxies=proxy)
print(r.text)
# 验证用户不输入密码时，注册失败
proxy = {
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
}
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register?mobilephone=15229807878&pwd= &rename=lemo"
r = requests.get(url,proxies=proxy)
print(r.text)
# 验证用户不输入手机号和密码时，注册失败
proxy = {
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
}
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register?mobilephone= &pwd= &rename=lemo"
r = requests.get(url,proxies=proxy)
print(r.text)
# 验证用户输入输入5位密码，注册失败
proxy = {
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
}
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register?mobilephone=15229807878&pwd=12345&rename=lemo"
r = requests.get(url,proxies=proxy)
print(r.text)
# 验证用户输入19位密码，注册失败
proxy = {
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
}
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register?mobilephone=15229807878&pwd=1234567891234567890&rename=lemo"
r = requests.get(url,proxies=proxy)
print(r.text)
# 验证用户输入10位手机号，注册失败
proxy = {
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
}
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register?mobilephone=1522980787&pwd=123456&rename=lemo"
r = requests.get(url,proxies=proxy)
print(r.text)
#验证用户输入12位手机号，注册失败
proxy = {
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
}
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register?mobilephone=152298078789&pwd=123456&rename=lemo"
r = requests.get(url,proxies=proxy)
print(r.text)
# 验证用户输入包含特殊字符的手机号，注册失败
proxy = {
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
}
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register?mobilephone=1522980787*&pwd=123456&rename=lemo"
r = requests.get(url,proxies=proxy)
print(r.text)
# 验证用户输入不合法手机号，注册失败
proxy = {
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
}
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register?mobilephone=12345612345&pwd=123456&rename=lemo"
r = requests.get(url,proxies=proxy)
print(r.text)
# 验证用户输入正确手机号和密码，注册失败
proxy = {
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
}
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register?mobilephone=15229807373&pwd=123456&rename=lemo"
r = requests.get(url,proxies=proxy)
print(r.text)
# 验证用户输入正确的手机号，6位密码，注册成功
proxy = {
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
}
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register?mobilephone=15229807878&pwd=123456&rename=lemo"
r = requests.get(url,proxies=proxy)
print(r.text)
# 验证用户输入正确的手机号，18位密码，注册成功
proxy = {
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
}
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register?mobilephone=15229807878&pwd=123456789123456789&rename=lemo"
r = requests.get(url,proxies=proxy)
print(r.text)
# 验证用户输入正确的手机号和密码，输入昵称，注册成功
proxy = {
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
}
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register?mobilephone=15229807878&pwd=123456&rename=lemo"
r = requests.get(url,proxies=proxy)
print(r.text)
# 验证用户输入正确的手机号和密码，不输入昵称，注册成功
proxy = {
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
}
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register?mobilephone=15229807878&pwd=123456"
r = requests.get(url,proxies=proxy)
print(r.text)
# 验证用户输入正确的手机号和密码，输入超长昵称，注册失败
proxy = {
    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
}
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register?mobilephone=15229807878&pwd=123456&rename=lemozxcvbnmasdfghjkl"
r = requests.get(url,proxies=proxy)
print(r.text)




