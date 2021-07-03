class mycalc :
   "mycalc class"
   def __init__(self,a,b):
      self.a=a
      self.b=b
   def addition ( self ,Retain ):
      return round( self.a + self.b,Retain )
   def subtraction ( self ,Retain ):
      return round( self.a - self.b,Retain )
   def multiplication ( self ,Retain ):
      return round( self.a * self.b,Retain )
   def division ( self ,Retain ):
      return round ( self.a / self.b,Retain )
while True:
   get__num1 = input ( "请输入第一个数字:" ) 
   calculate =input ( " 请输入运算符号: " ) 
   get__num2 = input ( " 请输入第二个数字: " ) 
   get__retain =input ( " 请输入保留的小数: " )
   num1 = float ( get__num1 )
   num2 = float ( get__num2 )
   retain = int ( get__retain )
   if calculate =='+':
      temes = mycalc ( num1,num2 ).addition( retain )
   elif calculate=='-':
      temes = mycalc ( num1,num2 ).subtraction ( retain )
   elif calculate =='*':
      temes = mycalc ( num1 ,num2 ).multiplication( retain )
   elif calculate =='/':
      if num2 == 0:
         print ("输入错误，分母不能为零")
         continue
      else:
         temes = mycalc ( num1 ,num2 ).division ( retain )
   elif calculate != ['+','-','*','/']:
       print ( " 运算符号错误，请重新输入 " )
       continue
   print ("  计算结果为: ",temes )
