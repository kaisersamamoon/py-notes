import random
temes = random.randint ( 1,10 )
i = 6
print ("游戏开始")
print ("本次游戏数字1-10，你有六次机会")
while i != 0 :
   digital = int (input (" 请输入一个数字： "))
   if 0 < digital < 10:
         
      if int(temes) < digital:
         print ("大了，大了")
      elif int(temes) > digital:
         print ( "小了，小了" )
      
      else:
         print ("回答正确")
         break
      i = i - 1
      print ("你还剩余",int (i),"机会")
   else:
      print ('错误输入')
print("游戏结束")
   
   
   
