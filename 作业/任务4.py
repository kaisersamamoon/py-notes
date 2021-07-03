
print ("圆的计算")
print (   '1 ("通过半径计算")    2 ("通过面积计算")     3 ("通过周长计算")'   )
times = 1
while times < 1000:
   characater = int( input ( "请选择你的模式:" ) )
   a = 1
   b = 2
   d = 3
   if characater == a:
      banjin = input ( "请输入圆的半径r:" )
      ban = float (banjin)
      r = ban
      s = 3.14*( r * r )
      print ( "面积:" , s )
      c = r * 3.14 * 2
      print ( "周长:" , c )
   if characater == b:
      mianji = input ( "请输入圆的面积s:" )
      ban = float (mianji)
      s = ban
      r = ( s / 3.14  )** 0.5
      print ( "半径:" , r )
      c = (( s / 3.14  )** 0.5 )*3.14 * 2
      print ("周长:" , c )
   if characater == d:
      zhouchang = input ( "请输入圆的周长c:" )
      ban = float (zhouchang)
      c = ban
      r = ( c / 2 / 3.14 )
      print ( "半径:" , r )
      s = ( c / 2 / 3.14 ) * 3.14
      print ( "面积:" , s )

   
