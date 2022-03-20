import time
from turtle import width
import requests
import pyautogui
import cv2
from cv2 import waitKey
import numpy as np
src_width=460
src_length=200
screenshot_x=800
screenshot_y=500
click_x=800
click_y=500
###################################################################################
def Runout(input_user):#設定次數耗盡時的通知對象
  if(input_user==1):
    my_data = {'content': '<@384722629539397633>次數耗盡'}#小見貨
  elif(input_user==2):
    my_data = {'content': '<@395247987229458453>次數耗盡'}#小丙級
  elif(input_user==3):
    my_data = {'content': '<@564853163677581347>次數耗盡'}#小俊吉
  return my_data
###################################################################################
def TargetArraySetting():
  while(1):
    print("*****目標設定*****")
    print("設定目標數量(1~20):")
    Quantity=int(input())
    if(Quantity>0 and Quantity<21):
      break
    else:
      print("輸入錯誤")
      print("重新輸入\n")
  targetQuantity=np.zeros(Quantity,dtype=int)
  print("---------------------")
  for i in range (0,Quantity):
    while(1):
      print("目標",i+1,"涵蓋潛能數量(1~2):")
      targetQuantity[i]=int(input())
      if(targetQuantity[i]>0 and targetQuantity[i]<3):
        print("---------------------")
        break
      else:
        print("輸入錯誤")
        print("重新輸入\n")
  targetArray=np.zeros((Quantity,2,2),dtype=int)
  for i in range (0,Quantity):
    for j in range (0,targetQuantity[i]):
      print("<設定目標",i+1,"潛能(共",targetQuantity[i],"項)>")
      print("+-------------+")
      print("|(1)INT+12%   |")
      print("|(2)STR+12%   |")
      print("|(3)DEX+12%   |")
      print("|(4)LUK+12%   |")
      print("|(5)全屬+9%   |")
      print("|(6)掉寶++    |")
      print("|(7)掉幣++    |")
      print("|(8)物功++    |")
      print("|(9)魔功++    |")
      print("|(10)B傷++    |")
      print("|(11)B防++    |")
      print("+-------------+")
      while(1):
        print("選擇目標",i+1,"第",j+1,"項屬性(1~11):")
        targetArray[i][j][0]=int(input())
        if(targetArray[i][j][0]>0 and targetArray[i][j][0]<12):
          break
        else:
          print("輸入錯誤")
          print("重新輸入\n")
      while(1):
        print("設定目標",i+1,"第",j+1,"項門檻值(1~3)")
        targetArray[i][j][1]=int(input())
        if(targetArray[i][j][1]>0 and targetArray[i][j][1]<4):
          print("=============================")
          break
        else:
          print("輸入錯誤")
          print("重新輸入\n")
  for i in range (0,len(targetQuantity)):
    print("目標",i+1,"涵蓋潛能數量:",targetQuantity[i])
  print("=============================")
  for i in range (0,len(targetQuantity)):
    print("****************************************")
    for j in range (0,targetQuantity[i]):
      if(targetArray[i][j][0]==1):
        print("目標",i+1,"第",j+1,"項屬性及門檻值: INT+12% ,",targetArray[i][j][1])
      elif(targetArray[i][j][0]==2):
        print("目標",i+1,"第",j+1,"項屬性及門檻值: STR+12% ,",targetArray[i][j][1])
      elif(targetArray[i][j][0]==3):
        print("目標",i+1,"第",j+1,"項屬性及門檻值: DEX+12% ,",targetArray[i][j][1])
      elif(targetArray[i][j][0]==4):
        print("目標",i+1,"第",j+1,"項屬性及門檻值: LUK+12% ,",targetArray[i][j][1])
      elif(targetArray[i][j][0]==5):
        print("目標",i+1,"第",j+1,"項屬性及門檻值: 全屬+9% ,",targetArray[i][j][1])
      elif(targetArray[i][j][0]==6):
        print("目標",i+1,"第",j+1,"項屬性及門檻值: 掉寶++ ,",targetArray[i][j][1])
      elif(targetArray[i][j][0]==7):
        print("目標",i+1,"第",j+1,"項屬性及門檻值: 掉幣++ ,",targetArray[i][j][1])
      elif(targetArray[i][j][0]==8):
        print("目標",i+1,"第",j+1,"項屬性及門檻值: 物功++ ,",targetArray[i][j][1])
      elif(targetArray[i][j][0]==9):
        print("目標",i+1,"第",j+1,"項屬性及門檻值: 魔功++ ,",targetArray[i][j][1])
      elif(targetArray[i][j][0]==10):
        print("目標",i+1,"第",j+1,"項屬性及門檻值: B傷++ ,",targetArray[i][j][1])
      elif(targetArray[i][j][0]==11):
        print("目標",i+1,"第",j+1,"項屬性及門檻值: B防++ ,",targetArray[i][j][1])
  print("****************************************")
  return Quantity,targetQuantity,targetArray
