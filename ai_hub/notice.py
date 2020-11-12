import requests

class notice:
    def __init__(self, openid):
        self.openid = openid

    def sendmsg(self, msg):
        if not isinstance(msg,str):
            msg = str(msg)
        if len(msg) >1024:
            msg = msg[:1024]

        url = "http://35.194.206.106/notice"
        data = {"openid":self.openid,"msg":msg}
        print(data)
        res = requests.post(url=url,params=data)
        print(res.text)
        
    def sendpic(self, pic):
        
        print("send pic.")
        
    def sendplot(self, plot):
        
        print("send plot.")

    def setopenid(self, openid):
        self.openid = openid
