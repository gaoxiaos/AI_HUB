# AI_HUB
AI utils for developer.
such as notice、send massage when model training is over.Bind WeChat Official Account（AI_HUB）
插入在代码里的小工具，可以在模型训练结束时通过公众号及时发送微信消息给自己，提高科研效率。
inferServer: server your ai model as a API and match the tianchi eval
简单的操作把你训练好的模型变为服务API，并且支持天池大赛的流评测。

## INSTALL
```
pip install ai-hub
```

## SAMPLE
### NOTICE
```Python
from ai_hub.notice import notice
#到AIUTILS微信公众号获取个人openid如（oM8pVuBWl8Rw_vFz7rZNgeO4T8H8）,需替换为自己的openid
nc = notice("oM8pVuBWl8Rw_vFz7rZNgeO4T8H8")
#借助AIUTILS公众号发送消息给自己
nc.task_complete_notice(task_name="Training", task_progree="training complete.")
```

### inferServer
```Python
'''
依赖：pip install ai-hub #(version>=0.1.7) 
测试用例：
model为y=2*x
请求数据为json:{"img":3}
-----------
post请求：
curl localhost:8080/tccapi -X POST -d '{"img":3}'
返回结果 6
'''
from ai_hub import inferServer
import json

class myInfer(inferServer):
    def __init__(self, model):
       	super().__init__(model)
        print("init_myInfer")
    
    #数据前处理
    def pre_process(self, data):
        print("my_pre_process")
        #json process
        json_data = json.loads(data.decode('utf-8'))
        img = json_data.get("img")
        print("processed data: ", img)
        return img
    
    #数据后处理
    def post_process(self, data):
        print("post_process")
        processed_data = data
        return processed_data
    
    #模型预测：默认执行self.model(preprocess_data)，一般不用重写
    #如需自定义，可覆盖重写
    #def pridect(self, data)：
    #    ret = self.model(data)
    #    return ret

if __name__ == "__main__":
    mymodel = lambda x: x * 2
    my_infer = myInfer(mymodel)
    my_infer.run(debuge=False) #默认为("127.0.0.1", 80)，可自定义端口，如用于天池大赛请默认即可，指定debuge=False更高效
    
```


### TccProgressBar
```Python
from ai_hub import TccProgressBar#当前版本仅在特定场景下可用
#定义progress，显示名为training，在竞赛平台TCC上显示该进度条（tccBar_show=false 不影响本地打印进度条）
progress = TccProgressBar(title="training", tccBar_show=True)
for j in progress(range(100)):
    time.sleep(0.1)
```

### TccTensorboard
```Python
from ai_hub import Logger
#Logger用法与tensorboard的logger包一致
info= {
    'loss': loss.data[0],
    'accuracy': accuracy.data[0]
}
#假设logger本地存放路径./logdir；微信接受端openid="oWbT458JtKQGoRme28Cf1LbHwxLs"
logger = Logger("./logdir", openid='oWbT458JtKQGoRme28Cf1LbHwxLs')
for tag, value in info.items():
    logger.scalar_summary(tag, value, step)
logger.show("loss")
```

## 获取OPENID
1.扫描关注公众号AIUTILS

![avatar](docs/qrcode.jpg)

2.发送“openid”给公众号 即可获得openid

