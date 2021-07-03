"""
x = float(input("请输入x的值:"))
if x>1:
   y = (3*x)-5
elif -1<=x<=1:
   y =x+2
else:
   y = (5*x)+1
print('(%.2f) = (%.2f)'%(x,y))
"""
'''
value = float(input("请输入长度:"))
unit = input("请输入单位：")
if unit =='英寸':
   
   print("%d %s = %.5f %s"%(value,'英寸',value*2.54,'厘米' ))
elif unit =='英尺':
   print("%d %s = %.5f %s"%(value,'英尺',value*12*2.54,'厘米' ))
if unit =='英分':
   print("%d %s = %.5f %s"%(value,'英分',value*2.54/8,'厘米' ))
'''
'''
score = float(input('请输入分数:'))
if score >= 90:
   grade = 'A'
elif 80<= score < 90:
   grade = 'B'
elif 70<= score < 80:
   grade = 'C'
elif 60 <= score <70:
   grade = 'D'
else:
   grade = 'E'
print("你的成绩等级为%s"% grade)
'''
a = float (input("请输入一条边"))
b= float (input("请输入二条边"))
c= float (input("请输入三条边"))
if a+b>c and a+c>b and b+c >a:
   p = (a+b+c)/2
   s = (p*(p-a)*(p-b)*(p-c))**0.5
   print('面积为: %s,周长为:%.2f'%(s,a+b+c))
else:
   print('输入错误')
   
