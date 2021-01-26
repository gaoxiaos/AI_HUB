import sys
import os



#log.i info级别 普通打印
def i(*args):
    print(*args)

#log.w warning级别 蓝色加强
def w(text):
    #FF00
    print('<span style="color:#080"><b>%s</b></span>' % text)

#log.e error级别 红色加强提示
def e(text):
    print('<span style="color:#0A0"><b>%s</b></span>' %text)

#data格式：
#
#
def add_2_tensorboard(data, dir=None):
    if dir == None:
        dir = os.getcwd()
    else:
        if not os.path.exists(dir):
            os.makedirs(dir)

# def
