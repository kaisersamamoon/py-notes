flyme = []
for i in range(1,1000): 
   temes = list( str(i) )#将i的值通过str()转换成字符串类型的变量，通过list()生成一个列表赋值给temes变量
   if i > 100 and ( int(temes[0] )**3 + int(temes [1]) **3 + int (temes [2]) **3 == int(i)):#两个判断，一：i 是否大于 100,二：依次调用temes[[1],[2],[3]]变量中的1,2,3,([1]**3，[2]**3，[3]**3)计算是否等于i
      flyme.append(i)
print ('1~1000内是水仙花的有')
print(flyme)

