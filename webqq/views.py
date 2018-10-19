from django.shortcuts import render,HttpResponse
import json,datetime
import requests

from webqq import utils

global_msg_dic = {}


def dashboard(request):

    return render(request, 'webqq/dashboard.html')

def send_msg(request):

    data = request.POST.get("data")

    data = json.loads(data)#收到消息后转成python字典
    data['date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    to_id = data.get('to_id')
    from_id = data.get('from_id')
    contact_type = data.get('contact_type')

    if contact_type == 'single':

        if  not to_id in global_msg_dic:
            global_msg_dic[to_id] = utils.Chat()
            print(data)
        global_msg_dic[to_id].msg_queue.put(data)
        if to_id == "3":
            #当给id=3的好友发送消息时开启自动回复
            reply_msg = reply(data.get("msg"))
            reply_data = {}
            reply_data['date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            reply_data['from_id'] = to_id
            reply_data['to_id'] = from_id
            reply_data['contact_type'] = 'single'
            reply_data['msg'] = reply_msg
            print(reply_data)
            global_msg_dic[from_id].msg_queue.put(reply_data)

        return HttpResponse("ok")
    elif contact_type == 'group':
        return HttpResponse("ok")


def get_new_msg(request):

    uid = request.GET.get('uid')
    res = []
    if uid:
        if not uid in global_msg_dic:
            global_msg_dic[uid] = utils.Chat()

        res = global_msg_dic[uid].get_msg()

    return HttpResponse(json.dumps(res))


def reply(message):
    #自动回复功能
    apiUrl = 'http://www.tuling123.com/openapi/api'

    def get_info(message):
        data = {
            'key': '20c1796ea07e4579b1a0ec94db90fb87',
            'info': message,
            'userid': 'robot',
        }

        try:
            info = requests.post(apiUrl, data=data).json()["text"]
            print("回复消息： %s" % info)
            return info
        except:
            return None


    print("收到消息： %s" % message)
    defaulReply = "我知道了"

    #调用图灵接口,接收回复的语句
    reply_msg = get_info(message)

    if len(reply_msg) == 0:
        reply_msg = defaulReply

    return reply_msg




