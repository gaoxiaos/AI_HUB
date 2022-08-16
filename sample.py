
import os
from ai_hub import Logger
#Logger用法与tensorboard的logger包一致
import numpy as np

def test_logger_plot():
    info= {
        'loss': np.random.randn(50).cumsum(),
        'accuracy': np.random.randn(50).cumsum()
    }
    logger = Logger("./logdir", openid='oWbT458JtKQGoRme28Cf1LbHwxLs')
    for tag, value in info.items():
        # print(step)
        for i, val in enumerate(value):
            logger.scalar_summary(tag, val, step=i)
    logger.show("loss")


def test_notice():
    from ai_hub.notice import notice
    # 到AIUTILS微信公众号获取个人openid如（oM8pVuBWl8Rw_vFz7rZNgeO4T8H8）,需替换为自己的openid
    nc = notice(openid="oM8pVuBWl8Rw_vFz7rZNgeO4T8H8")
    # 借助AIUTILS公众号发送消息给自己
    nc.task_complete_notice(task_name="Training", task_progree="training complete.")

# test_notice()
