from inferServer import inferServer
import globalvar as gl
import json
import log
import torch
import torch.nn as nn

class myserver(inferServer):
    def __init__(self,model):
        super().__init__(model)
        print("init_myserver")
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.device = device
        self.model= model.to(device)

    def pre_process(self, data):
        log.i("my_pre_process.")
        #json process
        json_data = json.loads(data.decode('utf-8'))
        img = json_data.get("img")
        log.i("data: ", img)
        return torch.tensor(img).to(self.device)

    #pridict default run as follow：
    # def predict(self, data):
    #     ret = self.model(data)
    #     return ret

    def post_process(self, data):
        return data.cpu()


class mymodel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(1, 1)
        self.model = lambda x: torch.mul(x , 2)

    def forward(self, x):
        y = self.model(x)
        # y = self.fc(y)
        return y


if __name__ == '__main__':
    mymodel = mymodel()
    myserver = myserver(mymodel)
    #run your server, defult ip=localhost port=8080 debuge=false
    myserver.run(debuge=True) #myserver.run("127.0.0.1", 1234)
