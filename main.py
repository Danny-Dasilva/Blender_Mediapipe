
import json
import os
import bpy
from bpy import context
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator
from bpy.props import StringProperty, BoolProperty, EnumProperty
import math
import bpy
import math
import bpy


class Test_PT_Panel(bpy.types.Panel):
    bl_idname = "MOCAP_IMPORT_PT_Panel_ALPHA"
    bl_label = "MOCAP PE Import Data ALPHA"
    bl_category = "MOCAP_ALPHA"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    
    def draw(self, context):
        layout = self.layout

        sk_value_prop = context.scene.sk_value_prop
        # percent_render_var = sk_value_prop.sk_value

        # row = layout.row()
        # row.prop(sk_value_prop, "sk_raw_bool", text="Raw Import")
       
        # row = layout.row()
        # row.operator('mocap.import_easymocap', text="Import EasyMOCAP")
        row = layout.row()
        row.prop(sk_value_prop, "sk_record_bool", text="Record Realtime")
        row = layout.row()
        row.prop(sk_value_prop, "sk_record_frame_start", text="Frame to start Recording")
        
        row = layout.row()
        row.operator('mocap.mediapipe_prepare_sk_rt', text="Prepare MP Skeleton for RT")

        layout.row().separator()


        
        layout.prop(sk_value_prop, "sk_value", text="SK Mult")
        layout.operator('mocap.import_mediapipe_reload', text="Reload MP Skeleton for RT")
        # row = layout.row()
        # row.operator('mocap.import_frankmocap', text="SK Import FrankMocap")
        # row = layout.row()
        # row.operator('mocap.import_vibe', text="SK Import VIBE")
   
        # row = layout.row()
        # row.operator('mocap.mediapipe_pose', text="SK Generate Mocap (MediaPipe)")
        # layout.row().separator()
        layout.row().separator()
        
        row = layout.row()
        row.operator('mocap.mediapipe_pose_rt', text="MediaPipe Real Time")
        layout.row().separator()
        row = layout.row()
        row.prop(sk_value_prop, "sk_socket_buffer", text="Buffer")
        row = layout.row()
        row.prop(sk_value_prop, "sk_refresh_rate", text="Refresh Rate")
        
        

        # Create two columns, by using a split layout.
        # split = layout.split()

        # # First column
        # col = split.column()
        # # col.label(text="Column One:")
        # # layout.label(text='Original angles')
        # # layout.label(text='x: '+ '%.2f' %sk_value_prop.sk_root_rot_x)
        # # layout.label(text='y: '+ '%.2f' %sk_value_prop.sk_root_rot_y)
        # # layout.label(text='z: '+ '%.2f' %sk_value_prop.sk_root_rot_z)

        # col.label(text='Original angles')
        # col.label(text='x: '+ '%.2f' %sk_value_prop.sk_root_rot_x)
        # col.label(text='y: '+ '%.2f' %sk_value_prop.sk_root_rot_y)
        # col.label(text='z: '+ '%.2f' %sk_value_prop.sk_root_rot_z)

        # # Second column, aligned
        # col = split.column(align=True)
        # col.label(text="Actual Angle:")
        # col.label(text='x: '+ '%.2f' %sk_value_prop.sk_root_actual_rot_x)
        # col.label(text='y: '+ '%.2f' %sk_value_prop.sk_root_actual_rot_y)
        # col.label(text='z: '+ '%.2f' %sk_value_prop.sk_root_actual_rot_z)


        

class Modify_PT_Panel(bpy.types.Panel):
    bl_idname = "MODIFY_PT_Panel_ALPHA"
    bl_label = "Modify Data ALPHA"
    bl_category = "MOCAP_ALPHA"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    
    def draw(self, context):
        layout = self.layout

        sk_value_prop = context.scene.sk_value_prop
        # percent_render_var = sk_value_prop.sk_value

        layout.label(text=" Convert axis")
        row = layout.row()
        # row.prop(sk_value_prop, "sk_from_axis", text="From")
        # row.prop(sk_value_prop, "sk_to_axis", text="To")
        # row = layout.row()
        # row.operator('mocap.convert_axis', text='Convert')
        # row = layout.row()
        # row.label(text='----------')
        # row = layout.row()
        # row.operator('mocap.reset_location', text='Reset loc')
        # row.operator('mocap.reset_rotation', text='Reset rot')
        # row.operator('mocap.foot_high', text='Foot')
        # row = layout.row()
        # row.operator('mocap.smooth_bones', text='Smooth Curves')
        # row = layout.row()
        # row.label(text='----------')
        # row = layout.row()
        # row.label(text='Compensate Rotation')
        # row = layout.row()
        # row.prop(sk_value_prop, "sk_rot_compens_x", text="x")
        # row.prop(sk_value_prop, "sk_rot_compens_y", text="y")
        # row.prop(sk_value_prop, "sk_rot_compens_z", text="z")
        # row = layout.row()
        # row.operator('mocap.compensate_rotation', text='Rotate')



class Install_PT_Panel(bpy.types.Panel):
    bl_idname = "INSTALL_PT_Panel_ALPHA"
    bl_label = "Install PyPacks ALPHA"
    bl_category = "MOCAP_ALPHA"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    
    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('install.mediapipe_package', text="Install python Mediapipe Package")
        row = layout.row()
        row.operator('install.joblib_package', text="Install Joblib (Vibe requirement)")

class Debug_PT_Panel(bpy.types.Panel):
    bl_idname = "Debug_PT_Panel_ALPHA"
    bl_label = "Debug Panel"
    bl_category = "MOCAP_ALPHA"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    
    def draw(self, context):
        layout = self.layout
        sk_value_prop = context.scene.sk_value_prop

        row = layout.row()
        row.label(text='Debug skeleton size')
        row = layout.row()
        row.label(text='Main Structure')
        row = layout.row()
        row.prop(sk_value_prop, "sk_spine_mulitplier", text="Spine: ")
        row.prop(sk_value_prop, "sk_neck_mulitplier", text="Neck")
        row = layout.row()
        row.prop(sk_value_prop, "sk_head_mulitplier", text="Head")

        layout.row().separator()
        row = layout.row()
        
        row.label(text='Arms')
        row = layout.row()
        row.prop(sk_value_prop, "sk_forearm_mulitplier", text="Forearm: ")
        row.prop(sk_value_prop, "sk_arm_mulitplier", text="Arm: ")

        layout.row().separator()
        row = layout.row()
        row.label(text='Legs')
        row = layout.row()
        row.prop(sk_value_prop, "sk_tigh_mulitplier", text="Tigh: ")
        row.prop(sk_value_prop, "sk_leg_mulitplier", text="Leg: ")
        row = layout.row()
        row.prop(sk_value_prop, "sk_foot_mulitplier", text="Foot: ")

from bpy.props import (#StringProperty,
                    #    BoolProperty,
                      IntProperty,
                      FloatProperty,
#                       FloatVectorProperty,
#                       EnumProperty,
                       PointerProperty,
                       )
from bpy.props import (StringProperty,
                       BoolProperty,
                      IntProperty,
                      FloatProperty,
                    #   FloatVectorProperty,
                      EnumProperty,
                    #    PointerProperty,
                       )
from bpy.types import (Panel,
                       Operator,
                       AddonPreferences,
                       PropertyGroup,
                       )



class MySettings(PropertyGroup):
    sk_value: FloatProperty(name="multiplier", description="Multiplier for base proportion of the bones", default=0.9)
    sk_rot_compens_x: IntProperty(name="Rotation_compensate_x", description="Value to compensate Roation X", default=0)
    sk_rot_compens_y: IntProperty(name="Rotation_compensate_y", description="Value to compensate Roation Y", default=0)
    sk_rot_compens_z: IntProperty(name="Rotation_compensate_z", description="Value to compensate Roation Z", default=0)
    
    sk_rot_original: StringProperty(name="rotation", description="rotation")

    sk_root_rot_x: FloatProperty(name="original rotation x", description="original rotation of root bone x")
    sk_root_rot_y: FloatProperty(name="original rotation y", description="original rotation of root bone y")
    sk_root_rot_z: FloatProperty(name="original rotation z", description="original rotation of root bone z")

    sk_root_actual_rot_x: FloatProperty(name="Actual rotation x", description="Actual rotation of root bone x")
    sk_root_actual_rot_y: FloatProperty(name="Actual rotation y", description="Actual rotation of root bone y")
    sk_root_actual_rot_z: FloatProperty(name="Actual rotation z", description="Actual rotation of root bone z")

    sk_raw_bool: BoolProperty(name='raw_bool', default=False)
    sk_from_axis: EnumProperty(
        name= "From Axis",
        description="From specific axis of animation",
        items= [('from_x', "x","Choose origin x axis"),
                ('from_y', "y","Choose origin y axis"),
                ('from_z', "z","Choose origin z axis")
        ], 
        default = 'from_y'
    )
    sk_to_axis: EnumProperty(
        name= "To Axis",
        description="To specific axis of animation",
        items= [('to_x', "x","Choose destination x axis"),
                ('to_y', "y","Choose destination y axis"),
                ('to_z', "z","Choose destination z axis")
        ],
        default = 'to_z'
    )

    sk_spine_mulitplier: FloatProperty(name="Spine size multiplier", description="Ajust the Spine size", default=1)
    sk_neck_mulitplier: FloatProperty(name="Neck size multiplier", description="Ajust the Neck size", default=1)
    sk_head_mulitplier: FloatProperty(name="Head size multiplier", description="Ajust the Head size", default=1)

    sk_forearm_mulitplier: FloatProperty(name="Forearm size multiplier", description="Ajust the Forearm size", default=1)
    sk_arm_mulitplier: FloatProperty(name="Arm size multiplier", description="Ajust the Arm size", default=1)

    sk_tigh_mulitplier: FloatProperty(name="Thigh size multiplier", description="Ajust the Thigh size", default=1)
    sk_leg_mulitplier: FloatProperty(name="Leg size multiplier", description="Ajust the Leg size", default=1)
    sk_foot_mulitplier: FloatProperty(name="Foot size multiplier", description="Ajust the Foot size", default=1)


    sk_socket_buffer: IntProperty(name="Socket buffer", description="Socket buffer value", default=1024)
    sk_refresh_rate: FloatProperty(name="Refresh_rate", description="Value of refresh rate", default=0.1)
    
    sk_record_bool: BoolProperty(name='record_bool', default=False)
    sk_record_frame_start: IntProperty(name='Frame to start recording',description="Frame to start recording", default=1)

