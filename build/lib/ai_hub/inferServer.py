"""Tests for the flatten observation wrapper."""
from flask import Flask, request
import json
import globalvar as gl
import log

app = Flask("tccapi")


@app.route("/tccapi", methods=['GET', 'POST'])
def tccapi():
    ret = ""
    if request.method== 'POST':
        data = request.get_data()
        print("data: ", data)

        # inferserver
        #myinserver = gl.get_value("myinserver")
        inferserver = gl.get_value("inferserver")
        #print(inferserver)

        data_pred = inferserver.pre_process(data)
        print("pred_data: ",data_pred)
        ret = inferserver.pridect(data_pred)
        ret = inferserver.post_process(ret)
        if not isinstance(ret, str):
            ret = str(ret)
        log.i("return: ", ret)
    else:
        log.e("please use post request.such as ：curl localhost:8080/tccapi -X POST -d \'{\"img\"/:2}\'")
    return ret


class inferServer():
    def __init__(self, model):
        self.model = model
        print("init_Server")
        gl._init()
        # gl.set_value("inferModel", model)
        gl.set_value("inferserver", self)


    def pre_process(self, data):
        return data

    def post_process(self, data):
        return data

    def pridect(self, data):
        data = self.model(data)
        return data

    def run(self, ip="127.0.0.1", port=8080, debuge=False):
        app.run(ip, port, debuge)


if __name__ == '__main__':
    myserver = inferServer("")
    myserver.run()

