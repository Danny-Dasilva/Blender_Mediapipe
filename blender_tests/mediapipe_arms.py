import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
#Creating the connection to send the data
import socket
import pickle
import json
import time

from threading import Thread
import requests
import cv2
import numpy as np





HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4 and TCP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((socket.gethostname(), 1234))
s.listen(5)

clientsocket, address = s.accept()
print(f"Connection from {address} has ben estabilished!")



def android_cam():

  url = "http://192.168.1.244:8080/shot.jpg"
  while True:
      img_resp = requests.get(url)
      img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
      img = cv2.imdecode(img_arr, -1)

      scale_percent = 60 # percent of original size
      width = int(img.shape[1] * scale_percent / 100)
      height = int(img.shape[0] * scale_percent / 100)
      dim = (width, height)
      print(dim)
      # resize image
      resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
      

          
      return resized
      


def process_img(image, label):
  with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)

    # Draw landmark annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow(label, image)
    
    pose=''
    
    
    try:
      pose=results.multi_hand_landmarks[0].landmark
    except:
      pose=''
    return pose

# For webcam input:
cap = cv2.VideoCapture(0)

while cap.isOpened():
  success, image = cap.read()
  # if not success:
  #   print("Ignoring empty camera frame.")
  #   # If loading a video, use 'break' instead of 'continue'.
  #   continue

  
  img = android_cam()
  unused = process_img(img, 'Android Cam')
  pose = process_img(image, 'Physical Cam')
  #creating serialized variable to convert to json
  if isinstance(pose,str):
    msg = json.dumps('nada')
  elif not pose:
    msg = json.dumps('nada')
  else:
    pose_serialize=[]
    for i in range(len(pose)):

        x=pose[i].x
        y=pose[i].y
        z=pose[i].z
        type="A"
        pose_serialize.append([i,x,y,z, type])
    msg = json.dumps(pose_serialize)

  if isinstance(unused,str):
    msg2 = json.dumps('nada')
  elif not unused:
    msg2 = json.dumps('nada')
  else:
    pose_serialize=[]
    for i in range(len(unused)):

        x=unused[i].x
        y=unused[i].y
        z=unused[i].z
        type="B"
        pose_serialize.append([i,x,y,z, type])
    msg2 = json.dumps(pose_serialize)



  # print(msg)
  print('len: ',len(msg))
  print('len encode: ',len(msg.encode('utf-8')))
  # while True:
  msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg.encode('utf-8')
  clientsocket.send(msg)
  from time import sleep
  sleep(.01)

  print('len: ',len(msg2))
  print('len encode: ',len(msg2.encode('utf-8')))
  # while True:
  msg2 = bytes(f'{len(msg2):<{HEADERSIZE}}', "utf-8") + msg2.encode('utf-8')
  clientsocket.send(msg2)

  if cv2.waitKey(5) & 0xFF == 27:
    break


cap.release()


