import requests
import re
import time

from 汉语模组 import *

请求头 = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6",
    "Connection": "keep-alive",
    "Content-Length": "611",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "JSESSIONID=A5B951D688372331B6A43069C4A8A08B; iPlanetDirectoryPro=gQvs4O0dD95C7RcnPJFR2T",
    "Host": "yktwd.csust.edu.cn:8988",
    "Origin": "http://yktwd.csust.edu.cn:8988",
    "Referer": "http://yktwd.csust.edu.cn:8988/web/common/checkEle.html?ticket=ED96D331AA164FDDA7F4181338A38B93",
    "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 13421.99.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

def 获取电费json(房间编号, 前一次电费):
    链接 = "http://yktwd.csust.edu.cn:8988/web/Common/Tsm.html"
    负载 = ("jsondata=%7B+%22query_elec_roominfo%22%3A+%7B+%22aid%22%3A%220030000000002501%22%2C+%22account%22%3A+%22227622%22%2C%22room%22%3A+%7B+%22roomid%22%3A+%22"
            + 房间编号
            + "%22%2C+%22room%22%3A+%22"
            + 房间编号
            + "%22+%7D%2C++%22floor%22%3A+%7B+%22floorid%22%3A+%22%22%2C+%22floor%22%3A+%22%22+%7D%2C+%22area%22%3A+%7B+%22area%22%3A+%22%E4%BA%91%E5%A1%98%E6%A0%A1%E5%8C%BA%22%2C+%22areaname%22%3A+%22%E4%BA%91%E5%A1%98%E6%A0%A1%E5%8C%BA%22+%7D%2C+%22building%22%3A+%7B+%22buildingid%22%3A+%22106%22%2C+%22building%22%3A+%22%E8%A1%8C%E5%81%A5%E8%BD%A92%E6%A0%8BB%E5%8C%BA%22+%7D+%7D+%7D&funname=synjones.onecard.query.elec.roominfo&json=true")
    try:
        结果 = requests.post(headers = 请求头, url = 链接, data = 负载)
        打印(结果.text)

        剩余电费 = str(re.findall(re.compile(r'" 房间剩余电量(.*?)",'), 结果.text)[0])
        if 浮点(剩余电费).大于(5) and 浮点(剩余电费).小于(前一次电费) and 浮点(剩余电费).大于(前一次电费, 然后=lambda x: x-1):
            return float(前一次电费)
    except Exception:
        return float(前一次电费)

    return float(剩余电费)