class helper_functions(object):
    def anim_to_origin():
        f_start = bpy.context.scene.frame_start
        f_end = bpy.context.scene.frame_end

        bpy.context.scene.frame_current=f_start

        #==========================================
        #selecting and making the armature Active
        #selecionando armature
        #==========================================
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')


        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        armature = obs[len(obs)-1].name

        #bpy.data.objects[armature].select_set(True)
        obs[len(obs)-1].select_set(True)
        view_layer = bpy.context.view_layer
        #Armature_obj = bpy.context.scene.objects[armature]
        Armature_obj = obs[len(obs)-1]
        view_layer.objects.active = Armature_obj

        #############################################################################
        ##found that to move the animation to the center, 
        ##I just have to subtract the inicial frame loc and rot from the other frames
        #########
        x_dif = bpy.context.object.pose.bones["Root"].rotation_euler[0] * -1
        y_dif = bpy.context.object.pose.bones["Root"].rotation_euler[1] * -1
        z_dif = bpy.context.object.pose.bones["Root"].rotation_euler[2] * -1


        x_loc_dif = bpy.context.object.pose.bones["Root"].location[0] * -1
        y_loc_dif = bpy.context.object.pose.bones["Root"].location[1] * -1
        z_loc_dif = bpy.context.object.pose.bones["Root"].location[2] * -1

        bpy.ops.object.mode_set(mode='EDIT')
        z_high_to_add = bpy.context.object.data.edit_bones["Foot_L"].tail.z
        bpy.ops.object.mode_set(mode='POSE')

        range(f_start,f_end+1)

        for f in range(f_start,f_end+1):
            print('frame: ',f)
            bpy.context.scene.frame_current = f
            bpy.context.view_layer.update()
        #    print('rot orig x: ',bpy.context.object.pose.bones["Root"].rotation_euler[0])
        #    print('rot x: ',bpy.context.object.pose.bones["Root"].rotation_euler[0] + x_dif)
            bpy.context.object.pose.bones["Root"].rotation_euler[0] = bpy.context.object.pose.bones["Root"].rotation_euler[0] + x_dif 
            bpy.context.object.pose.bones["Root"].rotation_euler[1] = bpy.context.object.pose.bones["Root"].rotation_euler[1] + y_dif 
            bpy.context.object.pose.bones["Root"].rotation_euler[2] = bpy.context.object.pose.bones["Root"].rotation_euler[2] + z_dif 
            bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='rotation_euler',frame=f)
            #################
            ## location to origin
            ##
            bpy.context.object.pose.bones["Root"].location[0] = bpy.context.object.pose.bones["Root"].location[0] + x_loc_dif
            bpy.context.object.pose.bones["Root"].location[1] = bpy.context.object.pose.bones["Root"].location[1] + y_loc_dif
            bpy.context.object.pose.bones["Root"].location[2] = bpy.context.object.pose.bones["Root"].location[2] + z_loc_dif
            bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='location',frame=f)


        #Check if need to transpose axis
        if abs(abs(math.degrees(x_dif))-90) < 45 or abs(abs(math.degrees(x_dif))-270) < 45:
        # if 1==1:
            #############################
            #rotate oprientation z por y
            for f in range(f_start,f_end+1):
                print('frame: ',f)
                bpy.context.scene.frame_current = f
                bpy.context.view_layer.update()   
                #changing location
                bone_root_loc_x = bpy.context.object.pose.bones["Root"].location[0]
                bone_root_loc_y = bpy.context.object.pose.bones["Root"].location[1]
                bone_root_loc_z = bpy.context.object.pose.bones["Root"].location[2]
                #changing orientation from z to y
                #z=y
                bpy.context.object.pose.bones["Root"].location[2] = bone_root_loc_y
                #y=z
                bpy.context.object.pose.bones["Root"].location[1] = bone_root_loc_z
                bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='location',frame=f)
                #######################
                ## rotation orientation change
                ##
                #rotation the rotation z to y
                bone_root_rot_x = bpy.context.object.pose.bones["Root"].rotation_euler[0]
                bone_root_rot_y = bpy.context.object.pose.bones["Root"].rotation_euler[1]
                bone_root_rot_z = bpy.context.object.pose.bones["Root"].rotation_euler[2]
                #changing orientation from z to y
                #z=y
                bpy.context.object.pose.bones["Root"].rotation_euler[2] = bone_root_rot_y
                #y=z
                bpy.context.object.pose.bones["Root"].rotation_euler[1] = bone_root_rot_z
                bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='rotation_euler',frame=f)
            


        ###############################
        ## adjust the foot to z=0
        for f in range(f_start,f_end+1):
        #    print('frame: ',f)
            bpy.context.scene.frame_current = f
            bpy.context.view_layer.update()
            bpy.context.object.pose.bones["Root"].location[1] = bpy.context.object.pose.bones["Root"].location[1] + abs(z_high_to_add)
            bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='location',frame=f)


        
        # print('org x: ', math.degrees(x_dif), 'orig y: ', math.degrees(y_dif), 'orig_z: ', math.degrees(z_dif)) 
        rot_original = 'x: ', math.degrees(x_dif), ' y: ', math.degrees(y_dif), ' z: ', math.degrees(z_dif)
        print(rot_original)
        bpy.ops.object.mode_set(mode='OBJECT')
        
        return (math.degrees(x_dif),math.degrees(y_dif),math.degrees(z_dif))


    def compensate_rot(x,y,z):
        f_start = bpy.context.scene.frame_start
        f_end = bpy.context.scene.frame_end

        #just to compensate grad
        x_grad_compensate = x
        y_grad_compensate = y
        z_grad_compensate = z
        for f in range(f_start,f_end+1):
            print('frame: ',f)
            bpy.context.scene.frame_current = f
            bpy.context.view_layer.update()
            print('rot orig x: ',bpy.context.object.pose.bones["Root"].rotation_euler[0])
            print('rot x: ',bpy.context.object.pose.bones["Root"].rotation_euler[0]  +math.radians(x_grad_compensate))
            bpy.context.object.pose.bones["Root"].rotation_euler[0] = bpy.context.object.pose.bones["Root"].rotation_euler[0]  +math.radians(x_grad_compensate)
            bpy.context.object.pose.bones["Root"].rotation_euler[1] = bpy.context.object.pose.bones["Root"].rotation_euler[1]  +math.radians(y_grad_compensate)
            bpy.context.object.pose.bones["Root"].rotation_euler[2] = bpy.context.object.pose.bones["Root"].rotation_euler[2]  +math.radians(z_grad_compensate)
            bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='rotation_euler',frame=f)


        return True

    def rotate_orientation(from_axis,to_axis):
        #############################
        #rotate oprientation acording to choice on menu

        f_start = bpy.context.scene.frame_start
        f_end = bpy.context.scene.frame_end

        if from_axis == 'x':
            from_ax = 0
        elif from_axis == 'y':
            from_ax = 1
        elif from_axis == 'z':
            from_ax = 2

        if to_axis == 'x':
            to_ax = 0
        elif to_axis == 'y':
            to_ax = 1
        elif to_axis == 'z':
            to_ax = 2

        if (from_axis == 'x' and to_axis == 'y') or (to_axis == 'x' and from_axis == 'y'):
            rotate_axis = 'z'
        elif (from_axis == 'y' and to_axis == 'z') or (to_axis == 'y' and from_axis == 'z'):
            rotate_axis = 'x'
        elif (from_axis == 'z' and to_axis == 'x') or (to_axis == 'z' and from_axis == 'x'):
            rotate_axis = 'y'

        if 'rotate_axis' in locals():
            if rotate_axis == 'x':
                rot_ax = 0
            elif rotate_axis == 'y':
                rot_ax = 1
            elif rotate_axis == 'z':
                rot_ax = 2
        
            if from_axis != rot_ax:
                for f in range(f_start,f_end+1):
                    print('frame: ',f)
                    bpy.context.scene.frame_current = f
                    bpy.context.view_layer.update()   

                    ##################
                    #changing location

                    bone_root_loc = []
                    bone_root_loc.append(bpy.context.object.pose.bones["Root"].location[0])
                    bone_root_loc.append(bpy.context.object.pose.bones["Root"].location[1])
                    bone_root_loc.append(bpy.context.object.pose.bones["Root"].location[2])
                    # bone_root_loc_x = bpy.context.object.pose.bones["Root"].location[0]
                    # bone_root_loc_y = bpy.context.object.pose.bones["Root"].location[1]
                    # bone_root_loc_z = bpy.context.object.pose.bones["Root"].location[2]
                    
                    #from-to
                    # bpy.context.object.pose.bones["Root"].location[2] = bone_root_loc_y
                    bpy.context.object.pose.bones["Root"].location[from_ax] = bone_root_loc[to_ax]
                    
                    #to-from
                    # bpy.context.object.pose.bones["Root"].location[1] = bone_root_loc_z
                    bpy.context.object.pose.bones["Root"].location[to_ax] = bone_root_loc[from_ax]
                    bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='location',frame=f)
                    

                    #######################
                    ## rotation orientation change
                    ##
                    bone_root_rot=[]

                    bone_root_rot.append(bpy.context.object.pose.bones["Root"].rotation_euler[0])
                    bone_root_rot.append(bpy.context.object.pose.bones["Root"].rotation_euler[1])
                    bone_root_rot.append(bpy.context.object.pose.bones["Root"].rotation_euler[2])

                    # bone_root_rot_x = bpy.context.object.pose.bones["Root"].rotation_euler[0]
                    # bone_root_rot_y = bpy.context.object.pose.bones["Root"].rotation_euler[1]
                    # bone_root_rot_z = bpy.context.object.pose.bones["Root"].rotation_euler[2]
                    
                    #from-to
                    bpy.context.object.pose.bones["Root"].rotation_euler[from_ax] = bone_root_rot[to_ax]
                    #to-from
                    bpy.context.object.pose.bones["Root"].rotation_euler[to_ax] = bone_root_rot[from_ax]

                    #convert adding 90 degrees
                    bpy.context.object.pose.bones["Root"].rotation_euler[rot_ax] = bpy.context.object.pose.bones["Root"].rotation_euler[rot_ax] + math.radians(-90)

                    bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='rotation_euler',frame=f)


        return True

    def reset_loc(): #make the animation start from where the boneas are located
        f_start = bpy.context.scene.frame_start
        f_end = bpy.context.scene.frame_end

        x_loc_dif = bpy.context.object.pose.bones["Root"].location[0] * -1
        y_loc_dif = bpy.context.object.pose.bones["Root"].location[1] * -1
        z_loc_dif = bpy.context.object.pose.bones["Root"].location[2] * -1

        for f in range(f_start,f_end+1):
            print('frame: ',f)
            bpy.context.scene.frame_current = f
            bpy.context.view_layer.update()

            #################
            ## location to origin
            ##
            bpy.context.object.pose.bones["Root"].location[0] = bpy.context.object.pose.bones["Root"].location[0] + x_loc_dif
            bpy.context.object.pose.bones["Root"].location[1] = bpy.context.object.pose.bones["Root"].location[1] + y_loc_dif
            bpy.context.object.pose.bones["Root"].location[2] = bpy.context.object.pose.bones["Root"].location[2] + z_loc_dif
            bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='location',frame=f)

        return True

    def reset_rot():
        f_start = bpy.context.scene.frame_start
        f_end = bpy.context.scene.frame_end

        x_dif = bpy.context.object.pose.bones["Root"].rotation_euler[0] * -1
        y_dif = bpy.context.object.pose.bones["Root"].rotation_euler[1] * -1
        z_dif = bpy.context.object.pose.bones["Root"].rotation_euler[2] * -1

        for f in range(f_start,f_end+1):
            print('frame: ',f)
            bpy.context.scene.frame_current = f
            bpy.context.view_layer.update()

            bpy.context.object.pose.bones["Root"].rotation_euler[0] = bpy.context.object.pose.bones["Root"].rotation_euler[0] + x_dif 
            bpy.context.object.pose.bones["Root"].rotation_euler[1] = bpy.context.object.pose.bones["Root"].rotation_euler[1] + y_dif 
            bpy.context.object.pose.bones["Root"].rotation_euler[2] = bpy.context.object.pose.bones["Root"].rotation_euler[2] + z_dif 
            bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='rotation_euler',frame=f)

        return True

    def foot_high():
        f_start = bpy.context.scene.frame_start
        f_end = bpy.context.scene.frame_end

        bpy.ops.object.mode_set(mode='EDIT')
        z_high_to_add = bpy.context.object.data.edit_bones["Foot_L"].tail.z
        bpy.ops.object.mode_set(mode='POSE')

        for f in range(f_start,f_end+1):
        #    print('frame: ',f)
            bpy.context.scene.frame_current = f
            bpy.context.view_layer.update()
            bpy.context.object.pose.bones["Root"].location[1] = bpy.context.object.pose.bones["Root"].location[1] + abs(z_high_to_add)
            bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='location',frame=f)

        bpy.ops.object.mode_set(mode='OBJECT')
        return True

    def compensate_rot(x,y,z):
        f_start = bpy.context.scene.frame_start
        f_end = bpy.context.scene.frame_end

        #just to compensate grad
        x_grad_compensate = x
        y_grad_compensate = y
        z_grad_compensate = z
        for f in range(f_start,f_end+1):
            print('frame: ',f)
            bpy.context.scene.frame_current = f
            bpy.context.view_layer.update()
            print('rot orig x: ',bpy.context.object.pose.bones["Root"].rotation_euler[0])
            print('rot x: ',bpy.context.object.pose.bones["Root"].rotation_euler[0]  +math.radians(x_grad_compensate))
            bpy.context.object.pose.bones["Root"].rotation_euler[0] = bpy.context.object.pose.bones["Root"].rotation_euler[0]  +math.radians(x_grad_compensate)
            bpy.context.object.pose.bones["Root"].rotation_euler[1] = bpy.context.object.pose.bones["Root"].rotation_euler[1]  +math.radians(y_grad_compensate)
            bpy.context.object.pose.bones["Root"].rotation_euler[2] = bpy.context.object.pose.bones["Root"].rotation_euler[2]  +math.radians(z_grad_compensate)
            bpy.context.object.pose.bones["Root"].keyframe_insert(data_path='rotation_euler',frame=f)

        return True

    def get_rotations():

        bpy.context.scene.frame_current = 1
        bpy.context.view_layer.update()
        actual_rot_x = bpy.context.object.pose.bones["Root"].rotation_euler[0]
        actual_rot_y = bpy.context.object.pose.bones["Root"].rotation_euler[1]
        actual_rot_z = bpy.context.object.pose.bones["Root"].rotation_euler[2]

        return (actual_rot_x, actual_rot_y, actual_rot_z)

    # types = {'VIEW_3D', 'TIMELINE', 'GRAPH_EDITOR', 'DOPESHEET_EDITOR', 'NLA_EDITOR', 'IMAGE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'TEXT_EDITOR', 'NODE_EDITOR', 'LOGIC_EDITOR', 'PROPERTIES', 'OUTLINER', 'USER_PREFERENCES', 'INFO', 'FILE_BROWSER', 'CONSOLE'}

    def smooth_curves(o):
        current_area = bpy.context.area.type
        layer = bpy.context.view_layer

        # select all (relevant) bones
        for b in o.data.bones:
            b.select = False
        o.data.bones[0].select = True
        layer.update()

        # change to graph editor
        bpy.context.area.type = "GRAPH_EDITOR"

        # # lock or unlock the respective fcurves
        # for fc in o.animation_data.action.fcurves:
        #     print(fc.data_path)
        #     if "location" in fc.data_path:
        #         fc.lock = False
        #     else:
        #         fc.lock = True

        layer.update()
        # smooth curves of all selected bones
        bpy.ops.graph.smooth()

        # switch back to original area
        bpy.context.area.type = current_area

        # deselect all (relevant) bones
        for b in o.data.bones:
            b.select = False
        layer.update()

        return True

class skeleton_import(object):
    def middle_point(p1,p2,p_middle):
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[p1].select_set(True)
        bpy.data.objects[p2].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects[p2]
        obs = bpy.context.selected_objects
        n = len(obs)
        #    print('n: ',n)
        assert(n)
        #scene.cursor.location = sum([o.matrix_world.translation for o in obs], Vector()) / n
        bpy.data.objects[p_middle].location = sum([o.matrix_world.translation for o in obs], Vector()) / n

    def create_dots(name, amount):
        #remove Collection
        if bpy.data.collections.find(name) >= 0:
            collection = bpy.data.collections.get(name)
            #
            for obj in collection.objects:
                bpy.data.objects.remove(obj, do_unlink=True)
            bpy.data.collections.remove(collection)
        #cria os pontos nuima collection chamada Points
        #=====================================================
        collection = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(collection)
        #
        layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
        bpy.context.view_layer.active_layer_collection = layer_collection
        #
        for point in range(amount):
            bpy.ops.mesh.primitive_plane_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
            bpy.ops.mesh.merge(type='CENTER')
            bpy.ops.object.editmode_toggle()
            bpy.context.active_object.name = name+'.'+str(1000+point)[1:]
        #=====================================================

    def remove_dots(name):    
        #apagar collection points criada
        collection = bpy.data.collections.get(name)
        #
        for obj in collection.objects:
            bpy.data.objects.remove(obj, do_unlink=True)
        bpy.data.collections.remove(collection)

    def distance(point1, point2) -> float:
        #Calculate distance between two points in 3D.
        #    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2)
        return math.sqrt((point2.location[0] - point1.location[0]) ** 2 + (point2.location[1] - point1.location[1]) ** 2 + (point2.location[2] - point1.location[2]) ** 2)

    def size_bone(point_name1, point_name2, bone):
        p1 = bpy.data.objects[point_name1]
        p2 = bpy.data.objects[point_name2]
        #edit bones
        if bpy.context.active_object.mode == 'EDIT':
            bpy.context.object.data.edit_bones[bone].length= distance(p1,p2)
        else:
            bpy.ops.object.editmode_toggle()
            bpy.context.object.data.edit_bones[bone].length= distance(p1,p2)
        bpy.ops.object.editmode_toggle()

    def create_bones(bones_list):
        #===================================
        #creating bones
        #====================================

        bpy.ops.object.armature_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1)) #cria armature e primeiro bone
        #bpy.ops.object.editmode_toggle()
        #bpy.data.armatures['Armature'].edit_bones.active = bpy.context.object.data.edit_bones['Bone']


        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs


        bpy.ops.armature.select_all(action='DESELECT')
        obs[len(obs)-1].data.edit_bones['Bone'].select_tail=True


        
        bpy.ops.armature.bone_primitive_add()#Spine
        #Neck
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1)})
        #Face
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1)})


        bpy.ops.armature.bone_primitive_add()#Arm_L
        #Forearm_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1)})
        
        bpy.ops.armature.bone_primitive_add()#Arm_R
        #Forearm_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1)})
        
        bpy.ops.armature.bone_primitive_add()#Thigh_L
        #Leg_L
        #Foot_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1)})
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1)})
        
        bpy.ops.armature.bone_primitive_add()#Thigh_R
        #Leg_R
        #Foot_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1)})
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1)})
    
        for i in range(len(bones_list)):
            obs[len(obs)-1].data.edit_bones[bones_list[i][0]].name = bones_list[i][1]


        #Hierarquia
        bpy.context.object.data.edit_bones["Spine"].parent = bpy.context.object.data.edit_bones["Root"]
        bpy.context.object.data.edit_bones["Arm_L"].parent = bpy.context.object.data.edit_bones["Spine"]
        bpy.context.object.data.edit_bones["Arm_R"].parent = bpy.context.object.data.edit_bones["Spine"]
        bpy.context.object.data.edit_bones["Thigh_L"].parent = bpy.context.object.data.edit_bones["Root"]
        bpy.context.object.data.edit_bones["Thigh_R"].parent = bpy.context.object.data.edit_bones["Root"]

        bpy.ops.object.editmode_toggle()

    def distance(point1, point2) -> float: 
        #Calculate distance between two points in 3D.
        #return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2)
        return math.sqrt((point2.location[0] - point1.location[0]) ** 2 + (point2.location[1] - point1.location[1]) ** 2 + (point2.location[2] - point1.location[2]) ** 2)

    def size_bone(point_name1, point_name2, bone):
        p1 = bpy.data.objects[point_name1]
        p2 = bpy.data.objects[point_name2]
        #edit bones
        if bpy.context.active_object.mode == 'EDIT':
            bpy.context.object.data.edit_bones[bone].length= distance(p1,p2)
        else:
            bpy.ops.object.editmode_toggle()
            bpy.context.object.data.edit_bones[bone].length= distance(p1,p2)
        bpy.ops.object.editmode_toggle()

    def size_ref_bone(p1,p2,p_final):
        from mathutils import Vector
        import bpy

        ## size of the reference bone (spine)
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[p1].select_set(True)
        bpy.data.objects[p2].select_set(True)
        # bpy.context.view_layer.objects.active = bpy.data.objects['Point.034']
        bpy.context.view_layer.objects.active = bpy.data.objects[p2]
        obs = bpy.context.selected_objects
        n = len(obs)
        #    print('n: ',n)
        assert(n)
        #scene.cursor.location = sum([o.matrix_world.translation for o in obs], Vector()) / n
        #bpy.data.objects[p_middle].location = sum([o.matrix_world.translation for o in obs], Vector()) / n

        x_subtract = abs(obs[0].matrix_world.translation.x - obs[1].matrix_world.translation.x)
        y_subtract = abs(obs[0].matrix_world.translation.y - obs[1].matrix_world.translation.y)
        z_subtract = abs(obs[0].matrix_world.translation.z - obs[1].matrix_world.translation.z)

        max(x_subtract, y_subtract, z_subtract) #maior das medidas
        unit_def = max(x_subtract, y_subtract, z_subtract)/3
        #end of size of reference bone Spine
        return unit_def

    def size_of_bones(unit, root_size, spine_size, neck_size, face_size, thigh_size, leg_size, foot_size, arm_size, forearm_size):
        #==========================================
        #selecting and making the armature Active
        #selecionando armature
        #==========================================
        bpy.ops.object.select_all(action='DESELECT')
        #bpy.ops.armature.select_all(action='DESELECT')

        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        armature = obs[len(obs)-1].name

        #bpy.data.objects[armature].select_set(True)
        obs[len(obs)-1].select_set(True)
        view_layer = bpy.context.view_layer
        #Armature_obj = bpy.context.scene.objects[armature]
        Armature_obj = obs[len(obs)-1]
        view_layer.objects.active = Armature_obj

        #converting to euler rotation
        order = 'XYZ'
        context = bpy.context
        rig_object = context.active_object
        for pb in rig_object.pose.bones:
            pb.rotation_mode = order


        bpy.ops.object.editmode_toggle()

        #changing location
        #resetting
        bpy.context.object.data.edit_bones["Spine"].head.xy=0
        bpy.context.object.data.edit_bones["Neck"].head.xy=0
        bpy.context.object.data.edit_bones["Face"].head.xy=0

        bpy.context.object.data.edit_bones["Arm_L"].head.xy=0
        bpy.context.object.data.edit_bones["Forearm_L"].head.xy=0

        bpy.context.object.data.edit_bones["Arm_R"].head.xy=0
        bpy.context.object.data.edit_bones["Forearm_R"].head.xy=0

        bpy.context.object.data.edit_bones["Thigh_L"].head.xy=0
        bpy.context.object.data.edit_bones["Leg_L"].head.xy=0
        bpy.context.object.data.edit_bones["Foot_L"].head.xy=0

        bpy.context.object.data.edit_bones["Thigh_R"].head.xy=0
        bpy.context.object.data.edit_bones["Leg_R"].head.xy=0
        bpy.context.object.data.edit_bones["Foot_R"].head.xy=0
        #tail
        bpy.context.object.data.edit_bones["Face"].tail.xy=0
        bpy.context.object.data.edit_bones["Neck"].tail.xy=0
        bpy.context.object.data.edit_bones["Forearm_L"].tail.xy=0
        bpy.context.object.data.edit_bones["Forearm_R"].tail.xy=0
        bpy.context.object.data.edit_bones["Foot_L"].tail.xy=0
        bpy.context.object.data.edit_bones["Foot_R"].tail.xy=0




        bpy.context.object.data.edit_bones["Root"].length = root_size

        bpy.context.object.data.edit_bones["Spine"].head.z = unit/2
        bpy.context.object.data.edit_bones["Spine"].tail.z = spine_size

        bpy.context.object.data.edit_bones["Neck"].tail.z =  spine_size + neck_size
        bpy.context.object.data.edit_bones["Neck"].tail.y = neck_size/3
        bpy.context.object.data.edit_bones["Face"].tail.z = spine_size + neck_size
        bpy.context.object.data.edit_bones["Face"].tail.y = face_size*-1

        bpy.context.object.data.edit_bones["Arm_L"].head.z= spine_size
        bpy.context.object.data.edit_bones["Arm_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Forearm_L"].head.z=  spine_size
        bpy.context.object.data.edit_bones["Forearm_L"].head.x= unit + arm_size
        bpy.context.object.data.edit_bones["Forearm_L"].tail.z= spine_size
        bpy.context.object.data.edit_bones["Forearm_L"].tail.x= unit + arm_size + forearm_size

        bpy.context.object.data.edit_bones["Arm_R"].head.z= spine_size
        bpy.context.object.data.edit_bones["Arm_R"].head.x= (unit*3/4)*-1
        bpy.context.object.data.edit_bones["Forearm_R"].head.z= spine_size
        bpy.context.object.data.edit_bones["Forearm_R"].head.x= (unit + arm_size) *-1
        bpy.context.object.data.edit_bones["Forearm_R"].tail.z= spine_size
        bpy.context.object.data.edit_bones["Forearm_R"].tail.x= (unit + arm_size + forearm_size) *-1

        bpy.context.object.data.edit_bones["Thigh_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Thigh_L"].head.z= (unit/5)*-1
        bpy.context.object.data.edit_bones["Leg_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Leg_L"].head.z= (unit/5 + thigh_size)*-1
        bpy.context.object.data.edit_bones["Foot_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Foot_L"].head.z= (unit/5 + thigh_size + leg_size)*-1
        bpy.context.object.data.edit_bones["Foot_L"].tail.x= unit*3/4
        bpy.context.object.data.edit_bones["Foot_L"].tail.z= (unit/5 + thigh_size + leg_size + foot_size/2)*-1
        bpy.context.object.data.edit_bones["Foot_L"].tail.y= foot_size/2*-1

        bpy.context.object.data.edit_bones["Thigh_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Thigh_R"].head.z= (unit/5)*-1
        bpy.context.object.data.edit_bones["Leg_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Leg_R"].head.z= (unit/5 + thigh_size)*-1
        bpy.context.object.data.edit_bones["Foot_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Foot_R"].head.z= (unit/5 + thigh_size + leg_size)*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.z= (unit/5 + thigh_size + leg_size + foot_size/2)*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.y= foot_size/2*-1

        bpy.ops.object.editmode_toggle()

    def add_constraints(constraints, limit_rotation):
        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        bpy.ops.object.mode_set(mode='POSE')

        for i in range(len(constraints)):
            print('processar: ',constraints[i])
            if  constraints[i][1] == 'COPY_LOCATION' or constraints[i][1] == 'DAMPED_TRACK':
        #        print('in 1 j: ',j,' - name: ',constraints[i][0],' constraint: ',constraints[i][1])
                obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[constraints[i][0]].bone
                obs[len(obs)-1].pose.bones[constraints[i][0]].bone.select = True
                #
                bpy.ops.pose.constraint_add(type=constraints[i][1])
                qtd_constraint = len(bpy.context.object.pose.bones[constraints[i][0]].constraints)
                bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].target = bpy.data.objects[constraints[i][2]]
                if constraints[i][1] == 'DAMPED_TRACK' and len(constraints[i])==4:
                    bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].track_axis = constraints[i][3]
                #
            if constraints[i][1] == 'LIMIT_ROTATION' and limit_rotation == True :
                qtd_constraint = len(bpy.context.object.pose.bones[constraints[i][0]].constraints)
                if constraints[i][2] == 'LOCAL':
                    bpy.ops.pose.constraint_add(type=constraints[i][1])
                    qtd_constraint = len(bpy.context.object.pose.bones[constraints[i][0]].constraints)
                    bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].owner_space = constraints[i][2]
                if constraints[i][2] == 'X':
                    if constraints[i][3] == True:
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].use_limit_x = constraints[i][3]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].min_x  = constraints[i][4]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].max_x = constraints[i][5]
                if constraints[i][2] == 'Y':
                    if constraints[i][3] == True:
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].use_limit_y = constraints[i][3]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].min_y  = constraints[i][4]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].max_y = constraints[i][5]
                if constraints[i][2] == 'Z':
                    if constraints[i][3] == True:
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].use_limit_z = constraints[i][3]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].min_z  = constraints[i][4]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].max_z = constraints[i][5]

    def add_constraints_track_X(constraints,limit_rotation):
        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        bpy.ops.object.mode_set(mode='POSE')

        for i in range(len(constraints)):
            print('processar: ',constraints[i])
            if  constraints[i][1] == 'COPY_LOCATION' or constraints[i][1] == 'DAMPED_TRACK':
        #        print('in 1 j: ',j,' - name: ',constraints[i][0],' constraint: ',constraints[i][1])
                obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[constraints[i][0]].bone
                obs[len(obs)-1].pose.bones[constraints[i][0]].bone.select = True
                #
                bpy.ops.pose.constraint_add(type=constraints[i][1])
                qtd_constraint = len(bpy.context.object.pose.bones[constraints[i][0]].constraints)
                bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].target = bpy.data.objects[constraints[i][2]]
                if constraints[i][1] == 'DAMPED_TRACK' and len(constraints[i])>=4:
                    bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].track_axis = constraints[i][3]
                    bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].influence = constraints[i][4]
                #
            if constraints[i][1] == 'LIMIT_ROTATION' and limit_rotation == True:
                qtd_constraint = len(bpy.context.object.pose.bones[constraints[i][0]].constraints)
                if constraints[i][2] == 'LOCAL':
                    bpy.ops.pose.constraint_add(type=constraints[i][1])
                    qtd_constraint = len(bpy.context.object.pose.bones[constraints[i][0]].constraints)
                    bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].owner_space = constraints[i][2]
                if constraints[i][2] == 'X':
                    if constraints[i][3] == True:
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].use_limit_x = constraints[i][3]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].min_x  = constraints[i][4]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].max_x = constraints[i][5]
                if constraints[i][2] == 'Y':
                    if constraints[i][3] == True:
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].use_limit_y = constraints[i][3]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].min_y  = constraints[i][4]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].max_y = constraints[i][5]
                if constraints[i][2] == 'Z':
                    if constraints[i][3] == True:
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].use_limit_z = constraints[i][3]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].min_z  = constraints[i][4]
                        bpy.context.object.pose.bones[constraints[i][0]].constraints[qtd_constraint-1].max_z = constraints[i][5]



