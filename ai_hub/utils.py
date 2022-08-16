
import requests
import os
import ai_hub.globalvar as gl


def setopenid(openid):
    if openid is not None:
        gl.set_value("AIHUBID", openid)

def getopenid():
    openid = os.getenv("AIHUBID", None)
    if openid is None:
        openid = gl.get_value("AIHUBID", None)
    else:
        gl.set_value("AIHUBID", openid)
    return openid

def gethost():
    host = os.getenv("TCC", None)
    if not host:
        host = "http://aiutils.top:9000/notice"
    return host

def sendmsg(msg):
    if not isinstance(msg,str):
        msg = str(msg)
    if len(msg) >1024:
        msg = msg[:1024]

    url = gethost()
    data = {"msg":msg}
    try:
        res = requests.post(url=url,data=data)#,params=data,json=data
        print(res.text)
    except:
        print("ai-hub sendmsg error!")

def notice_newlogger(openid, tag):
    print("notice_newlogger: "+tag)
    hostname = os.getenv("HOSTNAME", "")
    msg = {"msgid":"notice_newlogger", "openid":openid, "tag":str(tag), "host":hostname}
    sendmsg(msg)

def notice_showlogger(openid, tag):
    print("notice_showlogger: "+tag)
    hostname = os.getenv("HOSTNAME", "")
    msg = {"msgid":"notice_showlogger", "tag":str(tag), "openid":openid, "host":hostname}
    sendmsg(msg)

def get_taskid():
    taskid = os.getenv("HOSTNAME", None)
    return taskid

def get_env():
    env = "local"
    if getopenid() and os.getenv("TCC",None):
        env = "TCC"
    elif getopenid():#不区分本地和远端，本地也可以发一遍消息 os.getenv("AIHUBLOGGER",None) and
        env = "AIHUB"
    else:
        env = "local"
    return env
