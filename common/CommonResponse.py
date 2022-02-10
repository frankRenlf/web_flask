import json

class CommonResponse(object):
    def __init__(self,status,msg,**kw):
        self.status=status
        self.msg=msg
        self.data=kw

    def get_status(self):
        return self.status

    def get_msg(self):
        return self.msg

    def get_data(self):
        return self.data