class OT_TestOpenFilebrowser(Operator, ImportHelper):

    bl_idname = "test.open_filebrowser"
    bl_label = "Open the file browser (yay)"


    def execute(self, context):
        
        filename, extension = os.path.splitext(self.filepath)
        
        print('real path', os.path.dirname(self.filepath))
        print('Selected file:', self.filepath)
        print('File name:', filename)
        print('File extension:', extension)
        # print('Some Boolean:', self.some_boolean)

        return {'FINISHED'}


class Import_Data_easymocap(Operator, ImportHelper):

    bl_idname = "mocap.import_easymocap"
    bl_label = "Import data"
    bl_description = "Import EasyMOCAP"


    filename_ext = ".json"

    filter_glob: StringProperty(
        default="*.json",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )




    def execute(self,context):

        

        #========================
        #EASYMOCAP
        #=====================

        import os
        import json
        import bpy
        from bpy import context
        import math 
        # bpy.ops.test.open_filebrowser('INVOKE_DEFAULT')#abrir janela de navegador

        object = []
        for ob in bpy.context.scene.objects:
                object.append(ob)

        if len(object) >0 :
            if bpy.context.mode != 'OBJECT':
                bpy.ops.object.editmode_toggle()

        #path = r'D:\MOCAP\EasyMocap-master\Teste_20210321_1_out\keypoints3d'
        path = os.path.dirname(self.filepath)
        list_dir = os.listdir(path)
        s_list = sorted(list_dir)

        data = []
        for i in s_list:
            with open(path+ os.sep +i,'r') as f: 
                data.append(json.load(f))
                #json.load(f)
                
        len(data)

        #-----------------
        x=0
        y=1
        z=2

        #armature = 'Armature'

        #=====================
        #trecho usado para rotacionar ao redor do cursor 
        def get_override(area_type, region_type):
            for area in bpy.context.screen.areas: 
                if area.type == area_type:             
                    for region in area.regions:                 
                        if region.type == region_type:                    
                            override = {'area': area, 'region': region} 
                            return override
            #error message if the area or region wasn't found
            raise RuntimeError("Wasn't able to find", region_type," in area ", area_type,
                                "\n Make sure it's open while executing script.")





        #===================================
        #creating bones
        #====================================

        # obs = []
        # for ob in bpy.context.scene.objects:
        #     # if ob.type == 'ARMATURE':
        #         obs.append(ob)
        # if len(obs)>0:
        #     if obs[len(obs)-1].mode != 'OBJECT':
        #         bpy.ops.object.editmode_toggle() #try to change to object mode
        #         if obs[len(obs)-1].mode != 'OBJECT':
        #             bpy.ops.object.editmode_toggle() #try again to change to object mode

        bpy.ops.object.armature_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1)) #cria armature e primeiro bone
        #bpy.ops.object.editmode_toggle()
        #bpy.data.armatures['Armature'].edit_bones.active = bpy.context.object.data.edit_bones['Bone']


        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        bpy.ops.armature.select_all(action='DESELECT')
        #bpy.context.object.data.edit_bones['Bone'].select_tail=True
        obs[len(obs)-1].data.edit_bones['Bone'].select_tail=True
        #bpy.ops.armature.extrude_move()#Neck
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.1, 0.1, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        #bpy.ops.armature.extrude_move()#Head_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.1, 0.1, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})


        bpy.ops.armature.select_all(action='DESELECT')
        bpy.context.object.data.edit_bones['Bone.001'].select_tail=True
        #bpy.ops.armature.extrude_move()#Head_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.1, 0.1, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})



        bpy.ops.armature.bone_primitive_add()#Forearm_L
        #bpy.ops.armature.extrude_move()#Arm_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.1, 0.1, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Forearm_R
        #bpy.ops.armature.extrude_move()#Arm_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.1, 0.1, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Thigh_L
        #bpy.ops.armature.extrude_move()#Leg_L
        #bpy.ops.armature.extrude_move()#Foot_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.1, 0.1, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.1, 0.1, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Thigh_R
        #bpy.ops.armature.extrude_move()#Leg_R
        #bpy.ops.armature.extrude_move()#Foot_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.1, 0.1, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.1, 0.1, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})


        #bpy.ops.object.editmode_toggle()
        #bpy.data.objects['Armature'].data.edit_bones['Arm_L'].name = 'Teste'

        #bpy.context.object.data.edit_bones["Bone"].name = 'Spline'
        #bpy.context.object.data.edit_bones["Bone.001"].name = 'Neck'
        #bpy.context.object.data.edit_bones["Bone.002"].name = 'Head_L'
        #bpy.context.object.data.edit_bones["Bone.003"].name = 'Head_R'
        #bpy.context.object.data.edit_bones["Bone.004"].name = 'Forearm_L'
        #bpy.context.object.data.edit_bones["Bone.005"].name = 'Arm_L'
        #bpy.context.object.data.edit_bones["Bone.006"].name = 'Forearm_R'
        #bpy.context.object.data.edit_bones["Bone.007"].name = 'Arm_R'
        #bpy.context.object.data.edit_bones["Bone.008"].name = 'Thigh_L'
        #bpy.context.object.data.edit_bones["Bone.009"].name = 'Leg_L'
        #bpy.context.object.data.edit_bones["Bone.010"].name = 'Foot_L'
        #bpy.context.object.data.edit_bones["Bone.011"].name = 'Thigh_R'
        #bpy.context.object.data.edit_bones["Bone.012"].name = 'Leg_R'
        #bpy.context.object.data.edit_bones["Bone.013"].name = 'Foot_R'



        obs[len(obs)-1].data.edit_bones["Bone"].name = 'Spline'
        obs[len(obs)-1].data.edit_bones["Bone.001"].name = 'Neck'
        obs[len(obs)-1].data.edit_bones["Bone.002"].name = 'Head_L'
        obs[len(obs)-1].data.edit_bones["Bone.003"].name = 'Head_R'
        obs[len(obs)-1].data.edit_bones["Bone.004"].name = 'Forearm_L'
        obs[len(obs)-1].data.edit_bones["Bone.005"].name = 'Arm_L'
        obs[len(obs)-1].data.edit_bones["Bone.006"].name = 'Forearm_R'
        obs[len(obs)-1].data.edit_bones["Bone.007"].name = 'Arm_R'
        obs[len(obs)-1].data.edit_bones["Bone.008"].name = 'Thigh_L'
        obs[len(obs)-1].data.edit_bones["Bone.009"].name = 'Leg_L'
        obs[len(obs)-1].data.edit_bones["Bone.010"].name = 'Foot_L'
        obs[len(obs)-1].data.edit_bones["Bone.011"].name = 'Thigh_R'
        obs[len(obs)-1].data.edit_bones["Bone.012"].name = 'Leg_R'
        obs[len(obs)-1].data.edit_bones["Bone.013"].name = 'Foot_R'

        bpy.ops.object.editmode_toggle()















        #remove Collection
        if bpy.data.collections.find("Points") >= 0:
            collection = bpy.data.collections.get('Points')
            #
            for obj in collection.objects:
                bpy.data.objects.remove(obj, do_unlink=True)
            bpy.data.collections.remove(collection)










        #cria os pontos nuima collection chamada Points
        #=====================================================
        collection = bpy.data.collections.new("Points")
        bpy.context.scene.collection.children.link(collection)

        layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
        bpy.context.view_layer.active_layer_collection = layer_collection

        for point in range(25):
            bpy.ops.mesh.primitive_plane_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
            bpy.ops.mesh.merge(type='CENTER')
            bpy.ops.object.editmode_toggle()
            context.active_object.name = 'Point.'+str(1000+point)[1:]
        #=====================================================





        #colocar cursor no tempo
        #bpy.context.scene.cursor.location = (0.0, 0.0, 0.0)
        #bpy.context.scene.tool_settings.transform_pivot_point = 'CURSOR'




        ## Deselect all objects
        #bpy.ops.object.select_all(action='DESELECT')

        #for o in bpy.data.objects:
        #    # Check for given object names
        #    if o.name in ("Point.000","Point.001","Point.002","Point.003","Point.004","Point.005","Point.006","Point.007","Point.008","Point.009" ,"Point.010" ,"Point.011","Point.012","Point.013","Point.014","Point.015","Point.016","Point.017","Point.018","Point.019","Point.020" ,"Point.021","Point.022","Point.023","Point.024"):
        #        o.select_set(True)

        for item in range(len(data)):
            print("frame: ",item)
            for limb in range(len(data[item][0]['keypoints3d'])):
                # print("limb: ",limb)
                bpy.data.objects["Point."+str(1000+limb)[1:]].location[x]=data[item][0]['keypoints3d'][limb][x]
                bpy.data.objects["Point."+str(1000+limb)[1:]].location[y]=data[item][0]['keypoints3d'][limb][y]
                bpy.data.objects["Point."+str(1000+limb)[1:]].location[z]=data[item][0]['keypoints3d'][limb][z]
                #
                
        #        #we need to override the context of our operator    
        #        override = get_override( 'VIEW_3D', 'WINDOW' )
        #        #rotate about the X-axis by 45 degrees
        #        bpy.ops.transform.rotate(override, value=6.283/2, orient_axis="Y") 
        #        
                #Salva Frame
                bpy.data.objects["Point."+str(1000+limb)[1:]].keyframe_insert(data_path="location", frame=item)






        #==========================================================================================================

        def distance(point1, point2) -> float: 
            #Calculate distance between two points in 3D.
        #    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2)
            return math.sqrt((point2.location[0] - point1.location[0]) ** 2 + (point2.location[1] - point1.location[1]) ** 2 + (point2.location[2] - point1.location[2]) ** 2)


        def size_bone(point_name1, point_name2, bone):
            p1 = bpy.data.objects[point_name1]
            p2 = bpy.data.objects[point_name2]
            #edit bones
            if bpy.context.active_object.mode == 'EDIT':
                bpy.context.object.data.edit_bones[bone].length= distance(p1,p2)
            else:
                bpy.ops.object.editmode_toggle()
                bpy.context.object.data.edit_bones[bone].length= distance(p1,p2)
            bpy.ops.object.editmode_toggle()

        #selecting and making the armature Active
        #selecionando armature

        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        armature = obs[len(obs)-1].name

        #bpy.data.objects[armature].select_set(True)
        obs[len(obs)-1].select_set(True)
        view_layer = bpy.context.view_layer
        #Armature_obj = bpy.context.scene.objects[armature]
        Armature_obj = obs[len(obs)-1]
        view_layer.objects.active = Armature_obj



        size_bone("Point.008", "Point.001", "Spline")
        size_bone("Point.001", "Point.000", "Neck")
        size_bone("Point.000", "Point.016", "Head_L")
        size_bone("Point.000", "Point.015", "Head_R")

        size_bone("Point.005", "Point.006", "Forearm_L")
        size_bone("Point.006", "Point.007", "Arm_L")

        size_bone("Point.002", "Point.003", "Forearm_R")
        size_bone("Point.003", "Point.004", "Arm_R")

        size_bone("Point.012", "Point.013", "Thigh_L")
        size_bone("Point.013", "Point.014", "Leg_L")
        size_bone("Point.014", "Point.019", "Foot_L")

        size_bone("Point.009", "Point.010", "Thigh_R")
        size_bone("Point.010", "Point.011", "Leg_R")
        size_bone("Point.011", "Point.022", "Foot_R")

        #comecando configuração  seguir movimentos pontos
        #colocando em pose mode
        bpy.ops.object.mode_set(mode='POSE')

        #bpy.data.objects[armature].pose.bones["Spine"]
        #bpy.data.objects[armature].pose.bones["Spine"].bone

        actual_bone = 'Spline'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True

        bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.008"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.001"]
        #=====
        actual_bone = 'Neck'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        #bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        #bpy.context.object.pose.bones[actual_bone].constraints["Copy Location"].target = bpy.data.objects["Point.001"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.000"]
        #=====
        actual_bone = 'Head_L'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        #bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        #bpy.context.object.pose.bones[actual_bone].constraints["Copy Location"].target = bpy.data.objects["Point.000"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.016"]
        #=====
        actual_bone = 'Head_R'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        #bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        #bpy.context.object.pose.bones[actual_bone].constraints["Copy Location"].target = bpy.data.objects["Point.000"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.015"]
        #=====


        actual_bone = 'Forearm_L'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.005"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.006"]
        #=====
        actual_bone = 'Arm_L'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        #bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        #bpy.context.object.pose.bones[actual_bone].constraints["Copy Location"].target = bpy.data.objects["Point.006"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.007"]
        #=====


        actual_bone = 'Forearm_R'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.002"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.003"]
        #=====
        actual_bone = 'Arm_R'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        #bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        #bpy.context.object.pose.bones[actual_bone].constraints["Copy Location"].target = bpy.data.objects["Point.003"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.004"]
        #=====




        actual_bone = 'Thigh_L'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.012"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.013"]
        #=====
        actual_bone = 'Leg_L'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        #bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        #bpy.context.object.pose.bones[actual_bone].constraints["Copy Location"].target = bpy.data.objects["Point.013"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.014"]
        #=====
        actual_bone = 'Foot_L'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        #bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        #bpy.context.object.pose.bones[actual_bone].constraints["Copy Location"].target = bpy.data.objects["Point.014"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.019"]
        #=====




        actual_bone = 'Thigh_R'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.009"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.010"]
        #=====
        actual_bone = 'Leg_R'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        #bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        #bpy.context.object.pose.bones[actual_bone].constraints["Copy Location"].target = bpy.data.objects["Point.010"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.011"]
        #=====
        actual_bone = 'Foot_R'
        bpy.context.object.data.bones.active = bpy.data.objects[armature].pose.bones[actual_bone].bone
        bpy.context.object.pose.bones[actual_bone].bone.select = True

        #bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        #bpy.context.object.pose.bones[actual_bone].constraints["Copy Location"].target = bpy.data.objects["Point.011"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.022"]
        #=====

        #bpy.data.objects['Armature'].pose.bones.items()
        #[('Bone', bpy.data.objects['Armature'].pose.bones["Bone"]), ('Thigh_L', bpy.data.objects['Armature'].pose.bones["Thigh_L"]), ('Leg_L', bpy.data.objects['Armature'].pose.bones["Leg_L"]), ('Foot_L', bpy.data.objects['Armature'].pose.bones["Foot_L"]), ('Spine', bpy.data.objects['Armature'].pose.bones["Spine"]), ('Neck', bpy.data.objects['Armature'].pose.bones["Neck"]), ('Head_L', bpy.data.objects['Armature'].pose.bones["Head_L"]), ('Head_R', bpy.data.objects['Armature'].pose.bones["Head_R"]), ('Forearm_L', bpy.data.objects['Armature'].pose.bones["Forearm_L"]), ('Arm_L', bpy.data.objects['Armature'].pose.bones["Arm_L"]), ('Thigh_R', bpy.data.objects['Armature'].pose.bones["Thigh_R"]), ('Leg_R', bpy.data.objects['Armature'].pose.bones["Leg_R"]), ('Foot_R', bpy.data.objects['Armature'].pose.bones["Foot_R"]), ('Forearm_R', bpy.data.objects['Armature'].pose.bones["Forearm_R"]), ('Arm_R', bpy.data.objects['Armature'].pose.bones["Arm_R"])]

        print(len(data))
        bpy.context.scene.frame_end = len(data)

        bpy.ops.nla.bake(frame_start=1, frame_end=len(data), visual_keying=True, clear_constraints=True, clear_parents=True, bake_types={'POSE'})
        bpy.ops.object.mode_set(mode='OBJECT')




        #apagar collection points criada
        collection = bpy.data.collections.get('Points')
        #
        for obj in collection.objects:
            bpy.data.objects.remove(obj, do_unlink=True)
        bpy.data.collections.remove(collection)


        return{'FINISHED'}


