import time
import requests
import pyautogui
import cv2
from cv2 import waitKey
import numpy as np

def Runout(input_user):#設定次數耗盡時的通知對象
  if(input_user==1):
    my_data = {'content': '<@384722629539397633>次數耗盡'}#小見貨
  elif(input_user==2):
    my_data = {'content': '<@395247987229458453>次數耗盡'}#小丙級
  elif(input_user==3):
    my_data = {'content': '<@564853163677581347>次數耗盡'}#小俊吉
  return my_data
    
def Setting():#設定執行條件
  print("*Setting*")
  print("----------------")
  while(1):#設定使用者
    print("選擇使用者(1 ~ 3):")
    print("(1):小見貨")
    print("(2):小丙級")
    print("(3):小俊吉")
    input_user = int(input())
    if input_user>0 and input_user<4:
      if(input_user==1):#依照使用者設定完成時DC通知對象
        my_data = {'content': '<@384722629539397633>完成'}#小見貨
        user='小見貨'
      elif(input_user==2):
        my_data = {'content': '<@395247987229458453>完成'}#小丙級
        user='小丙級'
      elif(input_user==3):
        my_data = {'content': '<@564853163677581347>完成'}#小俊吉
        user='小俊吉'
      break
    else:
      print("重新輸入")
  print("#完成#")
  print("----------------")
  while(1):#設定目標屬性
    print("選擇屬性(1 ~ 5):")
    print("(1):INT+12%")
    print("(2):LUK+12%")
    print("(3):STR+12%")
    print("(4):DEX+12%")
    print("(5):全屬性+9%")
    input_attributes = int(input())#!!!!!圖片資源待補!!!!!
    if input_attributes>0 and input_attributes<6:
      if(input_attributes==1):
        attributes="INT+12%"
        template=cv2.imread('int1.jpg', 0)
      elif(input_attributes==2):
        attributes="LUK+12%"
        template=cv2.imread('int.jpg', 0)
      elif(input_attributes==3):
        attributes="STR+12%"
        template=cv2.imread('int.jpg', 0)
      elif(input_attributes==4):
        attributes="DEX+12%"
        template=cv2.imread('int.jpg', 0)
      elif(input_attributes==5):
        attributes="全屬性+9%"
        template=cv2.imread('bossatk.jpg', 0)
      break
    else:
      print("重新輸入")
  print("#完成#")
  print("----------------")
  while(1):#設定須符合條件的潛能數量
    print("選擇條件數量(1 ~ 3):")
    input_quantity = int(input())
    if input_quantity>0 and input_quantity<4:
      break
    else:
      print("重新輸入")
  print("#完成#")
  print("----------------")
  while(1):#設定要執行的次數
    print("輸入執行次數(0以上):")
    input_times = int(input())
    if input_times>0:
      break
    else:
      print("重新輸入")
  print("#完成#")
  print("----------------")
  return user,input_user,attributes,input_quantity,template,my_data,input_times

def Comparison(template):#影像比對
  pyautogui.screenshot('src.jpg',region=(645,495,500,255))#螢幕抓取(X軸,Y軸,寬,高)
  img_rgb = cv2.imread('src.jpg')
  img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
  h, w = template.shape[:2]
  target=0
  # 归一化平方差匹配
  res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
  threshold = 0.9 #閥值設定
  # 这段代码后面会有解释
  loc = np.where(res >= threshold)  # 匹配程度大于80%的坐标y，x
  for pt in zip(*loc[::-1]): # *号表示可选参数
    right_bottom = (pt[0] + w, pt[1] + h)
    cv2.rectangle(img_rgb, pt, right_bottom, (0, 0, 255), 2)
    target+=1
  return target

#main_funtion開頭
user,input_user,attributes,target_num,template,my_data,times = Setting()#接收設定資料並顯示
print("*****設定*****","\n使用者:",user,"\n目標:",attributes,"\n符合條件數量:",target_num,"\n執行次數:",times,"\n**************")
while(1):
  print("確認資料正確(Y/N):")
  startkey = input()
  if(startkey.lower()=="y"):
    print("----------------")
    break
  elif(startkey.lower()=="n"):
    user,input_user,attributes,target_num,template,my_data,times = Setting()
    print("*****設定*****","\n使用者:",user,"\n目標:",attributes,"\n符合條件數量:",target_num,"\n執行次數:",times,"\n**************")

while(1):
  print("先關閉預覽視窗再輸入")
  print("確認圖片正確(Y/N):")
  pyautogui.screenshot('src.jpg',region=(645,495,500,255))#螢幕抓取(X軸,Y軸,寬,高)
  img_rgb = cv2.imread('src.jpg')
  cv2.imshow('result',img_rgb)
  cv2.setWindowProperty("result", cv2.WND_PROP_TOPMOST, 1)
  waitKey(0)
  startkey = input()
  if(startkey.lower()=="y"):
    print("開始執行程式！")
    print("----------------")
    break

while(1):#執行比對迴圈n
  if(times==0):
    my_data=Runout(input_user)
    send = requests.post('https://discord.com/api/webhooks/954026486225068042/RxV8oUWQfTgoFMFj-GKtFEqDpy7vgCeOCsFgUPrjITQmpSyL-KoCpYWrqoSQCKTb1Pd2',my_data)
    break
  time.sleep(1)
  result=Comparison(template)
  times-=1
  if(result >= target_num):
    print("SUCCESS!")
  # 將資料加入 POST 請求中
    send = requests.post('https://discord.com/api/webhooks/954026486225068042/RxV8oUWQfTgoFMFj-GKtFEqDpy7vgCeOCsFgUPrjITQmpSyL-KoCpYWrqoSQCKTb1Pd2',my_data)
    break
  else:#!!!!!補上滑鼠及鍵盤事件!!!!!
    pyautogui.click(x=645, y=495, clicks=2)
    pyautogui.press('enter')
    pyautogui.click(x=645, y=495, clicks=2)
    print("符合條件數:",result)
    print("FAIL!")
    print("剩餘次數:",times)
    print("----------------")
   


