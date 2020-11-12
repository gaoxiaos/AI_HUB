import requests

class notice:
    def __init__(self, openid):
        self.openid = openid

    def sendmsg(self, msg):
        if not isinstance(msg,str):
            msg = str(msg)
        if len(msg) >200:
            msg = msg[:200]

        url = "http://35.194.206.106/notice"
        data = {"openid":self.openid,"msg":msg}
        print(data)
        res = requests.post(url=url,params=data)
        print(res.text)

    def setopenid(self, openid):
        self.openid = openid
