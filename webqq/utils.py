import queue



class Chat(object):
    def __init__(self):
        self.msg_queue = queue.Queue()

    def get_msg(self):
        new_msgs = []
        if self.msg_queue.qsize() > 0:
            for msg in range(self.msg_queue.qsize()):
                new_msgs.append(self.msg_queue.get_nowait())

        else:
            #没有消息，等60秒
            try:
                print("没有新消息，等60秒```")
                new_msgs.append(self.msg_queue.get(timeout=60))
            except queue.Empty:
                print("没有消息")

        return new_msgs
