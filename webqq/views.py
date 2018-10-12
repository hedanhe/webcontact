from django.shortcuts import render,HttpResponse
import json,datetime

from webqq import utils

global_msg_dic = {}


def dashboard(request):

    return render(request, 'webqq/dashboard.html')

def send_msg(request):

    data = request.POST.get("data")

    data = json.loads(data)#收到消息后转成python字典
    data['date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    to_id = data.get('to_id')
    contact_type = data.get('contact_type')

    if contact_type == 'single':
        if  not to_id in global_msg_dic:
            global_msg_dic[to_id] = utils.Chat()
        global_msg_dic[to_id].msg_queue.put(data)
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


