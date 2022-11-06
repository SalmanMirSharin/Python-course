
# Pyautogui Packeg:

# from platform import python_branch
# import pyautogui
# import time

# #pyautogui.alert('This is an alert box.')

# # im1 = pyautogui.screenshot()
# # im1.save('my_screenshot.png')
# time.sleep(5)
# for i in range(1,5):
#     if(i==1):
#         time.sleep(3)
#         pyautogui.write('Hey', interval=0.25)
#         pyautogui.press('enter')
#     elif(i==2):
#         time.sleep(3)
#         pyautogui.write('What are you doing', interval=0.25)
#         pyautogui.press('enter')      
#     elif(i==3):
#         time.sleep(3)
#         pyautogui.write('Now are you in your office!', interval=0.25)
#         pyautogui.press('enter')   

#     elif(i==4):
#         time.sleep(3)
#         pyautogui.write('How is going your work!', interval=0.25)
#         pyautogui.press('enter')   



#CV2 Packeg:

import cv2
from cv2 import imshow

cam = cv2.VideoCapture(0)
while True:
    _,fr = cam.read()
    imshow('My cam',fr)
    cv2.waitKey(1)
