import time
import re
import requests
import pyautogui
import pytesseract 

target= ["","",""]

def Setting():
  print("#Setting#")
  target[0] = input("TARGET1:")
  target[1] = input("TARGET2:")
  target[2] = input("TARGET3:")
  while(1):
    input_num = int(input("輸入要求數量(1 ~ 3):"))
    if input_num>0 and input_num<4:
      return input_num
      break
    else:
      print("重新輸入")
  print("#輸入成功#")

target_num = Setting()
print("目標1:",target[0],"\n目標2:",target[1],"\n目標3:",target[2],"\n要求數量:",target_num)
while(1):
  startkey = input("輸入'start'開始執行程式:")
  if(startkey=="start"or startkey=="START"):
    print("開始執行程式")
    break
while(1):#執行比對迴圈
  time.sleep(1)
  img = pyautogui.screenshot(region=(400,225,200,100))#螢幕抓取(X軸,Y軸,寬,高)
  print("GRAB!")
  text = pytesseract.image_to_string(img, lang='eng')#圖像文字辨識(英文)
  text=text.replace(" ", "")#文字辨識資料處理(去除空格)
  print("-----------------")
  text=text.split()#文字辨識資料處理(分段)
  print(text)
  result=0
  if(len(text)>0):
    for x in range(0,len(text)):#字串比對
      if x>2:
        break
      else:
        if text[x] == target[x]:
          result+=1
    print("result=",result)
    if(result >= target_num):
      print("success!")
      my_data = {'content': '<@384722629539397633>完成'}#小見貨
    # 將資料加入 POST 請求中
      send = requests.post('https://discord.com/api/webhooks/943632618056990811/gBWDaudszvzMKkyHZ_7ppJzdcrT-fQRjMzQbe9owzecQTfCvMX0bIwABeEwaN4wf2MtL', data = my_data)
      break
    else:
      print("fail!")
      time.sleep(1)
      pyautogui.press('enter')#自動按下ENTER鍵
print("END!")
   


