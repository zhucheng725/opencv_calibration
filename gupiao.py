
# -*- coding:utf-8 -*-
 
import tushare as ts
import os
import threading
import time
 

from datetime import datetime
from datetime import timedelta
from datetime import timezone

SHA_TZ = timezone(
    timedelta(hours=8),
    name='Asia/Shanghai',
)




def get():
    i = os.system("clear")                                          # 清屏操作
    df = ts.get_realtime_quotes(['002594', '600577'])

    # 协调世界时
    utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
    # 北京时间
    beijing_now = utc_now.astimezone(SHA_TZ)
    print(beijing_now, beijing_now.tzname())
 
    print(df['code'][1] + "  " + df['name'][1] + "  " + str(round((float(df['price'][1]) - float(df['pre_close'][1])) / float(df['pre_close'][1]) * 100, 2)) + "%" + "  ")
 
    print(df['code'][0] + "  " + df['name'][0] + "  " + str(round((float(df['price'][0]) - float(df['pre_close'][0])) / float(df['pre_close'][0]) * 100, 2)) + "%" + "  ")
    global timer
    timer = threading.Timer(10.0, get, [])
    timer.start()
 
if __name__ == "__main__":
    timer = threading.Timer(10.0, get, [])
    timer.start()



