# AI_HUB
AI utils for developer. such as notice、send massage when model training is over.Bind WeChat Official Account（AI_HUB）
插入在代码里的小工具，可以在模型训练结束时通过公众号及时发送微信消息给自己，提高科研效率。

## install
```
pip install ai-hub
```

## sample
```Python
import ai_hub
#到AGIHub微信公众号获取个人openid如（oM8pVuBWl8Rw_vFz7rZNgeO4T8H8）,需替换为自己的openid
nc = ai_hub.notice("oM8pVuBWl8Rw_vFz7rZNgeO4T8H8")
#借助AGIHub公众号发送消息给自己
nc.sendmsg("hi,AI_HUB.I am su")
```

## 获取openid
1.扫描关注公众号AGIHub

![avatar](docs/qrcode.jpg)

2.发送“openid”给公众号 即可获得openid

