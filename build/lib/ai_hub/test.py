'''
测试用例：
model为y=2*x
请求数据为json:{"img":3}
-----------
post请求：
curl localhost:8080/tccapi -X POST -d '{"img":3}'
返回结果 6
'''
from inferServer import inferServer
#import ai_hub.globalvar as gl
import json
import ai_hub.log as log

class myserver(inferServer):
    def __init__(self,model):
        super().__init__(model)
        log.i("init_myserver")

    #数据前处理
    def pre_process(self, data):
        log.i("my_pre_process.")
        data = data.get_data()
        #json process
        json_data = json.loads(data.decode('utf-8'))
        img = json_data.get("img")
        log.i("data: ", img)
        return img

    #pridict default run as follow：
    # def predict(self, data):
    #     ret = self.model(data)
    #     return ret

    ##数据后处理
    def post_process(self, data):
        return data



if __name__ == '__main__':
    mymodel = lambda x: x * 2
    myserver = myserver(mymodel)
    #run your server, defult ip=localhost port=8080 debuge=false
    myserver.run(debuge=True) #myserver.run("127.0.0.1", 1234)
    #myserver.run(nohug=True) #持久化模型server则设置nohug=True 如江苏气象大赛第二阶段的评测
