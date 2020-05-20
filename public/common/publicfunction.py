#coding=utf-8

from config import globalparam
import time
import os
from public.common.log import Log


# 截图放到report下的img目录下
logger = Log()
def mk_img_dir():
    dir_time = time.strftime('%Y%m%d')
    img_path = '%s/%s' %(globalparam.img_path, dir_time)
    if not os.path.exists(img_path):
        os.mkdir(img_path)
    return img_path

def get_screen_shot(dr):
    now_time = lambda:str(round(time.time() * 1000))
    path = '%s/%s.%s.png' %(mk_img_dir(), time.strftime('%H%M%S'), now_time()[-3:])
    dr.take_screen_shot(path)
