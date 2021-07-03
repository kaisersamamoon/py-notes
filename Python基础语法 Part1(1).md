# 第一章 Python基础语法

## 1.1 Python的介绍和安装

### 1.1.1 编程语言的分层

机器语言：直接和硬件打交道，01代码，控制硬件功能。但对于人太难记忆和理解了。

汇编语言（嵌入式开发用到）：用英语来表示01代码初步。但是开发效率不够高效，比如写一个Hello world需要十几行代码。

高级语言（如C、Java、Python等）：对底层硬件的指令做了封装，可以使调用功能的代码大大简化，提高开发效率。

### 1.1.2 安装

[Python环境与Pycharm的安装](https://blog.csdn.net/Ans_min/article/details/104102046)

## 1.2 变量、常量和注释

### 1.2.1 变量

变量使用的规则：

1. 先定义变量，变量存储在内存里；
2. 后面的代码来调用。

```python
x = 2
y = 3
print(x+y)	# 输出5
```

### 1.2.2 变量名的定义

1. 变量名只能是字母、数字或下划线的任意组合；
2. 变量名的第一个字符不能是数字；
3. 以下关键字不能声明为变量名`['and', 'as', 'assert', "break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'globall', 'if', 'import', "in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']`；
4. 特殊字符不能包含在变量名内。

### 1.2.3 变量名的规范

变量名违反1.2.2的定义就会报错，但是变量名还应该保持一致的格式，培养良好的编程习惯。一般有两种规范：`age_of_person = 23`，`NumberOfStudents = 80`。

个人习惯第一种，也是Python官方的推荐规范，第二种自己喜欢在Java里面用。

其他规范还有：

- 变量名也不应该用汉字或者拼音，别人看会比较蠢。。。

- 变量名也不能太长，也不要词不达意，要方便理解

### 1.2.4 变量的修改

```python
name = 'zm'
print(name)
name = 'new_zm'	# 变量的修改
print(name)
```

### 1.2.5 常量

Python没有常量的语法，所以大家通过全部大写的数据来表示常量，方便告诉别的程序员这是一个常量，比如`SYSTEM_NAME = 'XXX系统'`

### 1.2.6 注释

```python
# 单行注释 一般#后加一个空格，符合规范
"""
三个双引号可以
多行注释
Python官方推荐
"""
'''
三个单引号也可以
多行注释
不推荐
'''

# 注释的代码不执行
```

## 1.3 基本数据类型

### 1.3.1 查看数据类型

```python
# type可以查看数据的类型
name = 'zm'
age = 18
print(type(name))
print(type(age))
```

### 1.3.2 字符串和数字

#### 数字(int/float)

数字包括类型有：

- int 整数 最大储存 2^62^
  - long 无限大（很多亿） Python3里去掉了，所有整数都按int类型处理
- float 浮点数
- 复数（比较少用，不介绍）

#### 字符串(str)

定义：

有引号的就是字符串。比如`name = 'zm'`，这里的`name`就是字符串类型的数据。Python中单引号双引号三引号都可以用来表示字符串，其中三引号可以表示多行的字符串，我们放在段落里讲（单引号和双引号可以通过`\n`来实现）

拼接：

```python
name1 = 'zm'
name2 = 'lalala'
print(name1 + name2)	# 实现字符拼接输出zmlalala
print(name1*3)	# 打印三遍name1
```

段落：

三引号可以写多行字符。

```python
name = '''
zm
wzw
yz
'''
print(name)		# 输出多行数据
```

### 1.3.3 布尔(bool)

若`a = 3`，`b = 5`，则可以得到`b > a`。计算机描述`b > a`是通过布尔类型来描述，布尔类型有两种：`True`和`False`。比如`a = 3; b = 5; print(a<b)`，输出的结果就为`True`。布尔类型在`if`语句中经常搭配使用。

### 1.3.4 列表

列表的作用：一个存多个数据，而且方便取其中的某个或某些数据。

```python
names = ['zm', 'wzw', 'yz']
print(type(names))		# 输出list类型
print(names[0])		# 输出zm
print(names[2])		# 输出yz
```

列表里每个数据被称作元素，元素之间以逗号隔开，取值时根据下标取即可。关于下标（又称索引），就是列表自带的一个东西，默认给每个元素按顺序从0开始给下标。比如上面的代码中，`'zm'`的下标是0，`'wzw'`的下标是1，以此类推。

#### 列表的增

```python
# 插入
names = ['zm', 'wzw', 'yz']
# names.insert(位置, 插入元素)
names.insert(1, 'zk')	# 插入到位置1，原位置1以及后面的元素向后移
print(names)	# 输出的是['zm', 'zk', 'wzw', 'yz']
```

```python
# 追加（插入无法将数据放在列表的最后面，append就可以）
names = ['zm', 'wzw', 'yz']
names.append('zk')	# append只能加在列表的最后面
print(names)	# 输出['zm', 'wzw', 'yz', 'zk']
```

#### 列表的删

```python
names = ['zm', 'wzw', 'yz']
# 用正序下标定位
del names[0]	# 删除'zm'
# 用倒序下标定位
del names[-1]	# 删除'yz'

print(names)	# 输出['wzw']
```

#### 列表的改

```python
names = ['zm', 'wzw', 'yz']
names[0] = '朱明'	# 将'zm'元素改成'朱明'
print(names)	# 输出['朱明', 'wzw', 'yz']
```

#### 列表的查

```python
names = ['zm', 'wzw', 'yz']
# 单纯的看该元素在不在列表中
print('zm' in names)

# 查元素的下标
print(names.index('zm'))	# 返回'zm'的下标，即0
# PS:若查询的列表中没有查询的元素就会报错，显示该元素'is not in list'
```

#### 命令嵌套

多种命令搭配，比如删除`zm`元素。

```python
names = ['zm', 'wzw', 'yz']
del names[names.index('wzw')]	# 删除元素zm
```

还有很多其他数据类型，这里者介绍数字、字符串和列表三种，其他数据类型（字典`dict`、集合`set`、元组`tuple`等）之后再慢慢介绍到。

## 1.4 读取输入用户指令

Python终端中进行交互的一个方法。

```python
# 用户输入，不输入程序不会执行下面的语句
name = input('please input your name:')

print(name)	# 输出用户输入的数据
```

需要注意的点：

1. `input()`获得的数据皆为字符串`str`类型；
2. 多个数据输入时，使用多条input语句就好。

## 1.5 格式化输出

```python
name = 'zm'
print('My name is %s' % name)
print('My name is ', name)
print(f'My name is {name}')
print('My name is {}'.format(name))
```

关于格式化输出的一些说明：

1. 以上的方法建议使用第一种和第三种，个人喜欢第三种，方便。
2. 还可以多行输出的格式化，可以自行试试。
3. 对于第一种方法，`%s`表示字符串，`%d`表示整形数字，`%f`表示浮点数，其他的可以自行百度查询。

## 1.6 运算符

### 1.6.1 算术运算

- `+`：加号，比如`1+2=3`

- `-`：减号，比如`2-2=0`

- `*`：乘号，比如`2*2=4`

- `/`：除号，比如`2/1=2`

- `%`：取余，比如`7%3=1`

- `**`：幂运算，比如`2**3=8`

- `//`：取整除，比如`7%3=2`

### 1.6.2 比较运算

- `==`：等于
- `!=`：不等于
- `<`：小于
- `>`：大于
- `>=`：大于等于
- `<=`：小于等于

### 1.6.3 赋值运算

- `=`：单纯的赋值
- `+=`：比如`c+=a`等价于`c = c + a`
- `-=`：同`+=`
- `*=`：同`+=`
- `%=`：同`+=`
- `/=`：同`+=`
- `**=`：同`+=`
- `//=`：同`+=`

### 1.6.4 逻辑运算

- `and`：多个条件都为真就返回真，有一个假就返回假
- `or`：多个条件有一个为真就返回真，全都为假就返回假
- `not`：取反

### 1.6.5 身份运算

- `is`：类似于`==`；但是，`is`比较的是两个数据的`id`，即两个指针是否指向一个值，`==`只判断值是否相等。

  ```python
  # -*- encoding: utf-8 -*-
  a = 10
  b = 10
  
  print(id(a))
  print(id(b))
  
  if a is b:
      print('is OK')	# 输出这个
  else:
      print('is NO')
  
  if a == b:
      print('== OK')	# 输出这个
  else:
      print('== NO')
  ```

## 1.7 流程控制之if..else

### 1.7.1 为何要缩进

C和Java中用`{}`来进行代码分级，Python中采用缩进来进行代码分级，一般四个空格为一个缩进，也可以两个空格，没有严格要求，只是需要保持代码中的缩进保持一致即可，否则会报错。

### 1.7.2 单分支

```python
weather = 'rain'	# 程序输出：带伞和出门
# weather = 'sun'	# 程序输出：出门

if weather == 'rain':
    print('带伞')

print('出门')

```

### 1.7.3 双分支

```python
age = 18	# 修改age，大于等于18和其他数值会产生不同输出结果
if age>=18:
    print('be allowed in')
else:
    print('not be allowed in')
```

### 1.7.4 多分支

```python
age = 18
if 18 <= age < 30:
    print('可以工作')
elif age >= 30:
    print('退休了')
else:
    print('年龄没有达到要求')
# 也可以多个elif，else不是必须要有的
```

## 1.8 小程序

需求：ABCDE五个分数等级，对应关系是：

A：90-100；B：80-89；C：60-79；D：40-59；E：0-39。

```python
score = int(input('please input your score:'))

if 0 <= score <= 39:
    print('E')
elif 40 <= score <= 59:
    print('D')
elif 60 <= score <= 79:
    print('C')
elif 80 <= score <= 89:
    print('B')
elif 90 <= score <= 100:
    print('A')
else:
    print('请输入0-100的数字')
```

## 1.9 猜随机数

```python
import random

number = random.randint(0, 100)

while True:
    input_number = int(input('input your guess number:'))
    if input_number == number:
        print('bingo!')
        break	# 终止循环
    elif input_number < number:
        print('猜小了')
    elif input_number > number:
        print('猜大了')
```

## 1.10 流程控制之while循环

```python
while True:
    print('循环执行')

# while后面的条件如果是True，那么循环就不断执行，直到后面的条件为False
```

### 1.10.1 break和continue

break：终止循环

continue：结束本次循环

```python
max_num = 10
count = 1
while True:
    if count > 10:
        break

    if count % 2 == 0:
        if count % 4 == 0:
            count += 1
            continue
        print(count)

    count += 1
```

### 1.10.2 死循环

保持`while`后面的条件一直保持`True`就会一直死循环下去，不会中断。

### 1.10.3 从1加到100

```python
# -*- encoding: utf-8 -*-
# 方法1
s = 0
for i in range(1, 101):	# range()后面会讲到
    s += i
print(s)

# 方法2
print(sum(range(1, 101)))
```

### 1.10.4 打印0到100的偶数

```python
max_num = 100
count = 1
while True:
    if count > max_num:
        break

    if count % 2 == 0:
        print(count)

    count += 1
```
