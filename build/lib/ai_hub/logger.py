#utf-8
import os
import ai_hub.globalvar as gl
from ai_hub import utils
from ai_hub.utils import notice_newlogger, getopenid, notice_showlogger, get_taskid, setopenid
import tensorflow as tf


class Logger(object):
    def __init__(self, log_dir=None, openid=None):
        """Create a summary writer logging to log_dir."""
        gl._init()
        self.tf_version = tf.version.VERSION
        self.tags = []
        # 创建一个数据保存器，给定文件路径
        self.env = os.getenv("AIHUBLOGGER",None)
        if openid:
            self.openid = openid
            setopenid(openid)
        else:
            self.openid = getopenid()
        if self.openid ==None:
            raise Exception('openid is None,ex: Logger(openid="oM8pVuBWl8Rw_vFz7rZNgeO4T8H8"')
        self.taskid = get_taskid()
        if self.env and self.openid:
            log_dir = self.env
        if self.tf_version >= "2.0.0":
            self.writer = tf.summary.create_file_writer(log_dir, name=self.taskid)
        else:
            self.writer = tf.summary.FileWriter(log_dir, name=self.taskid)
        self.log_dir = log_dir
        print("log_dir : "+log_dir)

    def scalar_summary(self, tag, value, step):
        """Log a scalar variable."""
        # 保存标量，tag为标签，value是此次数值，step是时间节点
        if self.tf_version >= "2.0.0":
            with self.writer.as_default():
                tf.summary.scalar(tag, value, step=step)
                self.writer.flush()
        else:
            summary = tf.summary.scalar(value=[tf.Summary.Value(tag=tag, simple_value=value)])
            self.writer.add_summary(summary, step)
        if tag not in self.tags:
            self.tags.append(tag)
            if self.env and self.openid:
                notice_newlogger(self.openid, tag)

    def list_of_scalars_summary(self, tag_value_pairs, step):
        """Log scalar variables."""
        # 保存多个标量值，tag_value_pairs是tag和value做为数据对存放在其中
        if self.tf_version >= "2.0.0":
            with self.writer.as_default():
                for tag, value in tag_value_pairs:
                    tf.summary.scalar(tag, value, step=step)
                    self.writer.flush()
        else:
            summary = tf.Summary(value=[tf.Summary.Value(tag=tag, simple_value=value) for tag, value in tag_value_pairs])
            self.writer.add_summary(summary, step)

    def show(self, tag="all", local_auto_show=False):
        env = utils.get_env()
        if env == "TCC":
            notice_showlogger(self.openid, tag)
        #elif env == "AIHUB":#当前版本暂不开放
        #    notice_showlogger(self.openid, tag)
        else:
            CMD = "tensorboard --logdir "+ self.log_dir
            if local_auto_show:
                os.system(CMD)
            else:
                print(CMD)


