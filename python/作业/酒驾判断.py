print ( " 酒驾判断 " )

while True:
     hanliang = int ( input ( "请输入驾驶员酒驾含量:  " )  )
     if hanliang < 20 :
          print ( "驾驶员不构成酒驾" )
     elif 20 < hanliang < 80 :
          print ( " 酒驾 " )
     else :
          print ( " 醉驾 " )
