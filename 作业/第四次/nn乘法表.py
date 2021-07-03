temes = int(input('请输入一个值：'))
dell = 1
if temes <=9:
   while dell <= temes:
      whilee = 1
      
      
      while whilee <= temes:
         pop = dell * whilee
         
         print('%d*%d=%d'%(dell,whilee,pop))
         whilee =whilee + 1
      print('\n')
      dell = dell + 1
   
else:
   
   print("输入错误，范围0~10，请重新输入")
   