class Import_Data_frankmocap(Operator, ImportHelper):
    bl_idname = "mocap.import_frankmocap"
    bl_label = "Import data from Frankmocap"
    bl_description = "Import FrankMocap"


    filename_ext = ".pkl"

    filter_glob: StringProperty(
        default="*.pkl",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )




    def execute(self,context):

        #"""
        #Frnakmocap
        #==========================
        
        import math
        import bpy
        import os
        import pickle
        import numpy as np
        from bpy import context
        import joblib

        multiplier = context.scene.sk_value_prop.sk_value
        raw_bool = context.scene.sk_value_prop.sk_raw_bool

        def middle_point(p1,p2,p_middle):
            bpy.ops.object.select_all(action='DESELECT')
            bpy.data.objects[p1].select_set(True)
            bpy.data.objects[p2].select_set(True)
            bpy.context.view_layer.objects.active = bpy.data.objects[p2]
            obs = bpy.context.selected_objects
            n = len(obs)
        #    print('n: ',n)
            assert(n)
            #scene.cursor.location = sum([o.matrix_world.translation for o in obs], Vector()) / n
            bpy.data.objects[p_middle].location = sum([o.matrix_world.translation for o in obs], Vector()) / n


        def create_dots(name, amount):
            #remove Collection
            if bpy.data.collections.find(name) >= 0:
                collection = bpy.data.collections.get(name)
                #
                for obj in collection.objects:
                    bpy.data.objects.remove(obj, do_unlink=True)
                bpy.data.collections.remove(collection)
            #cria os pontos nuima collection chamada Points
            #=====================================================
            collection = bpy.data.collections.new(name)
            bpy.context.scene.collection.children.link(collection)
        #
            layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
            bpy.context.view_layer.active_layer_collection = layer_collection
        #
            for point in range(amount):
                bpy.ops.mesh.primitive_plane_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
                bpy.ops.mesh.merge(type='CENTER')
                bpy.ops.object.editmode_toggle()
                bpy.context.active_object.name = name+'.'+str(1000+point)[1:]
            #=====================================================

        #==============================
        #codes to size the bones
        #==============================

        def distance(point1, point2) -> float:
            #Calculate distance between two points in 3D.
        #    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2)
            return math.sqrt((point2.location[0] - point1.location[0]) ** 2 + (point2.location[1] - point1.location[1]) ** 2 + (point2.location[2] - point1.location[2]) ** 2)


        def size_bone(point_name1, point_name2, bone):
            p1 = bpy.data.objects[point_name1]
            p2 = bpy.data.objects[point_name2]
            #edit bones
            if bpy.context.active_object.mode == 'EDIT':
                bpy.context.object.data.edit_bones[bone].length= distance(p1,p2)
            else:
                bpy.ops.object.editmode_toggle()
                bpy.context.object.data.edit_bones[bone].length= distance(p1,p2)
            bpy.ops.object.editmode_toggle()



        create_dots('Point',49)


        # pkl_path=r'C:\MOCAP\frankmocap\mocap_output\mocap\temp'
        pkl_path = os.path.dirname(self.filepath)
        list_dir = os.listdir(pkl_path)
        s_list = sorted(list_dir)

        len(s_list)

        x=0
        y=1
        z=2
        multi=100
        #armature = 'Armature'


        #exemplo
        file = open(pkl_path+ os.sep +s_list[0],'rb')

        pic = pickle.load(file)
        file.close()

        nppic = np.load(pkl_path+ os.sep +s_list[0], allow_pickle=True)

        for item in range(len(s_list)-1):
            nppic = np.load(pkl_path+ os.sep +s_list[item], allow_pickle=True)
        #    nppic['pred_output_list'][0]['pred_body_joints_img'] #todos os limbs
            print("frame: ",item)
            for limb in range(len(nppic['pred_output_list'][0]['pred_body_joints_img'])):
        #        print("limb: ",limb)
                bpy.data.objects["Point."+str(1000+limb)[1:]].location[z]=nppic['pred_output_list'][0]['pred_body_joints_img'][limb][x]/multi
                bpy.data.objects["Point."+str(1000+limb)[1:]].location[y]=nppic['pred_output_list'][0]['pred_body_joints_img'][limb][y]/multi
                bpy.data.objects["Point."+str(1000+limb)[1:]].location[x]=nppic['pred_output_list'][0]['pred_body_joints_img'][limb][z]/multi
                bpy.data.objects["Point."+str(1000+limb)[1:]].keyframe_insert(data_path="location", frame=item)


        len(nppic['pred_output_list'][0]['pred_body_joints_img'])



        import bpy


        #===========
        # selectign Scene Collection
        scene_collection = bpy.context.view_layer.layer_collection
        bpy.context.view_layer.active_layer_collection = scene_collection


        #===================================
        #creating bones
        #====================================

        bpy.ops.object.armature_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1)) #cria armature e primeiro bone
        #bpy.ops.object.editmode_toggle()
        #bpy.data.armatures['Armature'].edit_bones.active = bpy.context.object.data.edit_bones['Bone']


        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs


        bpy.ops.armature.select_all(action='DESELECT')
        #bpy.context.object.data.edit_bones['Bone'].select_tail=True
        obs[len(obs)-1].data.edit_bones['Bone'].select_tail=True

        bpy.ops.armature.bone_primitive_add()#Spine
        #bpy.ops.armature.extrude_move()#Neck
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        ##bpy.ops.armature.extrude_move()#Face
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})


        bpy.ops.armature.bone_primitive_add()#Arm_L
        #bpy.ops.armature.extrude_move()#Forearm_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Arm_R
        #bpy.ops.armature.extrude_move()#Forearm_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Thigh_L
        #bpy.ops.armature.extrude_move()#Leg_L
        #bpy.ops.armature.extrude_move()#Foot_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Thigh_R
        #bpy.ops.armature.extrude_move()#Leg_R
        #bpy.ops.armature.extrude_move()#Foot_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})


        obs[len(obs)-1].data.edit_bones["Bone"].name = 'Root'
        obs[len(obs)-1].data.edit_bones["Bone.001"].name = 'Spine'
        obs[len(obs)-1].data.edit_bones["Bone.002"].name = 'Neck'
        obs[len(obs)-1].data.edit_bones["Bone.003"].name = 'Face'
        obs[len(obs)-1].data.edit_bones["Bone.004"].name = 'Arm_L'
        obs[len(obs)-1].data.edit_bones["Bone.005"].name = 'Forearm_L'
        obs[len(obs)-1].data.edit_bones["Bone.006"].name = 'Arm_R'
        obs[len(obs)-1].data.edit_bones["Bone.007"].name = 'Forearm_R'
        obs[len(obs)-1].data.edit_bones["Bone.008"].name = 'Thigh_L'
        obs[len(obs)-1].data.edit_bones["Bone.009"].name = 'Leg_L'
        obs[len(obs)-1].data.edit_bones["Bone.010"].name = 'Foot_L'
        obs[len(obs)-1].data.edit_bones["Bone.011"].name = 'Thigh_R'
        obs[len(obs)-1].data.edit_bones["Bone.012"].name = 'Leg_R'
        obs[len(obs)-1].data.edit_bones["Bone.013"].name = 'Foot_R'


        #Hierarquia
        bpy.context.object.data.edit_bones["Spine"].parent = bpy.context.object.data.edit_bones["Root"]
        bpy.context.object.data.edit_bones["Arm_L"].parent = bpy.context.object.data.edit_bones["Spine"]
        bpy.context.object.data.edit_bones["Arm_R"].parent = bpy.context.object.data.edit_bones["Spine"]
        bpy.context.object.data.edit_bones["Thigh_L"].parent = bpy.context.object.data.edit_bones["Root"]
        bpy.context.object.data.edit_bones["Thigh_R"].parent = bpy.context.object.data.edit_bones["Root"]

        bpy.ops.object.editmode_toggle()



        from mathutils import Vector
        import bpy

        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects['Point.001'].select_set(True)
        bpy.data.objects['Point.008'].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects['Point.034']
        obs = bpy.context.selected_objects
        n = len(obs)
        #    print('n: ',n)
        assert(n)
        #scene.cursor.location = sum([o.matrix_world.translation for o in obs], Vector()) / n
        #bpy.data.objects[p_middle].location = sum([o.matrix_world.translation for o in obs], Vector()) / n



        x_subtract = abs(obs[0].matrix_world.translation.x - obs[1].matrix_world.translation.x)
        y_subtract = abs(obs[0].matrix_world.translation.y - obs[1].matrix_world.translation.y)
        z_subtract = abs(obs[0].matrix_world.translation.z - obs[1].matrix_world.translation.z)

        max(x_subtract, y_subtract, z_subtract) #maior das medidas
        unit = max(x_subtract, y_subtract, z_subtract)/3
        unit = unit*multiplier

        root_sz    =unit/10
        spine_sz   =unit*3.5
        neck_sz    =unit
        face_sz    =unit
        thigh_sz    =unit*3
        leg_sz     =unit*2.5
        foot_sz    =unit #inclinado 45 graud pra frente
        arm_sz     =unit*1.5
        forearm_sz =unit*1.5



        #if bpy.context.active_object.mode != 'EDIT':
        #    bpy.ops.object.editmode_toggle()
        #==========================================
        #selecting and making the armature Active
        #selecionando armature
        #==========================================
        bpy.ops.object.select_all(action='DESELECT')
        #bpy.ops.armature.select_all(action='DESELECT')

        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        armature = obs[len(obs)-1].name

        #bpy.data.objects[armature].select_set(True)
        obs[len(obs)-1].select_set(True)
        view_layer = bpy.context.view_layer
        #Armature_obj = bpy.context.scene.objects[armature]
        Armature_obj = obs[len(obs)-1]
        view_layer.objects.active = Armature_obj


        #converting to euler rotation
        order = 'XYZ'
        context = bpy.context
        rig_object = context.active_object
        for pb in rig_object.pose.bones:
            pb.rotation_mode = order



        bpy.ops.object.editmode_toggle()

        #changing location
        #resetting
        bpy.context.object.data.edit_bones["Spine"].head.xy=0
        bpy.context.object.data.edit_bones["Neck"].head.xy=0
        bpy.context.object.data.edit_bones["Face"].head.xy=0

        bpy.context.object.data.edit_bones["Arm_L"].head.xy=0
        bpy.context.object.data.edit_bones["Forearm_L"].head.xy=0

        bpy.context.object.data.edit_bones["Arm_R"].head.xy=0
        bpy.context.object.data.edit_bones["Forearm_R"].head.xy=0

        bpy.context.object.data.edit_bones["Thigh_L"].head.xy=0
        bpy.context.object.data.edit_bones["Leg_L"].head.xy=0
        bpy.context.object.data.edit_bones["Foot_L"].head.xy=0

        bpy.context.object.data.edit_bones["Thigh_R"].head.xy=0
        bpy.context.object.data.edit_bones["Leg_R"].head.xy=0
        bpy.context.object.data.edit_bones["Foot_R"].head.xy=0
        #tail
        bpy.context.object.data.edit_bones["Face"].tail.xy=0
        bpy.context.object.data.edit_bones["Neck"].tail.xy=0
        bpy.context.object.data.edit_bones["Forearm_L"].tail.xy=0
        bpy.context.object.data.edit_bones["Forearm_R"].tail.xy=0
        bpy.context.object.data.edit_bones["Foot_L"].tail.xy=0
        bpy.context.object.data.edit_bones["Foot_R"].tail.xy=0




        bpy.context.object.data.edit_bones["Root"].length = root_sz

        bpy.context.object.data.edit_bones["Spine"].head.z = unit/2
        bpy.context.object.data.edit_bones["Spine"].tail.z = spine_sz

        bpy.context.object.data.edit_bones["Neck"].tail.z =  spine_sz + neck_sz
        bpy.context.object.data.edit_bones["Neck"].tail.y = neck_sz/3
        bpy.context.object.data.edit_bones["Face"].tail.z = spine_sz + neck_sz
        bpy.context.object.data.edit_bones["Face"].tail.y = face_sz*-1

        bpy.context.object.data.edit_bones["Arm_L"].head.z= spine_sz
        bpy.context.object.data.edit_bones["Arm_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Forearm_L"].head.z=  spine_sz
        bpy.context.object.data.edit_bones["Forearm_L"].head.x= unit + arm_sz
        bpy.context.object.data.edit_bones["Forearm_L"].tail.z= spine_sz
        bpy.context.object.data.edit_bones["Forearm_L"].tail.x= unit + arm_sz + forearm_sz

        bpy.context.object.data.edit_bones["Arm_R"].head.z= spine_sz
        bpy.context.object.data.edit_bones["Arm_R"].head.x= (unit*3/4)*-1
        bpy.context.object.data.edit_bones["Forearm_R"].head.z= spine_sz
        bpy.context.object.data.edit_bones["Forearm_R"].head.x= (unit + arm_sz) *-1
        bpy.context.object.data.edit_bones["Forearm_R"].tail.z= spine_sz
        bpy.context.object.data.edit_bones["Forearm_R"].tail.x= (unit + arm_sz + forearm_sz) *-1

        bpy.context.object.data.edit_bones["Thigh_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Thigh_L"].head.z= (unit/5)*-1
        bpy.context.object.data.edit_bones["Leg_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Leg_L"].head.z= (unit/5 + thigh_sz)*-1
        bpy.context.object.data.edit_bones["Foot_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Foot_L"].head.z= (unit/5 + thigh_sz + leg_sz)*-1
        bpy.context.object.data.edit_bones["Foot_L"].tail.x= unit*3/4
        bpy.context.object.data.edit_bones["Foot_L"].tail.z= (unit/5 + thigh_sz + leg_sz + foot_sz/2)*-1
        bpy.context.object.data.edit_bones["Foot_L"].tail.y= foot_sz/2*-1

        bpy.context.object.data.edit_bones["Thigh_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Thigh_R"].head.z= (unit/5)*-1
        bpy.context.object.data.edit_bones["Leg_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Leg_R"].head.z= (unit/5 + thigh_sz)*-1
        bpy.context.object.data.edit_bones["Foot_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Foot_R"].head.z= (unit/5 + thigh_sz + leg_sz)*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.z= (unit/5 + thigh_sz + leg_sz + foot_sz/2)*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.y= foot_sz/2*-1

        bpy.ops.object.editmode_toggle()



        import bpy

        #comecando configuração  seguir movimentos pontos
        #colocando em pose mode


        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        bpy.ops.object.mode_set(mode='POSE')


        actual_bone = 'Root'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.008"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.039"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.001"]
        bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.037"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.001"]
        bpy.context.object.pose.bones[actual_bone].constraints[2].target = bpy.data.objects["Point.027"]
        bpy.context.object.pose.bones[actual_bone].constraints[2].track_axis = 'TRACK_X'


        #====
        actual_bone = 'Spine'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.001"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.037"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x  = -0.349066
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.349066
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = -0.698132
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0.698132
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.174533

        #=====
        actual_bone = 'Neck'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.000"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.042"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 1.0472
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0.523599
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.349066
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.349066
        #=====
        actual_bone = 'Face'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.044"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.872665
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.523599
        #=====
        actual_bone = 'Arm_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.006"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.032"]
        #=====
        actual_bone = 'Forearm_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.007"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.031"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -2.53073
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = -0.191986
        #=====
        actual_bone = 'Arm_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.003"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.035"]
        #=====
        actual_bone = 'Forearm_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.004"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.036"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = False
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = False
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0.191986
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 2.53073
        #=====
        actual_bone = 'Thigh_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.013"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.026"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -1.76278
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 1.3439
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.785398
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.174533
        #=====
        actual_bone = 'Leg_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.014"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.025"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = 0.0698132
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 2.0944
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0
        #=====
        actual_bone = 'Foot_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.019"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.022"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.523599
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0
        #=====
        actual_bone = 'Thigh_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.010"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.029"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -1.76278
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 1.3439
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.785398

        actual_bone = 'Leg_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.011"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.030"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = 0.0698132
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 2.0944
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0

        actual_bone = 'Foot_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.022"]
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.019"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.523599
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0

        print(len(s_list))
        bpy.context.scene.frame_end = len(s_list)

        bpy.ops.nla.bake(frame_start=1, frame_end=len(s_list), visual_keying=True, clear_constraints=True, clear_parents=True, bake_types={'POSE'})
        bpy.ops.object.mode_set(mode='OBJECT')



        #apagar collection points criada
        collection = bpy.data.collections.get('Point')
        #
        for obj in collection.objects:
            bpy.data.objects.remove(obj, do_unlink=True)
        bpy.data.collections.remove(collection)


        sk_value_prop = context.scene.sk_value_prop
        if raw_bool == True:
            print('raw_bool True - ',raw_bool)

            x_original, y_original, z_original = helper_functions.get_rotations()
            sk_value_prop.sk_root_rot_x = math.degrees(x_original)
            sk_value_prop.sk_root_rot_y = math.degrees(y_original)
            sk_value_prop.sk_root_rot_z = math.degrees(z_original)

            #in this case both original and actual is the same, because there was no alteration on the angle
            x_actual_deg = math.degrees(x_original)
            y_actual_deg = math.degrees(y_original)
            z_actual_deg = math.degrees(z_original)

            sk_value_prop.sk_root_actual_rot_x = x_actual_deg
            sk_value_prop.sk_root_actual_rot_y = y_actual_deg
            sk_value_prop.sk_root_actual_rot_z = z_actual_deg
        else:
            print('raw_bool False - ',raw_bool)
            x_deg, y_deg, z_deg = helper_functions.anim_to_origin()
            #take the information of the rotation to the panel
            print('result x: ',x_deg)
            print('result y: ',y_deg)
            print('result z: ',z_deg)
            sk_value_prop.sk_root_rot_x = x_deg
            sk_value_prop.sk_root_rot_y = y_deg
            sk_value_prop.sk_root_rot_z = z_deg


        #"""
        return{'FINISHED'}
        #"""


