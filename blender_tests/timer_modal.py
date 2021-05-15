import bpy
import random
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


#_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#_s.connect((socket.gethostname(), 1234)) #gethostname is the local address,

def connection(self):
    full_msg = b''
    nem_msg = True
    while True:
        msg = self._s.recv(1024) 
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
#        print('Frame:',1,'bone: ',d[1][0],' x: ',d[1][1],' y: ',d[1][2],' z: ',d[1][3])

        for i in range(len(d)):
            x_pose = d[i][1]
            y_pose = d[i][2]
            z_pose = d[i][3]
            bpy.data.objects["Point."+str(1000+i)[1:]].location[0]=x_pose
            bpy.data.objects["Point."+str(1000+i)[1:]].location[1]=y_pose
            bpy.data.objects["Point."+str(1000+i)[1:]].location[2]=z_pose
        

class Test_PT_Panel(bpy.types.Panel):
    bl_idname = "MOCAP_IMPORT_PT_Panel_ALPHA"
    bl_label = "MOCAP PE Import Data ALPHA"
    bl_category = "testing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator('wm.modal_timer_operator', text="MediaPipe Real Time")


class ModalTimerOperator(bpy.types.Operator):
    """Operator which runs its self from a timer"""
    bl_idname = "wm.modal_timer_operator"
    bl_label = "Modal Timer Operator"

    limits = bpy.props.IntProperty(default=0)
    _timer = None

    def modal(self, context, event):
        if event.type in {'RIGHTMOUSE', 'ESC'}:
            self.limits = 0
            self.cancel(context)
            return {'FINISHED'}

        if event.type == 'TIMER':
            connection(self)

        return {'PASS_THROUGH'}

    def execute(self, context):
        wm = context.window_manager
        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._s.connect((socket.gethostname(), 1234)) #gethostname is the local address,

        self._timer = wm.event_timer_add(time_step=0.01, window=context.window)
        wm.modal_handler_add(self)
        print('MODAL!!!!!!!!!!!!!!!')
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)


def register():
    bpy.utils.register_class(ModalTimerOperator)
    bpy.utils.register_class(Test_PT_Panel)


def unregister():
    bpy.utils.unregister_class(ModalTimerOperator)
    bpy.utils.unregister_class(Test_PT_Panel)

if __name__ == "__main__":
    register()

    # test call
#    bpy.ops.wm.modal_timer_operator()