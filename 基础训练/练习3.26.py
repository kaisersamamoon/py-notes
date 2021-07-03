'''
for i in range(1,10):
   i = int(i)
   for j in range(0,10):
      j =int(j)
      for k in range(0,10):
         k = int(k)
         if i*3 + j *3 +k*3 == i*100 +j*10 + k:
            
            print(i*100 +j*10 + k)


            k+=1

      j +=1
      i +=1
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)
'''
'''
m = int (input('请输入m的值：'))
n = int (input('请输入n的值：'))

nux_m = 1
for i  in range

for  i in range(1,n+1):
   nux_n *= i
   
nux_mn = 1
for i in range(1,m-n+1):
   nux_mn *= i
   
print("当m = %d,n = %d时，一共%d种方案"%(m,n,nux_m//(nux_n*nux_mn)))


def fac(num):
   
   result = 1
   for n in range(1,num+1):
      result *= n
   return result


m = int(input('请输入m的值：'))
n = int(input('请输入n的值:'))

print (fac(m) // (fac(n)*fac(m - n)))
'''
'''
def gcd(x,y):
   (y,x)= (x,y)if y > x else(y,x)
 
   for factor in range(y,1,-1):
      if x % factor ==0 and y % factor ==0:
         return factor
def lcm(x,y):
   return x*y//gcd(x,y)
x = int(input('x的值:'))
y = int(input('y的值:'))
print('最小公倍数为',gcd(x,y))
print('最大公倍数为',lcm(x,y))
'''
'''
def is_palindrome(num):
    """判断一个数是不是回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num
num = int(input('请输入一个数:'))
print(is_palindrome(num))

'''

'''
def foo():
    b = 'hello'

    # Python中可以在函数内部再定义函数
    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()
'''
'''
def foo():
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 100
'''
'''
s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello, 
world!
"""
print(s1, s2, s3, end='')
'''
'''
s1 = '\'hello,world!\''
s2 = '\n\\hello,world!\\\n'
print(s1,s2,end='')
'''
'''
s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1,s2)
'''

'''
s1 = r'\'hello,world!\''
s2 = r'\n\\hello,world!\\\n'
print(s1,s2,end=' ')
s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')
'''
'''
list1 = [1, 3, 5, 7, 100]
for index in range(len(list1)):
    print(list1[index])
print(list1)
'''
'''
list1 = [1, 3, 5, 7, 100]
for elem in list1:
   print(elem)
for index, elem in enumerate(list1):
    print(index, elem)

'''
'''
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True)#True为倒叙，默认为顺序
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list1)
print(list2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)#在原列表的基础上直接排序
print(list1)

'''
'''
f = [x for x in range(1, 10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
'''
'''
f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))  # 查看对象占用内存的字节数
print(f)
'''
'''
import sys
f = [x ** 2 for x in range(1, 1000)]print(f)
print(sys.getsizeof(f)) 
for val in f:
    print(val)
'''

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()