class Import_Data_vibe(Operator, ImportHelper):
    bl_idname = "mocap.import_vibe"
    bl_label = "Import data from Vibe (needs joblib install)"
    bl_description = "Import Vibe"


    filename_ext = ".pkl"

    filter_glob: StringProperty(
        default="*.pkl",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    def execute(self,context):



        #==========================
        #======VIBE

        #instalar joblib
        #D:\Blender\blender-2.92.0-windows64\2.92\python\bin\python.exe D:\Blender\blender-2.92.0-windows64\2.92\python\lib\site-packages\pip install joblib
        
   
        import math
        import bpy
        import os
        import pickle
        import numpy as np
        from bpy import context
        import joblib

        multiplier = context.scene.sk_value_prop.sk_value
        raw_bool = context.scene.sk_value_prop.sk_raw_bool

        def middle_point(p1,p2,p_middle):
            bpy.ops.object.select_all(action='DESELECT')
            bpy.data.objects[p1].select_set(True)
            bpy.data.objects[p2].select_set(True)
            bpy.context.view_layer.objects.active = bpy.data.objects[p2]
            obs = bpy.context.selected_objects
            n = len(obs)
        #    print('n: ',n)
            assert(n)
            #scene.cursor.location = sum([o.matrix_world.translation for o in obs], Vector()) / n
            bpy.data.objects[p_middle].location = sum([o.matrix_world.translation for o in obs], Vector()) / n


        def create_dots(name, amount):
            #remove Collection
            if bpy.data.collections.find(name) >= 0:
                collection = bpy.data.collections.get(name)
                #
                for obj in collection.objects:
                    bpy.data.objects.remove(obj, do_unlink=True)
                bpy.data.collections.remove(collection)
            #cria os pontos nuima collection chamada Points
            #=====================================================
            collection = bpy.data.collections.new(name)
            bpy.context.scene.collection.children.link(collection)
        #
            layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
            bpy.context.view_layer.active_layer_collection = layer_collection
        #
            for point in range(amount):
                bpy.ops.mesh.primitive_plane_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
                bpy.ops.mesh.merge(type='CENTER')
                bpy.ops.object.editmode_toggle()
                bpy.context.active_object.name = name+'.'+str(1000+point)[1:]
            #=====================================================
            
        #==============================
        #codes to size the bones
        #==============================

        def distance(point1, point2) -> float: 
            #Calculate distance between two points in 3D.
        #    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2)
            return math.sqrt((point2.location[0] - point1.location[0]) ** 2 + (point2.location[1] - point1.location[1]) ** 2 + (point2.location[2] - point1.location[2]) ** 2)


        def size_bone(point_name1, point_name2, bone):
            p1 = bpy.data.objects[point_name1]
            p2 = bpy.data.objects[point_name2]
            #edit bones
            if bpy.context.active_object.mode == 'EDIT':
                bpy.context.object.data.edit_bones[bone].length= distance(p1,p2)
            else:
                bpy.ops.object.editmode_toggle()
                bpy.context.object.data.edit_bones[bone].length= distance(p1,p2)
            bpy.ops.object.editmode_toggle()




        #path = r'D:\MOCAP\EasyMocap-master\demo_test\videos\1.mp4'
        #path = r'D:\Video_editing\running e brack dance para mocap.mp4'
        create_dots('Point',49)



        # pkl_path=r'D:\MOCAP\VIBE\output\sample_video\vibe_output.pkl'
        pkl_path=self.filepath
        pic = joblib.load(pkl_path)

        x=0
        y=1
        z=2


        person_id=1

        for item in range(len(pic[person_id]['pose'])):
            print("frame: ",item)
            final_limbs = int(len(pic[person_id]['pose'][item])/3)
            for limb in range(final_limbs):
                # print("limb: ",limb)
                bpy.data.objects["Point."+str(1000+limb)[1:]].location[x]=pic[person_id]['joints3d'][item][limb][x]
                bpy.data.objects["Point."+str(1000+limb)[1:]].location[y]=pic[person_id]['joints3d'][item][limb][y]
                bpy.data.objects["Point."+str(1000+limb)[1:]].location[z]=pic[person_id]['joints3d'][item][limb][z]
                bpy.data.objects["Point."+str(1000+limb)[1:]].keyframe_insert(data_path="location", frame=item)



        import bpy


        #===========
        # selectign Scene Collection
        scene_collection = bpy.context.view_layer.layer_collection
        bpy.context.view_layer.active_layer_collection = scene_collection


        #===================================
        #creating bones
        #====================================

        bpy.ops.object.armature_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1)) #cria armature e primeiro bone
        #bpy.ops.object.editmode_toggle()
        #bpy.data.armatures['Armature'].edit_bones.active = bpy.context.object.data.edit_bones['Bone']


        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs


        bpy.ops.armature.select_all(action='DESELECT')
        #bpy.context.object.data.edit_bones['Bone'].select_tail=True
        obs[len(obs)-1].data.edit_bones['Bone'].select_tail=True

        bpy.ops.armature.bone_primitive_add()#Spine
        #bpy.ops.armature.extrude_move()#Neck
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        ##bpy.ops.armature.extrude_move()#Face
        #bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})


        bpy.ops.armature.bone_primitive_add()#Arm_L
        #bpy.ops.armature.extrude_move()#Forearm_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Arm_R
        #bpy.ops.armature.extrude_move()#Forearm_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Thigh_L
        #bpy.ops.armature.extrude_move()#Leg_L
        #bpy.ops.armature.extrude_move()#Foot_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Thigh_R
        #bpy.ops.armature.extrude_move()#Leg_R
        #bpy.ops.armature.extrude_move()#Foot_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})


        obs[len(obs)-1].data.edit_bones["Bone"].name = 'Root'
        obs[len(obs)-1].data.edit_bones["Bone.001"].name = 'Spine'
        obs[len(obs)-1].data.edit_bones["Bone.002"].name = 'Neck'
        #obs[len(obs)-1].data.edit_bones["Bone.003"].name = 'Face'
        obs[len(obs)-1].data.edit_bones["Bone.003"].name = 'Arm_L'
        obs[len(obs)-1].data.edit_bones["Bone.004"].name = 'Forearm_L'
        obs[len(obs)-1].data.edit_bones["Bone.005"].name = 'Arm_R'
        obs[len(obs)-1].data.edit_bones["Bone.006"].name = 'Forearm_R'
        obs[len(obs)-1].data.edit_bones["Bone.007"].name = 'Thigh_L'
        obs[len(obs)-1].data.edit_bones["Bone.008"].name = 'Leg_L'
        obs[len(obs)-1].data.edit_bones["Bone.009"].name = 'Foot_L'
        obs[len(obs)-1].data.edit_bones["Bone.010"].name = 'Thigh_R'
        obs[len(obs)-1].data.edit_bones["Bone.011"].name = 'Leg_R'
        obs[len(obs)-1].data.edit_bones["Bone.012"].name = 'Foot_R'


        #Hierarquia
        bpy.context.object.data.edit_bones["Spine"].parent = bpy.context.object.data.edit_bones["Root"]
        bpy.context.object.data.edit_bones["Arm_L"].parent = bpy.context.object.data.edit_bones["Spine"]
        bpy.context.object.data.edit_bones["Arm_R"].parent = bpy.context.object.data.edit_bones["Spine"]
        bpy.context.object.data.edit_bones["Thigh_L"].parent = bpy.context.object.data.edit_bones["Root"]
        bpy.context.object.data.edit_bones["Thigh_R"].parent = bpy.context.object.data.edit_bones["Root"]

        bpy.ops.object.editmode_toggle()




        from mathutils import Vector
        import bpy

        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects['Point.001'].select_set(True)
        bpy.data.objects['Point.008'].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects['Point.034']
        obs = bpy.context.selected_objects
        n = len(obs)
        #    print('n: ',n)
        assert(n)
        #scene.cursor.location = sum([o.matrix_world.translation for o in obs], Vector()) / n
        #bpy.data.objects[p_middle].location = sum([o.matrix_world.translation for o in obs], Vector()) / n



        x_subtract = abs(obs[0].matrix_world.translation.x - obs[1].matrix_world.translation.x)
        y_subtract = abs(obs[0].matrix_world.translation.y - obs[1].matrix_world.translation.y)
        z_subtract = abs(obs[0].matrix_world.translation.z - obs[1].matrix_world.translation.z)

        max(x_subtract, y_subtract, z_subtract) #maior das medidas
        unit = max(x_subtract, y_subtract, z_subtract)/3
        unit = unit*multiplier

        root_sz    =unit/10
        spine_sz   =unit*3.5
        neck_sz    =unit
        face_sz    =unit
        thigh_sz    =unit*3
        leg_sz     =unit*2.5
        foot_sz    =unit #inclinado 45 graud pra frente
        arm_sz     =unit*1.5
        forearm_sz =unit*1.5



        #if bpy.context.active_object.mode != 'EDIT':
        #    bpy.ops.object.editmode_toggle()
        #==========================================
        #selecting and making the armature Active
        #selecionando armature
        #==========================================
        bpy.ops.object.select_all(action='DESELECT')
        #bpy.ops.armature.select_all(action='DESELECT')

        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        armature = obs[len(obs)-1].name

        #bpy.data.objects[armature].select_set(True)
        obs[len(obs)-1].select_set(True)
        view_layer = bpy.context.view_layer
        #Armature_obj = bpy.context.scene.objects[armature]
        Armature_obj = obs[len(obs)-1]
        view_layer.objects.active = Armature_obj

        #converting to euler rotation
        order = 'XYZ'
        context = bpy.context
        rig_object = context.active_object
        for pb in rig_object.pose.bones:
            pb.rotation_mode = order


        bpy.ops.object.editmode_toggle()

        #changing location
        #resetting
        bpy.context.object.data.edit_bones["Spine"].head.xy=0
        bpy.context.object.data.edit_bones["Neck"].head.xy=0
        #bpy.context.object.data.edit_bones["Face"].head.xy=0

        bpy.context.object.data.edit_bones["Arm_L"].head.xy=0
        bpy.context.object.data.edit_bones["Forearm_L"].head.xy=0

        bpy.context.object.data.edit_bones["Arm_R"].head.xy=0
        bpy.context.object.data.edit_bones["Forearm_R"].head.xy=0

        bpy.context.object.data.edit_bones["Thigh_L"].head.xy=0
        bpy.context.object.data.edit_bones["Leg_L"].head.xy=0
        bpy.context.object.data.edit_bones["Foot_L"].head.xy=0

        bpy.context.object.data.edit_bones["Thigh_R"].head.xy=0
        bpy.context.object.data.edit_bones["Leg_R"].head.xy=0
        bpy.context.object.data.edit_bones["Foot_R"].head.xy=0
        #tail
        #bpy.context.object.data.edit_bones["Face"].tail.xy=0
        bpy.context.object.data.edit_bones["Neck"].tail.xy=0
        bpy.context.object.data.edit_bones["Forearm_L"].tail.xy=0
        bpy.context.object.data.edit_bones["Forearm_R"].tail.xy=0
        bpy.context.object.data.edit_bones["Foot_L"].tail.xy=0
        bpy.context.object.data.edit_bones["Foot_R"].tail.xy=0




        bpy.context.object.data.edit_bones["Root"].length = root_sz

        bpy.context.object.data.edit_bones["Spine"].head.z = unit/2
        bpy.context.object.data.edit_bones["Spine"].tail.z = spine_sz

        bpy.context.object.data.edit_bones["Neck"].tail.z =  spine_sz + neck_sz
        bpy.context.object.data.edit_bones["Neck"].tail.y = neck_sz/3
        #bpy.context.object.data.edit_bones["Face"].tail.z = spine_sz + neck_sz
        #bpy.context.object.data.edit_bones["Face"].tail.y = face_sz*-1

        bpy.context.object.data.edit_bones["Arm_L"].head.z= spine_sz
        bpy.context.object.data.edit_bones["Arm_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Forearm_L"].head.z=  spine_sz
        bpy.context.object.data.edit_bones["Forearm_L"].head.x= unit + arm_sz
        bpy.context.object.data.edit_bones["Forearm_L"].tail.z= spine_sz
        bpy.context.object.data.edit_bones["Forearm_L"].tail.x= unit + arm_sz + forearm_sz

        bpy.context.object.data.edit_bones["Arm_R"].head.z= spine_sz
        bpy.context.object.data.edit_bones["Arm_R"].head.x= (unit*3/4)*-1
        bpy.context.object.data.edit_bones["Forearm_R"].head.z= spine_sz
        bpy.context.object.data.edit_bones["Forearm_R"].head.x= (unit + arm_sz) *-1
        bpy.context.object.data.edit_bones["Forearm_R"].tail.z= spine_sz
        bpy.context.object.data.edit_bones["Forearm_R"].tail.x= (unit + arm_sz + forearm_sz) *-1

        bpy.context.object.data.edit_bones["Thigh_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Thigh_L"].head.z= (unit/5)*-1
        bpy.context.object.data.edit_bones["Leg_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Leg_L"].head.z= (unit/5 + thigh_sz)*-1
        bpy.context.object.data.edit_bones["Foot_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Foot_L"].head.z= (unit/5 + thigh_sz + leg_sz)*-1
        bpy.context.object.data.edit_bones["Foot_L"].tail.x= unit*3/4
        bpy.context.object.data.edit_bones["Foot_L"].tail.z= (unit/5 + thigh_sz + leg_sz + foot_sz/2)*-1
        bpy.context.object.data.edit_bones["Foot_L"].tail.y= foot_sz/2*-1

        bpy.context.object.data.edit_bones["Thigh_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Thigh_R"].head.z= (unit/5)*-1
        bpy.context.object.data.edit_bones["Leg_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Leg_R"].head.z= (unit/5 + thigh_sz)*-1
        bpy.context.object.data.edit_bones["Foot_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Foot_R"].head.z= (unit/5 + thigh_sz + leg_sz)*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.z= (unit/5 + thigh_sz + leg_sz + foot_sz/2)*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.y= foot_sz/2*-1

        bpy.ops.object.editmode_toggle()




        import bpy

        #comecando configuração  seguir movimentos pontos
        #colocando em pose mode


        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        bpy.ops.object.mode_set(mode='POSE')


        actual_bone = 'Root'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.008"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.001"]

        #====
        actual_bone = 'Spine'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.001"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x  = -0.349066
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.349066
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = -0.698132
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0.698132
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.174533

        #=====
        actual_bone = 'Neck'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.000"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 1.0472
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0.523599
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.349066
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.349066
        #=====
        #actual_bone = 'Face'
        #obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        #obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        #bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        #bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.000"]
        #bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        #bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        ##x
        #bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        #bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.174533
        #bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.872665
        ##y
        #bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        #bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        #bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        ##z
        #bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        #bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.523599
        #bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.523599
        #=====
        actual_bone = 'Arm_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.006"]
        #=====
        actual_bone = 'Forearm_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.007"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -2.53073
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = -0.191986
        #=====
        actual_bone = 'Arm_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.003"]
        #=====
        actual_bone = 'Forearm_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.004"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = False
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = False
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0.191986
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 2.53073
        #=====
        actual_bone = 'Thigh_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.013"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -1.76278
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 1.3439
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.785398
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.174533
        #=====
        actual_bone = 'Leg_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.014"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = 0.0698132
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 2.0944
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0
        #=====
        actual_bone = 'Foot_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.019"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.523599
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0
        #=====
        actual_bone = 'Thigh_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.010"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -1.76278
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 1.3439
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.785398

        actual_bone = 'Leg_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.011"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = 0.0698132
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 2.0944
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0

        actual_bone = 'Foot_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.022"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.523599
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0

        bpy.context.scene.frame_end = len(pic[person_id]['pose'])

        bpy.ops.nla.bake(frame_start=1, frame_end=len(pic[person_id]['pose']), visual_keying=True, clear_constraints=True, clear_parents=True, bake_types={'POSE'})
        bpy.ops.object.mode_set(mode='OBJECT')

        #apagar collection points criada
        collection = bpy.data.collections.get('Point')
        #
        for obj in collection.objects:
            bpy.data.objects.remove(obj, do_unlink=True)
        bpy.data.collections.remove(collection)

        sk_value_prop = context.scene.sk_value_prop
        if raw_bool == True:
            print('raw_bool True - ',raw_bool)

            x_original, y_original, z_original = helper_functions.get_rotations()
            sk_value_prop.sk_root_rot_x = math.degrees(x_original)
            sk_value_prop.sk_root_rot_y = math.degrees(y_original)
            sk_value_prop.sk_root_rot_z = math.degrees(z_original)

            #in this case both original and actual is the same, because there was no alteration on the angle
            x_actual_deg = math.degrees(x_original)
            y_actual_deg = math.degrees(y_original)
            z_actual_deg = math.degrees(z_original)

            sk_value_prop.sk_root_actual_rot_x = x_actual_deg
            sk_value_prop.sk_root_actual_rot_y = y_actual_deg
            sk_value_prop.sk_root_actual_rot_z = z_actual_deg
        else:
            print('raw_bool False - ',raw_bool)
            x_deg, y_deg, z_deg = helper_functions.anim_to_origin()
            #take the information of the rotation to the panel
            print('result x: ',x_deg)
            print('result y: ',y_deg)
            print('result z: ',z_deg)
            sk_value_prop.sk_root_rot_x = x_deg
            sk_value_prop.sk_root_rot_y = y_deg
            sk_value_prop.sk_root_rot_z = z_deg


        
        

        return{'FINISHED'}

        
