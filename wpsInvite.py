import requests
from sys import argv
from json import dumps
from datetime import datetime
from time import sleep
from random import uniform
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

invite_sid = [
    "V02StVuaNcoKrZ3BuvJQ1FcFS_xnG2k00af250d4002664c02f",
    "V02SWIvKWYijG6Rggo4m0xvDKj1m7ew00a8e26d3002508b828",
    "V02Sr3nJ9IicoHWfeyQLiXgvrRpje6E00a240b890023270f97",
    "V02SBsNOf4sJZNFo4jOHdgHg7-2Tn1s00a338776000b669579",
    "V02S2oI49T-Jp0_zJKZ5U38dIUSIl8Q00aa679530026780e96",
    "V02ShotJqqiWyubCX0VWTlcbgcHqtSQ00a45564e002678124c",
    "V02SFiqdXRGnH5oAV2FmDDulZyGDL3M00a61660c0026781be1",
    "V02S7tldy5ltYcikCzJ8PJQDSy_ElEs00a327c3c0026782526",
    "V02SPoOluAnWda0dTBYTXpdetS97tyI00a16135e002684bb5c",
    "V02Sb8gxW2inr6IDYrdHK_ywJnayd6s00ab7472b0026849b17",
    "V02SwV15KQ_8n6brU98_2kLnnFUDUOw00adf3fda0026934a7f",
    "V02SC1mOHS0RiUBxeoA8NTliH2h2NGc00a803c35002693584d"
]
s = requests.session()
sidList = []
token = ''
if token == '':
    sidstr = input("sidlist:")
    tostr = input("token:")
    try:
        token = str(tostr)
        sidList = eval(sidstr)
    except:
        pass


def wps_invite(invite_userid: int):
    invite_url = 'https://zt.wps.cn/2018/clock_in/api/invite'
    cnt = 0
    for index, i in enumerate(invite_sid):
        headers = {
            'sid': i
        }
        secs = uniform(0.5, 1.2)
        sleep(secs)
        try:
            r = s.post(invite_url, headers=headers, data={
                       'invite_userid': invite_userid})
            print("ID={}, 状态码: {}, 请求信息{}".format(
                str(index+1).zfill(2), r.status_code, r.text))
            res = r.json()['result']
            if res == 'ok':
                cnt += 1
        except:
            pass
    return '{} 成功发送邀请 {} 个\n\n'.format(invite_userid, cnt)


def send2ding(msg):
    data = ''
    if type(msg) is dict:
        data = dumps(msg)
    url = 'https://oapi.dingtalk.com/robot/send?access_token=' + token
    rsp = requests.post(url, data=data, headers={
                        'Content-Type': 'application/json'}, verify=False)
    print(rsp.text)


def main():
    res = ''
    cnt = 1
    for id in sidList:
        secs = uniform(5.0, 10.0)
        print('start invite No. {} in {} secs.'.format(cnt, secs))
        sleep(secs)
        res += wps_invite(id)
        cnt += 1

    msg = {
        "msgtype": "markdown",
        "markdown": {
            "title": "WPS打卡邀请",
            "text": "#### WPS打卡邀请\n" + res
        }
    }
    send2ding(msg)


if __name__ == "__main__":
    main()
