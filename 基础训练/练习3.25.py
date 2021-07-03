'''
num = 0
for i in range(1,1001):
   num += i
   
print(num)
'''
'''
num=0
for i in range(1000,0,-1):
   num +=i
print(num)
'''
'''
#猜数字游戏
import random
temes = random.randint(1,100)

dell = 1
while True:
   num = int(input('请输入数字:'))
   if 0<num<100:
      if temes == num:
         print('回答正确,你一共用了%s次'%(dell))
         continue
      if temes < num:
         print ('大了，大了')
      else :
         print('小了，小了')
      
      dell+=1
   else:
      print('输入错误，数字范围为0~100')
      break
'''
'''
#九九乘法表
for i in range(1,10):
   for j in range(1,i+1):
      print('%d*%d=%d'%(i,j,i*j),end='\t')
   print('\r')
'''

'''
num = int(input('请输入一个正整数：'))

is_prime = True
for x in range(2,num):
   if num % x ==0:
      
      is_prime = False
      break
if is_prime and num != 1:
   print('%d是素数'%num)
else:
   print('%d不是素数'%num)
   '''
'''
num = int(input('请输入一个正整数：'))
for i in range(2,num):
   dell = True
   if num % i != 0:
      dell = False
      break
if dell == False and num != 1:
   print(1)
else:
   print(2)
'''
'''
a = int(input('请输入第一个正整数;'))
b= int(input('请输入第二个正整数:'))
if a>b:
   a,b = b,a
else:
   for factor in range(a,0,-1):
      if a % factor== 0 and b % factor == 0:
         print('%d和 %d的最大公约数是%d'%(a,b,factor))
         print('%d 和 %d的最小公倍数是%d'%(a,b,a*b//factor))
         break
      '''
'''
row = int(input('请输入打印行数:'))
for i in range(row):
   for _ in range(i+1):
      print('*',end = ' ')
   print()

for i in range(1,6):
    print(("*"*(2*i-1)).rjust(5))
    '''
for i in range(5,0,-1):
   print(('*'*(2*i-1)).center(9))
