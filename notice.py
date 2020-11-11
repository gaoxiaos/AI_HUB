import requests

class AI_HUB:
    def __init__(self, openid):
        self.openid = openid

    def sendmsg(self, msg):
        url = "http://35.194.206.106/notice"
        data = {"openid":self.openid,"msg":msg}
        print(data)
        res = requests.post(url=url,params=data)
        print(res.text)
