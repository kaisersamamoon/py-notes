print ( " bmi指数计算 " )
while True:
     shenggao = float ( input ( "请输入你的身高m：" ) )
     tizhong = float ( input ( "请输入你的体重kg：" ) )
     BIM = tizhong / shenggao ** 2
     if BIM < 18.5:
          print ( "你的BIM为：" , BIM,   " 过轻 " )
     elif  18.5 < BIM < 25:
          print ( "你的BIM为：" , BIM,  " 正常 " )
     elif 25 < BIM < 28:
          print ("你的BIM为：" , BIM,   " 过重 " )
     elif 28 < BIM < 32:
          print ("你的BIM为：" , BIM,   " 肥胖 " )
     else:
          print ( "你的BIM为：" , BIM,  " 严重肥胖 " )