class Mediapipe_Pose_estimation(Operator, ImportHelper):
    bl_idname = "mocap.mediapipe_pose"
    bl_label = "Generate Pose using MediaPipe"
    bl_description = "Generate Mocap data with MediaPipe"


    filename_ext = ".mp4"

    filter_glob: StringProperty(
        default="*.mp4",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

        
    def execute(self,context):

        import cv2
        import mediapipe as mp
        import bpy
        import sys
        from mathutils import Vector
        import math

        multiplier = context.scene.sk_value_prop.sk_value
        raw_bool = context.scene.sk_value_prop.sk_raw_bool

        def middle_point(p1,p2,p_middle):
            bpy.ops.object.select_all(action='DESELECT')
            bpy.data.objects[p1].select_set(True)
            bpy.data.objects[p2].select_set(True)
            bpy.context.view_layer.objects.active = bpy.data.objects[p2]
            obs = bpy.context.selected_objects
            n = len(obs)
        #    print('n: ',n)
            assert(n)
            #scene.cursor.location = sum([o.matrix_world.translation for o in obs], Vector()) / n
            bpy.data.objects[p_middle].location = sum([o.matrix_world.translation for o in obs], Vector()) / n



        def get_landmarks(vid_name, frame_list):
            mp_drawing = mp.solutions.drawing_utils
            mp_holistic = mp.solutions.holistic
        #
            # For static images:
            holistic = mp_holistic.Holistic(static_image_mode=True)
            for idx, image in enumerate(frame_list):
        #        image_height, image_width, _ = image.shape
                # Convert the BGR image to RGB before processing.
                results = holistic.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        #
        #
                x=0
                y=1
                z=2
                i=0
                print('frame: ',idx)
                try:
                    len(results.pose_landmarks.landmark)
                    for i in range(len(results.pose_landmarks.landmark)):
                        x_pose = results.pose_landmarks.landmark[i].x
                        y_pose = results.pose_landmarks.landmark[i].y
                        z_pose = results.pose_landmarks.landmark[i].z
                        bpy.data.objects["Point."+str(1000+i)[1:]].location[x]=x_pose
                        bpy.data.objects["Point."+str(1000+i)[1:]].location[y]=y_pose
                        bpy.data.objects["Point."+str(1000+i)[1:]].location[z]=z_pose
                        if i == 10:
                            middle_point('Point.009','Point.010','Point.033')
                            bpy.data.objects["Point."+str(1000+33)[1:]].keyframe_insert(data_path="location", frame=idx)
                        if i == 12:
                            middle_point('Point.011','Point.012','Point.034')
                            bpy.data.objects["Point."+str(1000+34)[1:]].keyframe_insert(data_path="location", frame=idx)
                        if i == 24:
                            middle_point('Point.023','Point.024','Point.035')
                            bpy.data.objects["Point."+str(1000+35)[1:]].keyframe_insert(data_path="location", frame=idx)
                        bpy.data.objects["Point."+str(1000+i)[1:]].keyframe_insert(data_path="location", frame=idx)
            #
        #                print('frame: ',idx,' landmark_id: ',i,'x: ', x_pose, ' - y: ',y_pose,' - z: ',z_pose)
                except:
                    print('Error Frame: ',idx)
                    bpy.data.objects["Point."+str(1000+i)[1:]].location[x]=0
                    bpy.data.objects["Point."+str(1000+i)[1:]].location[y]=0
                    bpy.data.objects["Point."+str(1000+i)[1:]].location[z]=0
                    bpy.data.objects["Point."+str(1000+i)[1:]].keyframe_insert(data_path="location", frame=idx)
                    continue
            holistic.close()


        def get_video_frames(file_url):
            vidcap = cv2.VideoCapture(file_url)
            success, image = vidcap.read()
            # array of objects with class 'numpy.ndarray'
            frames = []
            while success:
                frames.append(image)
                success, image = vidcap.read()
        #
            return frames

        def create_dots(name, amount):
            #remove Collection
            if bpy.data.collections.find(name) >= 0:
                collection = bpy.data.collections.get(name)
                #
                for obj in collection.objects:
                    bpy.data.objects.remove(obj, do_unlink=True)
                bpy.data.collections.remove(collection)
            #cria os pontos nuima collection chamada Points
            #=====================================================
            collection = bpy.data.collections.new(name)
            bpy.context.scene.collection.children.link(collection)
        #
            layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
            bpy.context.view_layer.active_layer_collection = layer_collection
        #
            for point in range(amount):
                bpy.ops.mesh.primitive_plane_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
                bpy.ops.mesh.merge(type='CENTER')
                bpy.ops.object.editmode_toggle()
                bpy.context.active_object.name = name+'.'+str(1000+point)[1:]
            #=====================================================
            
        #==============================
        #codes to size the bones
        #==============================

        def distance(point1, point2) -> float: 
            #Calculate distance between two points in 3D.
        #    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2)
            return math.sqrt((point2.location[0] - point1.location[0]) ** 2 + (point2.location[1] - point1.location[1]) ** 2 + (point2.location[2] - point1.location[2]) ** 2)


        def size_bone(point_name1, point_name2, bone):
            p1 = bpy.data.objects[point_name1]
            p2 = bpy.data.objects[point_name2]
            #edit bones
            if bpy.context.active_object.mode == 'EDIT':
                bpy.context.object.data.edit_bones[bone].length= distance(p1,p2)
            else:
                bpy.ops.object.editmode_toggle()
                bpy.context.object.data.edit_bones[bone].length= distance(p1,p2)
            bpy.ops.object.editmode_toggle()




        #path = r'D:\MOCAP\EasyMocap-master\demo_test\videos\1.mp4'
        # path = r'D:\Video_editing\running e brack dance para mocap.mp4'
        path = self.filepath
        create_dots('Point',36)
        get_landmarks('Name', get_video_frames(path))


        import bpy


        #===========
        # selectign Scene Collection
        scene_collection = bpy.context.view_layer.layer_collection
        bpy.context.view_layer.active_layer_collection = scene_collection


        #===================================
        #creating bones
        #====================================

        bpy.ops.object.armature_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1)) #cria armature e primeiro bone
        #bpy.ops.object.editmode_toggle()
        #bpy.data.armatures['Armature'].edit_bones.active = bpy.context.object.data.edit_bones['Bone']


        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs


        bpy.ops.armature.select_all(action='DESELECT')
        #bpy.context.object.data.edit_bones['Bone'].select_tail=True
        obs[len(obs)-1].data.edit_bones['Bone'].select_tail=True

        bpy.ops.armature.bone_primitive_add()#Spine
        #bpy.ops.armature.extrude_move()#Neck
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        #bpy.ops.armature.extrude_move()#Face
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})


        bpy.ops.armature.bone_primitive_add()#Arm_L
        #bpy.ops.armature.extrude_move()#Forearm_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Arm_R
        #bpy.ops.armature.extrude_move()#Forearm_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Thigh_L
        #bpy.ops.armature.extrude_move()#Leg_L
        #bpy.ops.armature.extrude_move()#Foot_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Thigh_R
        #bpy.ops.armature.extrude_move()#Leg_R
        #bpy.ops.armature.extrude_move()#Foot_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})


        obs[len(obs)-1].data.edit_bones["Bone"].name = 'Root'
        obs[len(obs)-1].data.edit_bones["Bone.001"].name = 'Spine'
        obs[len(obs)-1].data.edit_bones["Bone.002"].name = 'Neck'
        obs[len(obs)-1].data.edit_bones["Bone.003"].name = 'Face'
        obs[len(obs)-1].data.edit_bones["Bone.004"].name = 'Arm_L'
        obs[len(obs)-1].data.edit_bones["Bone.005"].name = 'Forearm_L'
        obs[len(obs)-1].data.edit_bones["Bone.006"].name = 'Arm_R'
        obs[len(obs)-1].data.edit_bones["Bone.007"].name = 'Forearm_R'
        obs[len(obs)-1].data.edit_bones["Bone.008"].name = 'Thigh_L'
        obs[len(obs)-1].data.edit_bones["Bone.009"].name = 'Leg_L'
        obs[len(obs)-1].data.edit_bones["Bone.010"].name = 'Foot_L'
        obs[len(obs)-1].data.edit_bones["Bone.011"].name = 'Thigh_R'
        obs[len(obs)-1].data.edit_bones["Bone.012"].name = 'Leg_R'
        obs[len(obs)-1].data.edit_bones["Bone.013"].name = 'Foot_R'


        #Hierarquia
        bpy.context.object.data.edit_bones["Spine"].parent = bpy.context.object.data.edit_bones["Root"]
        bpy.context.object.data.edit_bones["Arm_L"].parent = bpy.context.object.data.edit_bones["Spine"]
        bpy.context.object.data.edit_bones["Arm_R"].parent = bpy.context.object.data.edit_bones["Spine"]
        bpy.context.object.data.edit_bones["Thigh_L"].parent = bpy.context.object.data.edit_bones["Root"]
        bpy.context.object.data.edit_bones["Thigh_R"].parent = bpy.context.object.data.edit_bones["Root"]

        bpy.ops.object.editmode_toggle()




        from mathutils import Vector
        import bpy

        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects['Point.034'].select_set(True)
        bpy.data.objects['Point.035'].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects['Point.034']
        obs = bpy.context.selected_objects
        n = len(obs)
        #    print('n: ',n)
        assert(n)
        #scene.cursor.location = sum([o.matrix_world.translation for o in obs], Vector()) / n
        #bpy.data.objects[p_middle].location = sum([o.matrix_world.translation for o in obs], Vector()) / n



        x_subtract = abs(obs[0].matrix_world.translation.x - obs[1].matrix_world.translation.x)
        y_subtract = abs(obs[0].matrix_world.translation.y - obs[1].matrix_world.translation.y)
        z_subtract = abs(obs[0].matrix_world.translation.z - obs[1].matrix_world.translation.z)

        max(x_subtract, y_subtract, z_subtract) #maior das medidas
        unit = max(x_subtract, y_subtract, z_subtract)/3
        unit = unit*multiplier

        root_sz    =unit/10
        spine_sz   =unit*3.5
        neck_sz    =unit
        face_sz    =unit
        thigh_sz    =unit*3
        leg_sz     =unit*2.5
        foot_sz    =unit #inclinado 45 graud pra frente
        arm_sz     =unit*1.5
        forearm_sz =unit*1.5



        #if bpy.context.active_object.mode != 'EDIT':
        #    bpy.ops.object.editmode_toggle()
        #==========================================
        #selecting and making the armature Active
        #selecionando armature
        #==========================================
        bpy.ops.object.select_all(action='DESELECT')
        #bpy.ops.armature.select_all(action='DESELECT')

        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        armature = obs[len(obs)-1].name

        #bpy.data.objects[armature].select_set(True)
        obs[len(obs)-1].select_set(True)
        view_layer = bpy.context.view_layer
        #Armature_obj = bpy.context.scene.objects[armature]
        Armature_obj = obs[len(obs)-1]
        view_layer.objects.active = Armature_obj


        #converting to euler rotation
        order = 'XYZ'
        context = bpy.context
        rig_object = context.active_object
        for pb in rig_object.pose.bones:
            pb.rotation_mode = order



        bpy.ops.object.editmode_toggle()

        #changing location
        #resetting
        bpy.context.object.data.edit_bones["Spine"].head.xy=0
        bpy.context.object.data.edit_bones["Neck"].head.xy=0
        bpy.context.object.data.edit_bones["Face"].head.xy=0

        bpy.context.object.data.edit_bones["Arm_L"].head.xy=0
        bpy.context.object.data.edit_bones["Forearm_L"].head.xy=0

        bpy.context.object.data.edit_bones["Arm_R"].head.xy=0
        bpy.context.object.data.edit_bones["Forearm_R"].head.xy=0

        bpy.context.object.data.edit_bones["Thigh_L"].head.xy=0
        bpy.context.object.data.edit_bones["Leg_L"].head.xy=0
        bpy.context.object.data.edit_bones["Foot_L"].head.xy=0

        bpy.context.object.data.edit_bones["Thigh_R"].head.xy=0
        bpy.context.object.data.edit_bones["Leg_R"].head.xy=0
        bpy.context.object.data.edit_bones["Foot_R"].head.xy=0
        #tail
        bpy.context.object.data.edit_bones["Face"].tail.xy=0
        bpy.context.object.data.edit_bones["Forearm_L"].tail.xy=0
        bpy.context.object.data.edit_bones["Forearm_R"].tail.xy=0
        bpy.context.object.data.edit_bones["Foot_L"].tail.xy=0
        bpy.context.object.data.edit_bones["Foot_R"].tail.xy=0




        bpy.context.object.data.edit_bones["Root"].length = root_sz

        bpy.context.object.data.edit_bones["Spine"].head.z = unit/2
        bpy.context.object.data.edit_bones["Spine"].tail.z = spine_sz

        bpy.context.object.data.edit_bones["Neck"].tail.z =  spine_sz + neck_sz
        bpy.context.object.data.edit_bones["Neck"].tail.y = neck_sz/3
        bpy.context.object.data.edit_bones["Face"].tail.z = spine_sz + neck_sz
        bpy.context.object.data.edit_bones["Face"].tail.y = face_sz*-1

        bpy.context.object.data.edit_bones["Arm_L"].head.z= spine_sz
        bpy.context.object.data.edit_bones["Arm_L"].head.x= unit/2
        bpy.context.object.data.edit_bones["Forearm_L"].head.z=  spine_sz
        bpy.context.object.data.edit_bones["Forearm_L"].head.x= unit + arm_sz
        bpy.context.object.data.edit_bones["Forearm_L"].tail.z= spine_sz
        bpy.context.object.data.edit_bones["Forearm_L"].tail.x= unit + arm_sz + forearm_sz

        bpy.context.object.data.edit_bones["Arm_R"].head.z= spine_sz
        bpy.context.object.data.edit_bones["Arm_R"].head.x= (unit/2)*-1
        bpy.context.object.data.edit_bones["Forearm_R"].head.z= unit/2 + spine_sz
        bpy.context.object.data.edit_bones["Forearm_R"].head.x= (unit + arm_sz) *-1
        bpy.context.object.data.edit_bones["Forearm_R"].tail.z= unit/2 + spine_sz
        bpy.context.object.data.edit_bones["Forearm_R"].tail.x= (unit + arm_sz + forearm_sz) *-1

        bpy.context.object.data.edit_bones["Thigh_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Thigh_L"].head.z= (unit/5)*-1
        bpy.context.object.data.edit_bones["Leg_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Leg_L"].head.z= (unit/5 + thigh_sz)*-1
        bpy.context.object.data.edit_bones["Foot_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Foot_L"].head.z= (unit/5 + thigh_sz + leg_sz)*-1
        bpy.context.object.data.edit_bones["Foot_L"].tail.x= unit*3/4
        bpy.context.object.data.edit_bones["Foot_L"].tail.z= (unit/5 + thigh_sz + leg_sz + foot_sz/2)*-1
        bpy.context.object.data.edit_bones["Foot_L"].tail.y= foot_sz/2*-1

        bpy.context.object.data.edit_bones["Thigh_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Thigh_R"].head.z= (unit/5)*-1
        bpy.context.object.data.edit_bones["Leg_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Leg_R"].head.z= (unit/5 + thigh_sz)*-1
        bpy.context.object.data.edit_bones["Foot_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Foot_R"].head.z= (unit/5 + thigh_sz + leg_sz)*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.z= (unit/5 + thigh_sz + leg_sz + foot_sz/2)*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.y= foot_sz/2*-1

        bpy.ops.object.editmode_toggle()

        import bpy

        #comecando configuração  seguir movimentos pontos
        #colocando em pose mode


        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        bpy.ops.object.mode_set(mode='POSE')


        actual_bone = 'Root'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.035"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.011"]

        #====
        actual_bone = 'Spine'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.011"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.012"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[2].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[2].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[2].min_x  = -0.349066
        bpy.context.object.pose.bones[actual_bone].constraints[2].max_x = 0.349066
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[2].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[2].min_y = -0.698132
        bpy.context.object.pose.bones[actual_bone].constraints[2].max_y = 0.698132
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[2].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[2].min_z = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[2].max_z = 0.174533

        #=====
        actual_bone = 'Neck'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.033"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 1.0472
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0.523599
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.349066
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.349066
        #=====
        actual_bone = 'Face'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.000"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.872665
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.523599
        #=====
        actual_bone = 'Arm_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.013"]
        #=====
        actual_bone = 'Forearm_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.015"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -2.53073
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = -0.191986
        #=====
        actual_bone = 'Arm_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.014"]
        #=====
        actual_bone = 'Forearm_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.016"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = False
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = False
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0.191986
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 2.53073
        #=====
        actual_bone = 'Thigh_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.025"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -1.76278
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 1.3439
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.785398
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.174533
        #=====
        actual_bone = 'Leg_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.027"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = 0.0698132
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 2.0944
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0
        #=====
        actual_bone = 'Foot_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.031"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.523599
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0
        #=====
        actual_bone = 'Thigh_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.026"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -1.76278
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 1.3439
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.785398

        actual_bone = 'Leg_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.028"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = 0.0698132
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 2.0944
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0

        actual_bone = 'Foot_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.032"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.523599
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0

        frames = len(get_video_frames(path))

        bpy.context.scene.frame_end = frames

        bpy.ops.nla.bake(frame_start=1, frame_end=frames, visual_keying=True, clear_constraints=True, clear_parents=True, bake_types={'POSE'})
        bpy.ops.object.mode_set(mode='OBJECT')



        #apagar collection points criada
        collection = bpy.data.collections.get('Point')
        #
        for obj in collection.objects:
            bpy.data.objects.remove(obj, do_unlink=True)
        bpy.data.collections.remove(collection)

        sk_value_prop = context.scene.sk_value_prop
        if raw_bool == True:
            print('raw_bool True - ',raw_bool)

            x_original, y_original, z_original = helper_functions.get_rotations()
            sk_value_prop.sk_root_rot_x = math.degrees(x_original)
            sk_value_prop.sk_root_rot_y = math.degrees(y_original)
            sk_value_prop.sk_root_rot_z = math.degrees(z_original)

            #in this case both original and actual is the same, because there was no alteration on the angle
            x_actual_deg = math.degrees(x_original)
            y_actual_deg = math.degrees(y_original)
            z_actual_deg = math.degrees(z_original)

            sk_value_prop.sk_root_actual_rot_x = x_actual_deg
            sk_value_prop.sk_root_actual_rot_y = y_actual_deg
            sk_value_prop.sk_root_actual_rot_z = z_actual_deg
        else:
            print('raw_bool False - ',raw_bool)
            x_deg, y_deg, z_deg = helper_functions.anim_to_origin()
            #take the information of the rotation to the panel
            print('result x: ',x_deg)
            print('result y: ',y_deg)
            print('result z: ',z_deg)
            sk_value_prop.sk_root_rot_x = x_deg
            sk_value_prop.sk_root_rot_y = y_deg
            sk_value_prop.sk_root_rot_z = z_deg



        return{'FINISHED'}


