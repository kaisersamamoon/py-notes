"""
print ("圆的计算")
print (   '1 ("通过半径计算")    2 ("通过面积计算")     3 ("通过周长计算")'   )
times = 1
while times < 1000:
   flyme = int( input ( "请选择你的模式:" ) )
   a ,b , c = 1, 2 , 3
   if flyme == a:
      banjin = input ( "请输入圆的半径r:" )
      ban = float (banjin)
      r = ban
      s = 3.14*( r * r )
      print ( "面积:" , s )
      c = r * 3.14 * 2
      print ( "周长:" , c )
   if flyme == b:
      mianji = input ( "请输入圆的面积s:" )
      ban = float (mianji)
      s = ban
      r = ( s / 3.14  )** 0.5
      print ( "半径:" , r )
      c = (( s / 3.14  )** 0.5 )*3.14 * 2
      print ("周长:" , c )
   if flyme == d:
      zhouchang = input ( "请输入圆的周长c:" )
      ban = float (zhouchang)
      c = ban
      r = ( c / 2 / 3.14 )
      print ( "半径:" , r )
      s = ( c / 2 / 3.14 ) * 3.14
      print ( "面积:" , s )

   """



print ("圆的计算")
times = 1
while times < 1000:
   print (   '1 ("通过半径计算")    2 ("通过面积计算")     3 ("通过周长计算")'   )
   flyme = int( input ( "请选择你的模式:" ) )
   a ,b , c = 1, 2 , 3
   if flyme == a:
      banjin = float (input ( "请输入圆的半径r:" ))
      r = banjin
      s = 3.14*( r * r )
      print ( "面积:" , s )
      c = r * 3.14 * 2
      print ( "周长:" , c )
   if flyme == b:
      mianji = float (input ( "请输入圆的面积s:" ))
      s = mianji
      r = ( s / 3.14  )** 0.5
      print ( "半径:" , r )
      c = (( s / 3.14  )** 0.5 )*3.14 * 2
      print ("周长:" , c )
   if flyme == c:
      zhouchang = float (input ( "请输入圆的周长c:" ))
      c = zhouchang
      r = ( c / 2  / 3.14 )
      print ( "半径:" , r )
      s = ( 3.14 * r**2 )
      print ( "面积:" , s )
   if flyme > 3 or flyme <1:
      print ( "选择错误，请重新输入：" )





