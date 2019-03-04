import vrep 
import math
import sys
import tkinter

    ########################################################################################################
# For the connection  ...
    
def dis_connect():
    vrep.simxFinish(-1) # just in case, close all opened connections 
    print ("dis connected")
    
def connect():
    vrep.simxFinish(-1) # just in case, close all opened connections 
    clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # start a connection 
    if clientID!=-1: 
        print ("Connected to remote API server") 
    else: 
        print("Not connected to remote API server") 
        sys.exit("Could not connect")
    
    ########################################################################################################
# To Handle the 6 joints ...
    
    err_code1,l_motor_handle1 = vrep.simxGetObjectHandle(clientID,"P_Arm_joint1", vrep.simx_opmode_blocking)
    err_code2,l_motor_handle2 = vrep.simxGetObjectHandle(clientID,"P_Arm_joint2", vrep.simx_opmode_blocking)
    err_code3,l_motor_handle3 = vrep.simxGetObjectHandle(clientID,"P_Arm_joint3", vrep.simx_opmode_blocking)
    err_code4,l_motor_handle4 = vrep.simxGetObjectHandle(clientID,"P_Arm_joint4", vrep.simx_opmode_blocking)
    err_code5,l_motor_handle5 = vrep.simxGetObjectHandle(clientID,"P_Arm_joint5", vrep.simx_opmode_blocking)
    err_code6,l_motor_handle6 = vrep.simxGetObjectHandle(clientID,"P_Arm_joint6", vrep.simx_opmode_blocking)
    
    ########################################################################################################
# To make the sliders values  synchronized to the current manipulator joints values
    
    m1=vrep.simxGetJointPosition(clientID,l_motor_handle1, vrep.simx_opmode_blocking);
    m2=vrep.simxGetJointPosition(clientID,l_motor_handle2, vrep.simx_opmode_blocking);
    m3=vrep.simxGetJointPosition(clientID,l_motor_handle3, vrep.simx_opmode_blocking);
    m4=vrep.simxGetJointPosition(clientID,l_motor_handle4, vrep.simx_opmode_blocking);
    m5=vrep.simxGetJointPosition(clientID,l_motor_handle5, vrep.simx_opmode_blocking);
    m6=vrep.simxGetJointPosition(clientID,l_motor_handle6, vrep.simx_opmode_blocking);
     
    w[0].set(m1[1]*180/math.pi)
    w[1].set(m2[1]*180/math.pi)
    w[2].set(m3[1]*180/math.pi)
    w[3].set(m4[1]*180/math.pi)
    w[4].set(m5[1]*180/math.pi)
    w[5].set(m6[1]*180/math.pi)
    
    while(1):
        targetPos1=[w[0].get()*math.pi/180,w[1].get()*math.pi/180,w[2].get()*math.pi/180,w[3].get()*math.pi/180,w[4].get()*math.pi/180,w[5].get()*math.pi/180]
        vrep.simxSetJointTargetPosition(clientID, l_motor_handle1, targetPos1[0],  vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID, l_motor_handle2, targetPos1[1],  vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID, l_motor_handle3, targetPos1[2],  vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID, l_motor_handle4, targetPos1[3],  vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID, l_motor_handle5, targetPos1[4],  vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID, l_motor_handle6, targetPos1[5],  vrep.simx_opmode_streaming)
        
        master.update_idletasks()
        master.update()
        
    ########################################################################################################
# Sliders & It is  properties ...
    
master = tkinter.Tk()
w = [0,0,0,0,0,0]
w[0] = tkinter.Scale(master, from_=-180, to=180, orient=tkinter.VERTICAL)
w[0].pack(side=tkinter.LEFT)
w[1] = tkinter.Scale(master, from_=-180, to=180, orient=tkinter.VERTICAL)
w[1].pack(side=tkinter.LEFT)
w[2] = tkinter.Scale(master, from_=-180, to=180, orient=tkinter.VERTICAL)
w[2].pack(side=tkinter.LEFT)
w[3] = tkinter.Scale(master, from_=-180, to=180, orient=tkinter.VERTICAL)
w[3].pack(side=tkinter.LEFT)
w[4] = tkinter.Scale(master, from_=-180, to=180, orient=tkinter.VERTICAL)
w[4].pack(side=tkinter.LEFT)
w[5] = tkinter.Scale(master, from_=-180, to=180, orient=tkinter.VERTICAL)
w[5].pack(side=tkinter.LEFT)

    ########################################################################################################
# Connect & Disconnect Buttons ...
    
con = tkinter.Button(master, text="Connect", command=connect)
con.pack(side=tkinter.TOP )

dis_con = tkinter.Button(master, text="Disconnect", command=dis_connect)
dis_con.pack(side=tkinter.BOTTOM )

    ########################################################################################################
    
master.mainloop()