class Install_Mediapipe(bpy.types.Operator):
    bl_idname = "install.mediapipe_package"
    bl_label = "Install python Mediapipe Package"
    bl_description = "Install python Mediapipe Package"

    def execute(self,context):

        import subprocess
        import sys
        import os
        
        # path to python.exe
        python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')
        python_pip = os.path.join(sys.prefix, 'lib', 'site-packages', 'pip')
        

        # upgrade pip
        # subprocess.call([python_exe, "-m", "ensurepip"])
        subprocess.call([python_exe, python_pip, "install", "--upgrade", "pip"])
        
        # install required packages
        subprocess.call([python_exe, python_pip, "install", "mediapipe"])

        return{'FINISHED'}


class Install_Joblib(bpy.types.Operator):
    bl_idname = "install.joblib_package"
    bl_label = "Install python JobLib Package"
    bl_description = "Install python JobLib Package"

    def execute(self,context):

        import subprocess
        import sys
        import os
        
        # path to python.exe
        python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')
        
        # upgrade pip
        subprocess.call([python_exe, "-m", "ensurepip"])
        subprocess.call([python_exe, "-m", "pip", "install", "--upgrade", "pip"])
        
        # install required packages
        subprocess.call([python_exe, "-m", "pip", "install", "joblib"])

        return{'FINISHED'}

class Convert_axis(Operator):
    bl_idname = "mocap.convert_axis"
    bl_label = "Convert animation axis"
    bl_description = "Convert Axis"

    def execute(self,context):
        
        skvalue = context.scene.sk_value_prop

        print('from: ',skvalue.sk_from_axis,' ','to: ',skvalue.sk_to_axis)
        print('from simplified: ',skvalue.sk_from_axis[-1:],' ','to: ',skvalue.sk_to_axis[-1:])

        helper_functions.rotate_orientation(skvalue.sk_from_axis[-1:],skvalue.sk_to_axis[-1:])
        
        #send actual rotations
        x_actual_deg, y_actual_deg, z_actual_deg = helper_functions.get_rotations()
        skvalue.sk_root_actual_rot_x = math.degrees(x_actual_deg)
        skvalue.sk_root_actual_rot_y = math.degrees(y_actual_deg)
        skvalue.sk_root_actual_rot_z = math.degrees(z_actual_deg)
        return{'FINISHED'}

class Reset_location(Operator):
    bl_idname = "mocap.reset_location"
    bl_label = "Move animation to origin"
    bl_description = "Center Location"
    
    def execute(sel,context):
        helper_functions.reset_loc()
        return{'FINISHED'}

class Reset_rotation(Operator):
    bl_idname = "mocap.reset_rotation"
    bl_label = "Reset rotation, to the Rest rotatio position"
    bl_description = "Reset Rotation"
    
    def execute(sel,context):
        helper_functions.reset_rot()

        sk_value_prop = context.scene.sk_value_prop
        x_actual_deg, y_actual_deg, z_actual_deg = helper_functions.get_rotations()
        sk_value_prop.sk_root_actual_rot_x = math.degrees(x_actual_deg)
        sk_value_prop.sk_root_actual_rot_y = math.degrees(y_actual_deg)
        sk_value_prop.sk_root_actual_rot_z = math.degrees(z_actual_deg)
        return{'FINISHED'}

class Foot_high(Operator):
    bl_idname = "mocap.foot_high"
    bl_label = "Move the animation so the feet touch the floor"
    bl_description = "Move the feet to touch the floor"
    
    def execute(sel,context):
        helper_functions.foot_high()
        return{'FINISHED'}

class Compensate_Rotation(Operator):
    bl_idname = "mocap.compensate_rotation"
    bl_label = "compensate rotation"
    bl_description = "Compensate rotatio acording to value inserted"
    
    def execute(sel,context):
        skvalue = context.scene.sk_value_prop

        helper_functions.compensate_rot(skvalue.sk_rot_compens_x,skvalue.sk_rot_compens_y,skvalue.sk_rot_compens_z)
        return{'FINISHED'}


class Smooth_Bone(Operator):
    bl_idname = "mocap.smooth_bones"
    bl_label = "Smooth Bones"
    bl_description = "Smooth the curves"
    
    def execute(sel,context):
        
        # currently selected 
        o = bpy.context.object
        

        helper_functions.smooth_curves(o)
        return{'FINISHED'}


########################################
##### MediaPipe Realtime
########################################