###################################################################################
def Setting():#設定執行條件
  print("***設定基本資料***")
  print("------------------")
  while(1):#設定使用者
    print("選擇使用者(1 ~ 3):")
    print("(1)小見貨")
    print("(2)小丙級")
    print("(3)小俊吉")
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
      print("輸入錯誤")
      print("重新輸入\n")
  print("#完成#")
  print("------------------")
  while(1):#設定要執行的次數
    print("輸入執行次數(0以上):")
    input_times = int(input())
    if input_times>0:
      break
    else:
      print("輸入錯誤")
      print("重新輸入\n")
  print("#完成#")
  print("------------------")
  return user,input_user,my_data,input_times
###################################################################################
def Comparison(Attributes,Threshold):#影像比對
  if(Attributes==1):
    template=cv2.imread("int.jpg",0)
  elif(Attributes==2):
    template=cv2.imread("str.jpg",0)
  elif(Attributes==3):
    template=cv2.imread("dex.jpg",0)
  elif(Attributes==4):
    template=cv2.imread("luk.jpg",0)
  elif(Attributes==5):
    template=cv2.imread("all.jpg",0)
  elif(Attributes==6):
    template=cv2.imread("treasure.jpg",0)
  elif(Attributes==7):
    template=cv2.imread("gold.jpg",0)
  elif(Attributes==8):
    template=cv2.imread("ad.jpg",0)
  elif(Attributes==9):
    template=cv2.imread("ap.jpg",0)
  elif(Attributes==10):
    template=cv2.imread("bossatk.jpg",0)
  elif(Attributes==11):
    template=cv2.imread("bossdef.jpg",0)
  pyautogui.screenshot('src.jpg',region=(screenshot_x,screenshot_y,src_width,src_length))#螢幕抓取(X軸,Y軸,寬,高)
  img_rgb = cv2.imread('src.jpg')
  img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
  h, w = template.shape[:2]
  taken=0
  # 归一化平方差匹配
  res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
  com_threshold = 0.9 #閥值設定
  # 这段代码后面会有解释
  loc = np.where(res >= com_threshold)  # 匹配程度大于80%的坐标y，x
  for pt in zip(*loc[::-1]): # *号表示可选参数
    right_bottom = (pt[0] + w, pt[1] + h)
    cv2.rectangle(img_rgb, pt, right_bottom, (0, 0, 255), 2)
    taken+=1
  if(taken>=Threshold):
    return 1
  else:
    return 0
###################################################################################

####MAIN_Funtion開頭####
user,input_user,my_data,input_times = Setting()#接收設定資料並顯示
print("***基本資料參數***","\n使用者:",user,"\n執行次數:",input_times,"\n******************")
while(1):
  print("確認資料正確(Y/N):")
  startkey = input()
  if(startkey.lower()=="y"):
    print("----------------")
    break
  elif(startkey.lower()=="n"):
    user,input_user,my_data,input_times = Setting()
    print("***基本資料參數***","\n使用者:",user,"\n執行次數:",input_times,"\n******************")

while(1):
  #設定目標參數
  Quantity,targetQuantity,targetArray=TargetArraySetting()
  print("確認目標資料正確(Y/N):")
  startkey = input()
  if(startkey.lower()=="y"):
    print("----------------")
    break

while(1):
  print("先關閉預覽視窗再輸入")
  print("確認圖片正確(Y/N):")
  pyautogui.screenshot('src.jpg',region=(screenshot_x,screenshot_y,src_width,src_length))#螢幕抓取(X軸,Y軸,寬,高)
  img_rgb = cv2.imread('src.jpg')
  cv2.imshow('preview',img_rgb)
  cv2.setWindowProperty("preview", cv2.WND_PROP_TOPMOST, 1)
  waitKey(0)
  startkey = input()
  if(startkey.lower()=="y"):
    print("開始執行程式！")
    print("----------------")
    break

while(1):#執行比對迴圈n
  if(input_times==0):
    my_data=Runout(input_user)
    #傳送次數用盡通知
    send = requests.post('https://discord.com/api/webhooks/954026486225068042/RxV8oUWQfTgoFMFj-GKtFEqDpy7vgCeOCsFgUPrjITQmpSyL-KoCpYWrqoSQCKTb1Pd2',my_data)
    break
  for i in range(0,Quantity):
    compare_flag=0
    for j in range(0,targetQuantity[i]):
      conform_num=0
      conform_num+=Comparison(targetArray[i][j][0],targetArray[i][j][1])
      if(conform_num==targetQuantity[i]):
        print("完成目標:",i+1)
        compare_flag=1
        break
      else:
        compare_flag=0
    if(compare_flag==1):
      break
  input_times-=1 #執行次數-1
  if(compare_flag==1):
    print("SUCCESS!")
    #傳送成功通知
    send = requests.post('https://discord.com/api/webhooks/954026486225068042/RxV8oUWQfTgoFMFj-GKtFEqDpy7vgCeOCsFgUPrjITQmpSyL-KoCpYWrqoSQCKTb1Pd2',my_data)
    break
  else:
    pyautogui.click(click_x, click_y, clicks=2)
    pyautogui.press('enter')
    time.sleep(0.3)
    pyautogui.click(click_x, click_y, clicks=2)
    print("FAIL!")
    print("剩餘次數:",input_times)
    print("----------------")
