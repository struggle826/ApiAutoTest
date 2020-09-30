'''
发送post请求
1.使用data传参
2.使用json传参
'''

import  requests
url = "http://www.httpbin.org/post"
canshu = {"username":"root","password":"123456"}
r = requests.post(url,data=canshu) #使用data传参"Content-Type": "application/x-www-form-urlencoded",
print(r.text)

r = requests.post(url,json=canshu) #使用json传参"Content-Type": "application/json",
print(r.text)
# post接口具体用data传参，还是用json传参，是后台实现决定的

# 金融项目，登录接口，post接口
url = "http://192.168.150.52:8089/futureloan/mvc/api/member/login"
canshu = {"mobilephone":"15229807373","pwd":"123456"}
r = requests.post(url,data=canshu)
print(r.text)

# 金融项目不支持json传参
# canshu = {"mobilephone":"15229807373","pwd":"123456"}
# r = requests.post(url,json=canshu)
# print(r.text)  #{"status":0,"code":"20103","data":null,"msg":"手机号不能为空"}
