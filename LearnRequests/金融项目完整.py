'''
金融项目
'''

import requests
# 投资人注册
url0 = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone":"17386960032","pwd":"123456","rename":" investor"}
r = requests.get(url0,params=canshu)
print(r.text)

# 借款人注册
url1 = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone":"17386960034","pwd":"123456","rename":"borrower"}
r = requests.get(url1,params=canshu)
print(r.text)

# 获取用户列表
url2 = "http://192.168.150.222:8081/futureloan/mvc/api/member/list"
r = requests.get(url2)
print(r.text)

# 投资人登录
url3 = "http://192.168.150.52:8089/futureloan/mvc/api/member/login"
canshu = {"mobilephone":"17386960032","pwd":"123456"}
r = requests.post(url3,data=canshu)
print(r.text)

# 投资人充值
url4 = "http://192.168.150.52:8089/futureloan/mvc/api/member/recharge"
canshu = {"mobilephone":"17386960032","amount":"45"}
r = requests.post(url4,data=canshu)
print(r.text)

# 借款人登录
url5 = "http://192.168.150.52:8089/futureloan/mvc/api/member/login"
canshu = {"mobilephone":"17386960034","pwd":"123456"}
r = requests.post(url5,data=canshu)
print(r.text)

# 借款人提交借款申请材料，平台加贷款项目
url6 = "http://192.168.150.52:8089/futureloan/mvc/api/member/add"
canshu = {
    "memberId":" ",
    "title":" ",
    "amount":"1000",
    "loanRate":"24",
    "loanTerm":"30",
    "loanDateType":"0",
    "repaymemtWay":"5",
    "biddingDays":"7"
}
r = requests.post(url6,data=canshu)
print(r.text)

# 获取标列表
url7 = "http://192.168.150.52:8089/futureloan/mvc/api/loan/getLoanList"
r = requests.post(url7)
print(r.text)

# 平台人员审核1-运营人员审核（初审）
url8 = "http://192.168.150.52:8089/futureloan/mvc/api/loan/audit"
canshu = {"id":" ","status":"2"}
r = requests.post(url8,data=canshu)
print(r.text)

# 平台人员审核2-运营主管审核（复审）
url9 = "http://192.168.150.52:8089/futureloan/mvc/api/loan/audit"
canshu = {"id":" ","status":"3"}
r = requests.post(url9,data=canshu)
print(r.text)

# 平台人员审核3-运营总监审核（投标中状态）
url10 = "http://192.168.150.52:8089/futureloan/mvc/api/loan/audit"
canshu = {"id":" ","status":"4"}
r = requests.post(url10,data=canshu)
print(r.text)

# 投资人投标（满标）
url11 = "http://192.168.150.52:8089/futureloan/mvc/api/member/bidLoan"
canshu = {
    "memberId":" ",
    "password":"123456",
    "loanId":" ",
    "amount":"1000"
}
r = requests.post(url11,data=canshu)
print(r.text)

# 投资人投标（流标）
url12 = "http://192.168.150.52:8089/futureloan/mvc/api/member/bidLoan"
canshu = {
    "memberId":" ",
    "password":"123456",
    "loanId":" ",
    "amount":"100"
}
r = requests.post(url12,data=canshu)
print(r.text)

# 投资人获取投资记录
url13 = "http://192.168.150.52:8089/futureloan/mvc/api/invest/getInvestsByMemberId"
canshu = {"memberId":" "}
r = requests.post(url13,data=canshu)
print(r.text)

# 获取标的所有投资记录
url14 = "http://192.168.150.52:8089/futureloan/mvc/api/invest/getInvestsByLoanId"
canshu = {"loanId":" "}
r = requests.post(url14,data=canshu)
print(r.text)

# 生成借款人回款计划
url15 = "http://192.168.150.52:8089/futureloan/mvc/api/loan/generateRepayments"
canshu = {"id":" "}
r = requests.post(url15,data=canshu)
print(r.text)


