#-*- coding=utf-8 -*-
import base64
import datetime
passtr=''
key = str(datetime.datetime.now().month)+str(datetime.datetime.now().day)



def password(passtr):
    pass1 = 'KKNNBBO'+passtr[0:15]+'ZMXBBCS'
    pass2 = 'IINBDDB'+passtr[15:] + 'KDHHDHW'
    print base64.b64encode(pass2+pass1)

if __name__ == '__main__':
    password(passtr)



#run result:SUlOQkREQlpWZE13b3l2VmxZMGlqRG9XNkF6YjZhZWFpV3c9S0RISERIV0tLTk5CQk9VMkZzZEdWa1gxOEI1WUpaTVhCQkNT

#password=result:key



