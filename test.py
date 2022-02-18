import random
import cv2
import tkinter as tk
import numpy as np
from PIL import ImageFont,ImageDraw,Image

def Setting():
  window = tk.Tk()
  window.title('TEST')
  window.geometry("300x100+250+150")
  # 顯示文字
  label = tk.Label(window,text = '關閉此視窗開始執行\n***說明***\n按下任意按鍵刷新\n按ESC結束程式'#設定內容
  ,font=('',18)#設定字體
  ) 
  label.pack()
  window.mainloop()
output = [1,2,3]
Setting()
while(1):
  for x in range(0,3):
    randnum  = random.randint(1,7)
    if(randnum ==1):
      output[x]="int +12%"
    elif(randnum ==2):
      output[x]="str +12%"
    elif(randnum ==3):
      output[x]="dex +12%"
    elif(randnum ==4):
      output[x]="str +24"
    elif(randnum ==5):
      output[x]="最大爆擊率提升"
    elif(randnum ==6):
      output[x]="提升技能急速"
    elif(randnum ==7):
      output[x]="int +12"
  shape = (100, 200, 3) # y, x, RGB
  bk_img = np.full(shape,0).astype(np.uint8)
  fontpath = "/Users/chengyu/Downloads/simsun.ttc"
  font=ImageFont.truetype(fontpath,24)
  img_pil=Image.fromarray(bk_img)
  draw=ImageDraw.Draw(img_pil)
  draw.text((0,0),output[0],font=font,fill=(255,255,255))
  draw.text((0,33),output[1],font=font,fill=(255,255,255))
  draw.text((0,66),output[2],font=font,fill=(255,255,255))
  bk_img=np.array(img_pil)
  cv2.imshow("added",bk_img)
  cv2.moveWindow("added",400,200)
  key=cv2.waitKey(0)
  if(key==27):
    print("stop")
    break
cv2.destroyAllWindows()