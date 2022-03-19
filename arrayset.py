import numpy as np
print("*****目標設定*****")
print("設定目標數量(1~20):")
while(1):
  Quantity=int(input())
  if(Quantity>0 and Quantity<21):
    break
  else:
    print("輸入錯誤")
targetQuantity=np.zeros(Quantity,dtype=int)
print("---------------------")
for i in range (0,Quantity):
  while(1):
    print("目標",i+1,"潛能數量(1~2):")
    targetQuantity[i]=int(input())
    if(targetQuantity[i]>0 and targetQuantity[i]<3):
      break
    else:
      print("輸入錯誤")
print("---------------------")
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
    print("+-------------+")
    while(1):
      print("選擇目標",i+1,"第",j+1,"項屬性(1~7):")
      targetArray[i][j][0]=int(input())
      if(targetArray[i][j][0]>0 and targetArray[i][j][0]<8):
        break
      else:
        print("輸入錯誤")
    while(1):
      print("設定目標",i+1,"第",j+1,"項門檻值(1~3)")
      targetArray[i][j][1]=int(input())
      if(targetArray[i][j][1]>0 and targetArray[i][j][1]<4):
        break
      else:
        print("輸入錯誤")
print("---------------------")
for i in range (0,len(targetQuantity)):
  print("目標",i+1,"潛能數量:",targetQuantity[i])
print("---------------------")
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
print("****************************************")