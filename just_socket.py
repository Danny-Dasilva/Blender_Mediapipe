import bpy
import socket
import json
from datetime import datetime
from mathutils import Vector
import math

    
import time
    
    
##################################
#### Starting modal to get media pipe realtime
##################################

_timer = None
_s = None
_frame = None



# record_frame_start = context.scene.sk_value_prop.sk_record_frame_start


import socket
from mathutils import Vector
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((socket.gethostname(), 1234)) #gethostname is the local address,

HEADERSIZE = 10


_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
_s.connect((socket.gethostname(), 1234)) #gethostname is the local address,

#############
#begin of connection code
def connection():
    full_msg = b''
    nem_msg = True
    while True:
        time.sleep(.1)
        msg = _s.recv(1024) 
        if nem_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            nem_msg = False

        full_msg += msg

        if len(full_msg)-HEADERSIZE >= msglen:

            d = json.loads(full_msg[HEADERSIZE:].decode('utf-8'))
            print(d)
            nem_msg = True
            full_msg = b''
            break

    if d != 'nada':
        # print('len d[0]: ', len(d[0]))
        print('Frame:',1,'bone: ',d[1][0],' x: ',d[1][1],' y: ',d[1][2],' z: ',d[1][3])

        for i in range(len(d)):
            x_pose = d[i][1]
            y_pose = d[i][2]
            z_pose = d[i][3]
            bpy.data.objects["Point."+str(1000+i)[1:]].location[0]=x_pose
            bpy.data.objects["Point."+str(1000+i)[1:]].location[1]=y_pose
            bpy.data.objects["Point."+str(1000+i)[1:]].location[2]=z_pose
        



