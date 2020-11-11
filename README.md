# AI_HUB
AI utils for developer. such as notice、send massage when model training is over.Bind WeChat Official Account（AI_HUB）
插入在代码里的小工具，可以在模型训练结束时通过公众号及时发送微信消息给自己，提高科研效率。

## sample.py
```Python
import AI_HUB
#到AI_HUB微信公众号查看openid为oM8pVuBWl8Rw_vFz7rZNgeO4T8H8,替换为自己的openid
notice = AI_HUB("oM8pVuBWl8Rw_vFz7rZNgeO4T8H8")
#通过AI_HUB公众号发送消息给自己
notice.sendmsg("hi,AI_HUB.I am su")
```

## 获取openid
1.扫描关注公众号AI_HUB

2.发送“openid”给公众号 即可获得openid