class Mediapipe_Pose_Prepare_Skeleton_RT(Operator):
    bl_idname = "mocap.mediapipe_prepare_sk_rt"
    bl_label = "Generate Pose using MediaPipe"
    bl_description = "Generate Mocap data with MediaPipe"

       
    def execute(self,context):

        # import cv2
        # import mediapipe as mp
        import bpy
        import sys
        from mathutils import Vector
        import math

        multiplier = context.scene.sk_value_prop.sk_value
        raw_bool = context.scene.sk_value_prop.sk_raw_bool

        def middle_point(p1,p2,p_middle):
            bpy.ops.object.select_all(action='DESELECT')
            bpy.data.objects[p1].select_set(True)
            bpy.data.objects[p2].select_set(True)
            bpy.context.view_layer.objects.active = bpy.data.objects[p2]
            obs = bpy.context.selected_objects
            n = len(obs)
            # print('n: ',n)
            assert(n)
            #scene.cursor.location = sum([o.matrix_world.translation for o in obs], Vector()) / n
            bpy.data.objects[p_middle].location = sum([o.matrix_world.translation for o in obs], Vector()) / n

        # def get_video_frames(file_url):
        #     vidcap = cv2.VideoCapture(file_url)
        #     success, image = vidcap.read()
        #     # array of objects with class 'numpy.ndarray'
        #     frames = []
        #     while success:
        #         frames.append(image)
        #         success, image = vidcap.read()
        #     #
        #     return frames

        def create_dots(name, amount):
            #remove Collection
            if bpy.data.collections.find(name) >= 0:
                collection = bpy.data.collections.get(name)
                #
                for obj in collection.objects:
                    bpy.data.objects.remove(obj, do_unlink=True)
                bpy.data.collections.remove(collection)
            #cria os pontos nuima collection chamada Points
            #=====================================================
            collection = bpy.data.collections.new(name)
            bpy.context.scene.collection.children.link(collection)
            #
            layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
            bpy.context.view_layer.active_layer_collection = layer_collection
            #
            for point in range(amount):
                bpy.ops.mesh.primitive_plane_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
                bpy.ops.mesh.merge(type='CENTER')
                bpy.ops.object.editmode_toggle()
                bpy.context.active_object.name = name+'.'+str(1000+point)[1:]
            #=====================================================
            
        #==============================
        #codes to size the bones
        #==============================

        def distance(point1, point2) -> float: 
            #Calculate distance between two points in 3D.
            # return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2)
            return math.sqrt((point2.location[0] - point1.location[0]) ** 2 + (point2.location[1] - point1.location[1]) ** 2 + (point2.location[2] - point1.location[2]) ** 2)


        def size_bone(point_name1, point_name2, bone):
            p1 = bpy.data.objects[point_name1]
            p2 = bpy.data.objects[point_name2]
            #edit bones
            if bpy.context.active_object.mode == 'EDIT':
                bpy.context.object.data.edit_bones[bone].length= distance(p1,p2)
            else:
                bpy.ops.object.editmode_toggle()
                bpy.context.object.data.edit_bones[bone].length= distance(p1,p2)
            bpy.ops.object.editmode_toggle()


        create_dots('Point',36)
        


        import bpy


        #===========
        # selectign Scene Collection
        scene_collection = bpy.context.view_layer.layer_collection
        bpy.context.view_layer.active_layer_collection = scene_collection


        #===================================
        #creating bones
        #====================================

        bpy.ops.object.armature_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1)) #cria armature e primeiro bone
        #bpy.ops.object.editmode_toggle()
        #bpy.data.armatures['Armature'].edit_bones.active = bpy.context.object.data.edit_bones['Bone']


        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs


        bpy.ops.armature.select_all(action='DESELECT')
        #bpy.context.object.data.edit_bones['Bone'].select_tail=True
        obs[len(obs)-1].data.edit_bones['Bone'].select_tail=True

        bpy.ops.armature.bone_primitive_add()#Spine
        #bpy.ops.armature.extrude_move()#Neck
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        #bpy.ops.armature.extrude_move()#Face
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})


        bpy.ops.armature.bone_primitive_add()#Arm_L
        #bpy.ops.armature.extrude_move()#Forearm_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Arm_R
        #bpy.ops.armature.extrude_move()#Forearm_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Thigh_L
        #bpy.ops.armature.extrude_move()#Leg_L
        #bpy.ops.armature.extrude_move()#Foot_L
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.armature.bone_primitive_add()#Thigh_R
        #bpy.ops.armature.extrude_move()#Leg_R
        #bpy.ops.armature.extrude_move()#Foot_R
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.1), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})


        obs[len(obs)-1].data.edit_bones["Bone"].name = 'Root'
        obs[len(obs)-1].data.edit_bones["Bone.001"].name = 'Spine'
        obs[len(obs)-1].data.edit_bones["Bone.002"].name = 'Neck'
        obs[len(obs)-1].data.edit_bones["Bone.003"].name = 'Face'
        obs[len(obs)-1].data.edit_bones["Bone.004"].name = 'Arm_L'
        obs[len(obs)-1].data.edit_bones["Bone.005"].name = 'Forearm_L'
        obs[len(obs)-1].data.edit_bones["Bone.006"].name = 'Arm_R'
        obs[len(obs)-1].data.edit_bones["Bone.007"].name = 'Forearm_R'
        obs[len(obs)-1].data.edit_bones["Bone.008"].name = 'Thigh_L'
        obs[len(obs)-1].data.edit_bones["Bone.009"].name = 'Leg_L'
        obs[len(obs)-1].data.edit_bones["Bone.010"].name = 'Foot_L'
        obs[len(obs)-1].data.edit_bones["Bone.011"].name = 'Thigh_R'
        obs[len(obs)-1].data.edit_bones["Bone.012"].name = 'Leg_R'
        obs[len(obs)-1].data.edit_bones["Bone.013"].name = 'Foot_R'


        #Hierarquia
        bpy.context.object.data.edit_bones["Spine"].parent = bpy.context.object.data.edit_bones["Root"]
        bpy.context.object.data.edit_bones["Arm_L"].parent = bpy.context.object.data.edit_bones["Spine"]
        bpy.context.object.data.edit_bones["Arm_R"].parent = bpy.context.object.data.edit_bones["Spine"]
        bpy.context.object.data.edit_bones["Thigh_L"].parent = bpy.context.object.data.edit_bones["Root"]
        bpy.context.object.data.edit_bones["Thigh_R"].parent = bpy.context.object.data.edit_bones["Root"]

        bpy.ops.object.editmode_toggle()




        from mathutils import Vector
        import bpy

        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects['Point.034'].select_set(True)
        bpy.data.objects['Point.035'].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects['Point.034']
        obs = bpy.context.selected_objects
        n = len(obs)
        #    print('n: ',n)
        assert(n)
        #scene.cursor.location = sum([o.matrix_world.translation for o in obs], Vector()) / n
        #bpy.data.objects[p_middle].location = sum([o.matrix_world.translation for o in obs], Vector()) / n



        x_subtract = abs(obs[0].matrix_world.translation.x - obs[1].matrix_world.translation.x)
        y_subtract = abs(obs[0].matrix_world.translation.y - obs[1].matrix_world.translation.y)
        z_subtract = abs(obs[0].matrix_world.translation.z - obs[1].matrix_world.translation.z)

        max(x_subtract, y_subtract, z_subtract) #maior das medidas
        # unit = max(x_subtract, y_subtract, z_subtract)/3
        unit=1
        unit = unit*multiplier

        root_sz    =unit/10
        spine_sz   =unit*3.5
        neck_sz    =unit
        face_sz    =unit
        thigh_sz    =unit*3
        leg_sz     =unit*2.5
        foot_sz    =unit #inclinado 45 graud pra frente
        arm_sz     =unit*1.5
        forearm_sz =unit*1.5



        #if bpy.context.active_object.mode != 'EDIT':
        #    bpy.ops.object.editmode_toggle()
        #==========================================
        #selecting and making the armature Active
        #selecionando armature
        #==========================================
        bpy.ops.object.select_all(action='DESELECT')
        #bpy.ops.armature.select_all(action='DESELECT')

        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        armature = obs[len(obs)-1].name

        #bpy.data.objects[armature].select_set(True)
        obs[len(obs)-1].select_set(True)
        view_layer = bpy.context.view_layer
        #Armature_obj = bpy.context.scene.objects[armature]
        Armature_obj = obs[len(obs)-1]
        view_layer.objects.active = Armature_obj


        #converting to euler rotation
        order = 'XYZ'
        context = bpy.context
        rig_object = context.active_object
        for pb in rig_object.pose.bones:
            pb.rotation_mode = order



        bpy.ops.object.editmode_toggle()

        #changing location
        #resetting
        bpy.context.object.data.edit_bones["Spine"].head.xy=0
        bpy.context.object.data.edit_bones["Neck"].head.xy=0
        bpy.context.object.data.edit_bones["Face"].head.xy=0

        bpy.context.object.data.edit_bones["Arm_L"].head.xy=0
        bpy.context.object.data.edit_bones["Forearm_L"].head.xy=0

        bpy.context.object.data.edit_bones["Arm_R"].head.xy=0
        bpy.context.object.data.edit_bones["Forearm_R"].head.xy=0

        bpy.context.object.data.edit_bones["Thigh_L"].head.xy=0
        bpy.context.object.data.edit_bones["Leg_L"].head.xy=0
        bpy.context.object.data.edit_bones["Foot_L"].head.xy=0

        bpy.context.object.data.edit_bones["Thigh_R"].head.xy=0
        bpy.context.object.data.edit_bones["Leg_R"].head.xy=0
        bpy.context.object.data.edit_bones["Foot_R"].head.xy=0
        #tail
        bpy.context.object.data.edit_bones["Face"].tail.xy=0
        bpy.context.object.data.edit_bones["Forearm_L"].tail.xy=0
        bpy.context.object.data.edit_bones["Forearm_R"].tail.xy=0
        bpy.context.object.data.edit_bones["Foot_L"].tail.xy=0
        bpy.context.object.data.edit_bones["Foot_R"].tail.xy=0




        bpy.context.object.data.edit_bones["Root"].length = root_sz

        bpy.context.object.data.edit_bones["Spine"].head.z = unit/2
        bpy.context.object.data.edit_bones["Spine"].tail.z = spine_sz

        bpy.context.object.data.edit_bones["Neck"].tail.z =  spine_sz + neck_sz
        bpy.context.object.data.edit_bones["Neck"].tail.y = neck_sz/3
        bpy.context.object.data.edit_bones["Face"].tail.z = spine_sz + neck_sz
        bpy.context.object.data.edit_bones["Face"].tail.y = face_sz*-1

        bpy.context.object.data.edit_bones["Arm_L"].head.z= spine_sz
        bpy.context.object.data.edit_bones["Arm_L"].head.x= unit/2
        bpy.context.object.data.edit_bones["Forearm_L"].head.z=  spine_sz
        bpy.context.object.data.edit_bones["Forearm_L"].head.x= unit + arm_sz
        bpy.context.object.data.edit_bones["Forearm_L"].tail.z= spine_sz
        bpy.context.object.data.edit_bones["Forearm_L"].tail.x= unit + arm_sz + forearm_sz

        bpy.context.object.data.edit_bones["Arm_R"].head.z= spine_sz
        bpy.context.object.data.edit_bones["Arm_R"].head.x= (unit/2)*-1
        bpy.context.object.data.edit_bones["Forearm_R"].head.z= unit/2 + spine_sz
        bpy.context.object.data.edit_bones["Forearm_R"].head.x= (unit + arm_sz) *-1
        bpy.context.object.data.edit_bones["Forearm_R"].tail.z= unit/2 + spine_sz
        bpy.context.object.data.edit_bones["Forearm_R"].tail.x= (unit + arm_sz + forearm_sz) *-1

        bpy.context.object.data.edit_bones["Thigh_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Thigh_L"].head.z= (unit/5)*-1
        bpy.context.object.data.edit_bones["Leg_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Leg_L"].head.z= (unit/5 + thigh_sz)*-1
        bpy.context.object.data.edit_bones["Foot_L"].head.x= unit*3/4
        bpy.context.object.data.edit_bones["Foot_L"].head.z= (unit/5 + thigh_sz + leg_sz)*-1
        bpy.context.object.data.edit_bones["Foot_L"].tail.x= unit*3/4
        bpy.context.object.data.edit_bones["Foot_L"].tail.z= (unit/5 + thigh_sz + leg_sz + foot_sz/2)*-1
        bpy.context.object.data.edit_bones["Foot_L"].tail.y= foot_sz/2*-1

        bpy.context.object.data.edit_bones["Thigh_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Thigh_R"].head.z= (unit/5)*-1
        bpy.context.object.data.edit_bones["Leg_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Leg_R"].head.z= (unit/5 + thigh_sz)*-1
        bpy.context.object.data.edit_bones["Foot_R"].head.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Foot_R"].head.z= (unit/5 + thigh_sz + leg_sz)*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.x= unit*3/4*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.z= (unit/5 + thigh_sz + leg_sz + foot_sz/2)*-1
        bpy.context.object.data.edit_bones["Foot_R"].tail.y= foot_sz/2*-1

        bpy.ops.object.editmode_toggle()

        import bpy

        #comecando configuração  seguir movimentos pontos
        #colocando em pose mode


        obs = []
        for ob in bpy.context.scene.objects:
            if ob.type == 'ARMATURE':
                obs.append(ob)
        #obs

        bpy.ops.object.mode_set(mode='POSE')


        actual_bone = 'Root'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='COPY_LOCATION')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.035"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.011"]

        #====
        actual_bone = 'Spine'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.011"]
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[1].target = bpy.data.objects["Point.012"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[2].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[2].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[2].min_x  = -0.349066
        bpy.context.object.pose.bones[actual_bone].constraints[2].max_x = 0.349066
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[2].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[2].min_y = -0.698132
        bpy.context.object.pose.bones[actual_bone].constraints[2].max_y = 0.698132
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[2].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[2].min_z = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[2].max_z = 0.174533

        #=====
        actual_bone = 'Neck'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.033"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 1.0472
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0.523599
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.349066
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.349066
        #=====
        actual_bone = 'Face'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.000"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.872665
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.523599
        #=====
        actual_bone = 'Arm_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.013"]
        #=====
        actual_bone = 'Forearm_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.015"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -2.53073
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = -0.191986
        #=====
        actual_bone = 'Arm_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.014"]
        #=====
        actual_bone = 'Forearm_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.016"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = False
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = False
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0.191986
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 2.53073
        #=====
        actual_bone = 'Thigh_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.025"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -1.76278
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 1.3439
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.785398
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.174533
        #=====
        actual_bone = 'Leg_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.027"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = 0.0698132
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 2.0944
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0
        #=====
        actual_bone = 'Foot_L'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.031"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.523599
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0
        #=====
        actual_bone = 'Thigh_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.026"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -1.76278
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 1.3439
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = -0.174533
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0.785398

        actual_bone = 'Leg_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.028"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = 0.0698132
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 2.0944
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0

        actual_bone = 'Foot_R'
        obs[len(obs)-1].data.bones.active = obs[len(obs)-1].pose.bones[actual_bone].bone
        obs[len(obs)-1].pose.bones[actual_bone].bone.select = True
        bpy.ops.pose.constraint_add(type='DAMPED_TRACK')
        bpy.context.object.pose.bones[actual_bone].constraints[0].target = bpy.data.objects["Point.032"]
        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[actual_bone].constraints[1].owner_space = 'LOCAL'
        #x
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_x = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_x = -0.523599
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_x = 0.523599
        #y
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_y = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_y = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_y = 0
        #z
        bpy.context.object.pose.bones[actual_bone].constraints[1].use_limit_z = True
        bpy.context.object.pose.bones[actual_bone].constraints[1].min_z = 0
        bpy.context.object.pose.bones[actual_bone].constraints[1].max_z = 0

        # frames = len(get_video_frames(path))

        # bpy.context.scene.frame_end = frames

        # bpy.ops.nla.bake(frame_start=1, frame_end=frames, visual_keying=True, clear_constraints=True, clear_parents=True, bake_types={'POSE'})
        bpy.ops.object.mode_set(mode='OBJECT')



        #apagar collection points criada
        # collection = bpy.data.collections.get('Point')
        # #
        # for obj in collection.objects:
        #     bpy.data.objects.remove(obj, do_unlink=True)
        # bpy.data.collections.remove(collection)

        sk_value_prop = context.scene.sk_value_prop
        
        return{'FINISHED'}


# class Mediapipe_Pose_estimation_RT(Operator, ImportHelper):
class Mediapipe_Pose_estimation_RT(Operator):
    bl_idname = "mocap.mediapipe_pose_rt"
    bl_label = "Generate Pose using MediaPipe RealTime"
    bl_description = "Generate Mocap data with MediaPipe RealTime, you have to use separated script running outside Blender"


    import bpy
    import socket
    import json
    from datetime import datetime
    from mathutils import Vector
    import math

    

    
    
    ##################################
    #### Starting modal to get media pipe realtime
    ##################################

    _timer = None
    _s = None
    _frame = None
    

    def modal(self, context, event):
        socket_buffer = context.scene.sk_value_prop.sk_socket_buffer
        record_bool = context.scene.sk_value_prop.sk_record_bool
        # record_frame_start = context.scene.sk_value_prop.sk_record_frame_start


        import socket
        from mathutils import Vector
        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.connect((socket.gethostname(), 1234)) #gethostname is the local address,
        
        HEADERSIZE = 10

        
        if event.type in {'RIGHTMOUSE', 'ESC'}:
            self.cancel(context)
            return {'CANCELLED'}

        if event.type == 'TIMER':
            #############
            #begin of connection code
            full_msg = b''
            nem_msg = True
            while True:
                # msg = self._s.recv(1024) #1024 is the buffer
                msg = self._s.recv(socket_buffer) 
                if nem_msg:
                    # self._frame = self._frame + 1
                    print(f"new message length: {msg[:HEADERSIZE]}")
                    msglen = int(msg[:HEADERSIZE])
                    nem_msg = False

                full_msg += msg

                if len(full_msg)-HEADERSIZE >= msglen:

                    d = json.loads(full_msg[HEADERSIZE:].decode('utf-8'))

                    nem_msg = True
                    full_msg = b''
                    break

        # print('fim: ',d)
            if d != 'nada':
                # print('len d[0]: ', len(d[0]))
                print('Frame:',self._frame,'bone: ',d[1][0],' x: ',d[1][1],' y: ',d[1][2],' z: ',d[1][3])
                for i in range(len(d)):
                    x_pose = d[i][1]
                    y_pose = d[i][2]
                    z_pose = d[i][3]
                    bpy.data.objects["Point."+str(1000+i)[1:]].location[0]=x_pose
                    bpy.data.objects["Point."+str(1000+i)[1:]].location[1]=y_pose
                    bpy.data.objects["Point."+str(1000+i)[1:]].location[2]=z_pose
                    if i == 10:
                    #    middle_point('Point.009','Point.010','Point.033')
                        bpy.ops.object.select_all(action='DESELECT')
                        bpy.data.objects['Point.009'].select_set(True)
                        bpy.data.objects['Point.010'].select_set(True)
                        bpy.context.view_layer.objects.active = bpy.data.objects['Point.010']
                        obs = bpy.context.selected_objects
                        n = len(obs)
                        assert(n)
                        bpy.data.objects['Point.033'].location = sum([o.matrix_world.translation for o in obs], Vector()) / n
                        if record_bool == True:
                            bpy.data.objects["Point."+str(1000+33)[1:]].keyframe_insert(data_path="location", frame=self._frame)
                    if i == 12:
                        # middle_point('Point.011','Point.012','Point.034')
                        bpy.ops.object.select_all(action='DESELECT')
                        bpy.data.objects['Point.011'].select_set(True)
                        bpy.data.objects['Point.012'].select_set(True)
                        bpy.context.view_layer.objects.active = bpy.data.objects['Point.012']
                        obs = bpy.context.selected_objects
                        n = len(obs)
                        assert(n)
                        bpy.data.objects['Point.034'].location = sum([o.matrix_world.translation for o in obs], Vector()) / n
                        if record_bool == True:
                            bpy.data.objects["Point."+str(1000+34)[1:]].keyframe_insert(data_path="location", frame=self._frame)
                    if i == 24:
                        # middle_point('Point.023','Point.024','Point.035')
                        bpy.ops.object.select_all(action='DESELECT')
                        bpy.data.objects['Point.023'].select_set(True)
                        bpy.data.objects['Point.024'].select_set(True)
                        bpy.context.view_layer.objects.active = bpy.data.objects['Point.024']
                        obs = bpy.context.selected_objects
                        n = len(obs)
                        assert(n)
                        bpy.data.objects['Point.035'].location = sum([o.matrix_world.translation for o in obs], Vector()) / n
                        if record_bool == True:
                            bpy.data.objects["Point."+str(1000+35)[1:]].keyframe_insert(data_path="location", frame=self._frame)
                    if record_bool == True:
                        bpy.data.objects["Point."+str(1000+i)[1:]].keyframe_insert(data_path="location", frame=self._frame)
            self._frame = self._frame + 1

            #end connection code
        return {'PASS_THROUGH'}

    def execute(self, context):
        import socket
        import bpy

        refresh_rate = context.scene.sk_value_prop.sk_refresh_rate
        self._frame = context.scene.sk_value_prop.sk_record_frame_start

       
        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._s.connect((socket.gethostname(), 1234)) #gethostname is the local address,

        name_points = 'Point'
        
        #===========
        # selectign Scene Collection

        multiplier = 0.9

        scene_collection = bpy.context.view_layer.layer_collection
        bpy.context.view_layer.active_layer_collection = scene_collection

        wm = context.window_manager
        # self._timer = wm.event_timer_add(0.1, window=context.window)
        self._timer = wm.event_timer_add(refresh_rate, window=context.window)
        
        wm.modal_handler_add(self)
        print('MODAL!!!!!!!!!!!!!!!')
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)


class Reload_sk_Mediapipe(Operator):

    bl_idname = "mocap.import_mediapipe_reload"
    bl_label = "Reload Skeleton Easymocap"
    bl_description = "Reload SK EasyMOCAP"

    def execute(self,context):

        bpy.ops.object.mode_set(mode='OBJECT')
        multiplier = context.scene.sk_value_prop.sk_value

        

        unit = skeleton_import.size_ref_bone('Point.001','Point.008','Point.008')
        unit = unit*multiplier

        spine_multi = context.scene.sk_value_prop.sk_spine_mulitplier
        neck_multi = context.scene.sk_value_prop.sk_neck_mulitplier
        head_multi = context.scene.sk_value_prop.sk_head_mulitplier

        forearm_multi = context.scene.sk_value_prop.sk_forearm_mulitplier
        arm_multi = context.scene.sk_value_prop.sk_arm_mulitplier

        tigh_multi = context.scene.sk_value_prop.sk_tigh_mulitplier
        leg_multi = context.scene.sk_value_prop.sk_leg_mulitplier
        foot_multi = context.scene.sk_value_prop.sk_foot_mulitplier

        root_sz    =unit/10
        spine_sz   =unit*3.5*spine_multi
        neck_sz    =unit*neck_multi
        face_sz    =unit*head_multi
        thigh_sz    =unit*3*tigh_multi
        leg_sz     =unit*2.5*leg_multi
        foot_sz    =unit*foot_multi #inclinado 45 graud pra frente
        arm_sz     =unit*1.5*arm_multi
        forearm_sz =unit*1.5*forearm_multi

        skeleton_import.size_of_bones(unit, root_sz, spine_sz, neck_sz, face_sz, thigh_sz, leg_sz, foot_sz, arm_sz, forearm_sz)

        return{'FINISHED'}
classes = (Import_Data_easymocap, Test_PT_Panel, OT_TestOpenFilebrowser,Import_Data_frankmocap,Import_Data_vibe,Mediapipe_Pose_estimation,
            Install_Mediapipe,Install_Joblib,MySettings,Modify_PT_Panel,Install_PT_Panel,Convert_axis,Reset_location,Reset_rotation,Foot_high,Compensate_Rotation,Smooth_Bone,Mediapipe_Pose_estimation_RT,Mediapipe_Pose_Prepare_Skeleton_RT, 
            Reload_sk_Mediapipe, Debug_PT_Panel)

# register, unregister = bpy.utils.register_classes_factory(classes)
def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    # bpy.types.Scene.my_tool = PointerProperty(type=MySettings)
    bpy.types.Scene.sk_value_prop = PointerProperty(type=MySettings)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls) 
    del bpy.types.Scene.sk_value_prop




if __name__ == "__main__":
    register()