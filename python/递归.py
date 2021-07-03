def fab(n):
   if n < 1:
      print ("输入有误！")
      return -1
   if n == 1 or n == 2:
      return 1
   else:
      return fab(n-1) + fab (n -2)
   
import sys
sys.setrecursionlimit(10000)
resulat = fab(100)
if resulat != -1:
   print ("总共有%d对小兔子出生"%resulat)
