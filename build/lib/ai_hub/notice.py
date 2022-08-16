from datetime import datetime
import ai_hub.globalvar as gl
from ai_hub import utils, setopenid, getopenid


class notice:
    def __init__(self, openid=None):
        gl._init()
        if openid:
            self.openid = openid
            setopenid(openid)
        else:
            self.openid = getopenid()
        if self.openid ==None:
            raise Exception('openid is None,ex: notice(openid="oM8pVuBWl8Rw_vFz7rZNgeO4T8H8"')

    def setopenid(self, openid):
        utils.setopenid(openid)

    def task_complete_notice(self, task_name, task_progree=None, remark=None, title_mesh=None):
        time = datetime.now().strftime('%Y-%m-%d-%H-%M')
        try:
            msg = {"msgid":"task_complete_notice", "openid":self.openid, "title_mesh":str(title_mesh), "task_name":str(task_name), "task_progree":str(task_progree), "time":time,"remark":str(remark)}
            utils.sendmsg(msg)
        except:
            print("task_complete_notice faild! ")



    def sendpic(self, pic):
        print("send pic will be able in next version..")
        pass
        
    def sendplot(self, plot):
        
        print("send plot will be able in next version...")

