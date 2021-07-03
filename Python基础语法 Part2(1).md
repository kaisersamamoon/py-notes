# 第二章 基础语法的补充拓展

## 2.1 关于变量的机制

### 2.1.1 变量的创建和修改

当`Python`创建一个变量时，我们假设是`name`，赋值为`zm`，变量的值（`zm`）就会**存储**在计算机的**内存**中，而该变量的**变量名（`name`）**就会**指向**变量数据（`zm`）存放的**内存地址**，我们在代码中可以通过`id(name)`来查看变量`name`的内存地址。

现在我们修改`name`的值，修改成`zhuming`。此时，`zhuming`放到内存的一个新的地方，然后`name`指向的内存地址改变成`zhuming`的内存地址。那么就意味着一开始的`zm`就已经断了联系了，`Python`解释器有自动垃圾回收机制，在一定时间内就会刷新内存，将没有引用关系的变量值（`zm`）清除掉，恢复成可用的存储位置。

### 2.1.2 变量的指向关系

现在，创建变量`name`并赋值为`zm`，再创建一个新的变量`name1`，赋值为变量`name`，此时的对应关系改怎么解释。

`name1`赋值为`name`时，`name1`和`name`就同时指向`name`的内存地址（`name1`和`name`都指向`zm`的内存地址，此时`name1`和`name`无任何关系）；

我们这时候再修改`name`的值为`zhuming`，现在输出`name`和`name1`，我们可以看到`name`输出为`zhuming`，`name1`输出为`zm`。

## 2.2 身份运算和None

`python`中有很多数据类型，查看一个数据类型的方法有`type()`。

```python
name = 'zm'
age = 1

print(type(age))	# <class 'int'>
print(type(name))	# <class 'str'>
```

### 2.2.1 身份运算

需要用到`is`和`is not`运算符，可以理解为是和不是。

```python
name = 'zm'
print(type(name) is str)	# True
print(type(name) is int)	# False
print(type(name) is not int)	# True
print(type(name) is not str)	# False
```

### 2.2.2 None

`None`表示什么都没有，为空。

在程序中的用处：很多时候创建出来的变量是给用户输入的数据来赋值的，但是我们如果仅仅创建变量，不赋值就会报错。我们就会用`None`来赋值，表示现在值为空，后面会赋值的意思。

## 2.3 三元运算

```python
a = 10
b = 5

# 一般代码
if a > 15:
    c = a
else:
    c = b

# 三元运算 表示如果a > 15，d=a；否则d=b
d = a if a > 15 else b
```

三元运算的公式可以看为`变量名 = 值1 if 条件A else 值2`

## 2.4 细说数据类型-列表

前面说了列表的基本知识（1.3.4 列表），可以回顾一下。下面就做出一些补充。

### 2.4.1 列表的增

1. `append(value)`：追加，需要一个参数，将`value`插入在末尾
2. `insert(index, value)`：插入，需要两个参数，将`value`插入到`index`的位置，原来此位置以及后面的元素都往后挪`1`。
3. `extend(new_list)`：合并，需要一个列表参数，将`new_list`与调用此方法的

### 2.4.2 列表的删

1. `del`：Python自带的删除方法，不需调用。`del`后面跟删除的元素就好。eg：`del names[1]`
2. `pop([index])`：删除，**不加参数**就默认删除列表的**最后一个元素**；加参数就会删除索引为`index`的元素。如果传进的`index`值越界就会报错。eg：`names.pop() names.pop(3)`。
3. `clear()`：清空，不用参数，直接将列表清空，变成**空列表**（可以`print()`空列表看看，**`clear()`返回的不是`None`**）。eg：`names.clear()  # names为[] 即为空列表`。
4. `remove(value)`：从左到右删除**第一个**匹配到的`value`。删掉不存在的值也会报错。

学过下面列表的查方法之一的`index()`之后，我们可以搭配起来实现，通过元素值来匹配删除指定元素。

```python
names = ['zm', 'wzw', 'yz', 'zk']
names.pop(names.index('wzw'))		# 删除列表中的wzw
```

### 2.4.3 列表的改

和前面一样，还是以索引的方式来修改值。eg：`names[0] = 'zm'`

### 2.4.4 列表的查

1. `index(value)`：从左到右查看第一个`value`的下标，若列表中无`value`的值，会报错的。eg：`names.index('zm')`
2. `count(value)`：统计`value`数量，返回的是`int`型数据。

### 2.4.5 切片

#### 切片的正反

```python
names = ['zm', 'wzw', 'yz', 'zk']
print(names[1:2])	# 输出['wzw']，顾头不顾尾（包括1不包括2）
print(names[2:])	# 输出['yz', 'zk']
print(names[:2])	# 输出['zm', 'wzw']
print(names[-2:])	# 输出['yz', 'zk']
print(names[:-3])	# 输出['zm']
```

关于上面的负数，是切片的逆序切法，但是**切片**还是从左到右（**没变**），只是**索引**变成**从右往左**，所以还是顾头不顾尾。这个东西......多试试就会懂了，上升至理论层次可能会比较抽象，难以理解。eg：第五行代码切片包括`-2`的元素，第六行代码切片不包括`-3`的元素。

#### 步长

切片完整的格式是`[begin: end: ​step]`，这里的`step`就是步长。

关于步长，默认是`1`（eg：`[begin: end]`），可以来试试修改步长。eg：`names[::2] # 列表全部元素隔一个输出一个`

切片也可以啥都不写，比如`names[::]`，`name[:]`，他们都等价于`names`，就是啥都没切，原样输出了。

有趣的是，步长可以为负值，这时候整个列表就会反转输出。

```python
names = ['zm', 'wzw', 'yz', 'zk']
print(names[::])	# ['zm', 'wzw', 'yz', 'zk']
print(names[::-1])	# ['zk', 'yz', 'wzw', 'zm']
```

那步长为负时，`begin`和`end`参数也是负值的话，那是不是也符合顾头不顾尾呢？有兴趣可以自己试试，这个点不是很重要。

### 2.4.6 列表的循环与排序

- 排序：`sort()`，根据字符的十进制码进行排序。大体的优先级可以模糊理解为：字符<英文<汉字，可能会有一些特殊的个例。
- 循环：通常我们使用循环来遍历打印列表的元素（大多使用`for`循环，`while`循环看个人，习惯`while`的话就可以使用`while`）。

```python
names = [1, 2, 3, 4, 5]

for i in names:
    print(i)
```

### 2.4.7 嵌套

嵌套适用于列表，也包括后面的元组、字典，除了字符串，其他的基本数据类型都支持嵌套语句。所谓嵌套，就是在一个数据类型里面放入一个数据类型，不限于单一的数据类型。

```python
names = ['zm', ['zm', 'wzw', 'yz'], {'411': 'zm', '409': 'yz'}]
print(names)
```

### 2.4.8 enumerate()的使用

有时我们既需要取出列表的值，又需要列表的索引，我们就可以使用`enumerate()`

```python
# -*- encoding: utf-8 -*-
lis = ['b', 'a']
for i, k in enumerate(lis):
    print(i, k)
```

不过，`enumerate()`可以使用`index()`来代替，只是麻烦一点而已，尽量记住`enumerate()`。

## 2.5 细说数据类型-元组

取值和创建都与列表类似，只是把`[]`改成了`()`。与列表不同的是，元组创建后，**只能查，不能增删改**，可以看做**只读列表**。元组只有`count()`和`index()`两种方法，方法的功能也与前面列表的一样。

```python
names = ('zm', 'wzw')
print(type(names))	# <class 'tuple'>
```

元组的循环遍历、包含（`if ... in tuple:`）等运算都和列表一样。

不过，元组中的元素设置为可变的数据类型，就可以改变元组中的元素。

```python
names = ('yz', ['zm', 'wzw'])
print(names)	# ('yz', ['zm', 'wzw'])
names[1][0] = 'zhuming'
print(names)	# ('yz', ['zhuming', 'wzw'])
```

比如我们元组中嵌套列表，我们可以修改列表里面的元素。元组只是存每个元素的内存地址，而作为元组的元素的列表里面的元素存在内存里另外的空间，所以是可变的。

## 2.6 细说数据类型-字符串

### 2.6.1 切片

我们也可以对字符串使用切片的所有功能，或者说我们可以把字符串当做一个列表，每一个字符是列表的每个元素。

```python
name = 'zhuming'
print(name[::-1])
print(name[::2])
print(name[::2])
```

但是，值得注意的是，字符串不可被修改，修改的话都会创建一个新值，我们可以通过查看修改前和修改后的内存地址来观察。

```python
name = 'zm'
print(id(name))
name = 'wzw'
print(id(name))		# 与第一次输出的地址不一样
```

### 2.6.3 转义字符

Python中有许多有代表特殊含义的字符，被称为转义字符。比如常见的有`\n`、`\t`等，分别代表了回车、缩进等特殊含义。

如果不想让转义字符生效，就可以在前面加一个`\`，或者在字符串前加一个`r`，表示原生，不触发转义字符。

```python
print('zm\nwzw\tyz')
# 输出：
# zm
# wzw    yz

print('zm\\nwzw\\tyz')	# 输出：zm\nwzw\tyz
print(r'zm\nwzw\tyz')	# 输出：zm\nwzw\tyz
```

### 2.6.4 字符串的常用操作

- `capitalize()`：大写字符串的首字母。eg：`name = 'jack chen' name.capitalize()就是'Jack chen'`，注意而不是`'Jack Chen'`

- `casefold()`：大写全部变小写，与`lower()`函数的区别在于，`casefold()`适用于大多数字符。eg：`name = 'Jack Chen' name.casefold()就是'jack chen'`

- `center(width, fillchar)`：定义宽度，然后字符中间显示，两侧填充`fillchar`的字符。

  ```python
  name = 'System Of Information'
  print(name.center(50, '#'))
  # 输出：
  # ##############System Of Information###############
  ```

- `count(char, start, end)`：计数字符串内出现`char`字符的次数，后面两个参数可填可不填，表示切片的开始和结束，在切出来的一段字符串内对`char`进行计数。

  ```python
  the_string = 'ssaadd sad'
  print(the_string.count('s'))	# 3
  print(the_string.count('a', 0, 3))	# 1（顾头不顾尾）
  ```

- `endswith(str)`：判断字符串是以什么结尾。

  ```python
  email = '2511343050@qq.com'
  if email.endswith('@qq.com'):
      print('邮箱格式正确')
  elif email.endswith('@163.com'):
      print('邮箱格式正确')
  else:
      print('邮箱格式错误')
  # 输出：
  # 邮箱格式正确
  ```

- `find(char, start, end)`：这里的三个参数和`count`的参数一样的含义，找到了就返回`char`的下标。注意的是`find`只能找从左到右第一个的`char`。

  ```python
  name = 'qwq owo xwx'
  
  ```

- `format()`：格式化输出。

  ```python
  title = ' the system '
  choice_1 = ' [1] select '
  choice_0 = '  [0] exit  '
  # %
  welcome = """
  ----%s----
  ----%s----
  ----%s----
  ----%s----
  """ % (title, choice_1, choice_0, title)
  print(welcome)
  
  # format 1
  welcome = """
  ----{0}----
  ----{1}----
  ----{2}----
  ----{0}----
  """.format(title, choice_1, choice_0)
  print(welcome)
  
  # format 2
  welcome = f"""
  ----{title}----
  ----{choice_1}----
  ----{choice_0}----
  ----{title}----
  """
  print(welcome)
  ```

- `index(char, start, end)`：和count以及find类似的功能，只是返回的是下标

- `isdigit()`：判断字符串是否是一个整数（可以理解为`int()`强制转换为整型），返回`True`或`False`

- `islower()`：判断字符串是否全部是小写。

- `isspace()`：判断字符串是否有空格，多个空格也可以。

- `isupper()`：判断字符串是否全部是大写。

- `join(iterable)`：字符串的拼接，必须全是字符串，不能有其他任何类型。

  ```python
  names = ['zm', 'wzw', 'yz']
  print(''.join(names))	# zmwzwyz
  print('|'.join(names))	# zm|wzw|yz
  print(', '.join(names))	# zm, wzw, yz
  ```

- `ljust(width, fillchar)`：与`center()`类似，从左开始数

- `lower()`：大写变小写，只支持ASCI Ⅱ编码。

- `strip(chars)`：将字符串两边的其他字符清除，不写具体`chars`的值就默认包括空格和转义字符这些。该函数还衍生出另外两个函数，分别是`lstrip()`和`rstrip()`，`lstrip()`功能是将左边的其他字符清除，`rstrip()`功能是将左边的其他字符清除。

- `replace(old, new, count=None)`：将原字符串中的`old`片段换成`new`，`count`表示换多少个（顺序为从左到右），默认是全部`old`都换。

  ```python
  score = 'My score is 580!580!580!'
  print(score.replace("580", "630"))	# 修改成My score is 630!630!630!
  print(score.replace("580", "630", 1))	# 修改成My score is 630!580!580!
  print(score.replace("580", "630", 2))	# 修改成My score is 630!630!580!
  ```

- `split(sep, maxsplit=-1)`：字符串通过`sep`分割成列表的元素，以列表的形式返回。如果什么参数都不写，字符串直接变成只有一个元素的列表。`maxsplit`设置的是从左到右分割几次，默认无数次。该函数还衍生出一个函数，是`rsplit()`，其功能就是把从左往右变成从右往左。

  ```python
  n = ['zm', 'yz', 'wzw']
  name = ",".join(n)	# 'zm,yz,wzw'
  names = name.split(',')	# ['zm', 'yz', 'wzw']
  ```

- `startswith(prefix, start=None, end=None)`：和`endswith()`一样，一个判断字符串以什么开头，一个以什么结尾。`start`和`end`和`endswith()`的参数功能一模一样。

- `swapcase()`：大小写交换，小写变大写，大写变小写，不过特殊字符不会变。

- `upper()`：字符串统一变成大写。

- `zfill(width)`：规定长度，不够长度用`0`来补，一般不常用，网络编程时可能会用到。

总结:

- **查**：`find()`、`index()`、`count()`

- **改**：`replace()`、`upper()`、`lower()`、`swapcase()`、`casefold()`、`strip()`、`split()`

- **格式化**：`format()`、`ljust()`、`rjust()`、`join()`

- **判断**：`isdigit()`、`startswith()`、`endswith()`

## 2.7 细说数据类型-字典
### 2.7.1 字典的优点及创建

方便嵌套操作海量数据，而且字典是以键值对形式存储，可以通过查找键来获得值，而字典的键可以是整型、字符串、元组等不可变数据类型（且每个键要唯一存在），而不是像列表那样只有单一的下标查询。

字典的创建：

```python
# {key1: value1, key2: value2, ...}
new_dict = {
	"name": 'zm',
    "password": '123',
}
print(new_dict)
print(new_dict['name'])	# 取键name对应的值
```

字典没有顺序（**无序**），查询**速度不受字典大小的影响**（HASH），非常快。字典的键不可变、必须唯一，键对应的值可以有多个，可以被修改、可以不唯一。

#### 几种创建方法

```python
# 1
person = {"name": "zm", "age": 20}	# {'name': 'zm', 'age': 20}
# 2
person = dict(name='zm', age=20)	# {'name': 'zm', 'age': 20}
# 3
{}.fromkeys([1, 2, 3, 4, 5, 6, 7, 8], 100)	# {1: 100, 2: 100, 3: 100, 4: 100, 5: 100, 6: 100, 7: 100, 8: 100}
```

### 2.7.2 字典的增删改查

#### 字典的增

```python
new_dict = {
	"name": 'zm',
    "password": '123',
}
# 增 1 （如果job已经存在就变成了修改job的值）
new_dict['job'] = 'teacher'
# 增 2 （如果address已经存在，setdefault就只会返回原address的值，不进行任何修改或添加操作）
new_dict.setdefault('address', '地球')
print(new_dict)		# 多了job和address两个键值对
```

#### 字典的删

```python
new_dict = {
	"name": 'zm',
    "password": '123',
}
new_dict.pop('name')	# 删除键为name的键值对
new_dict.popitem()	# 随机删除一个键值对
del new_dict['name']	# 删除键为name的键值对
new_dict.clear()	# 清空字典
```

==`del`在删除数据类型的所有方法里，尽量不要用......==

#### 字典的改

```python
dic = {1: 1, 2: 2, 3: 3}
dic2 = {1: 2, 2: 4, 4: 8}
# 修改3的键值对
dic[3] = 5	# {1: 1, 2: 2, 3: 5}
# 将dic2的键值对加到dic里面，如果键有重复的情况，dic2中的键值对会覆盖dic的原键值对
dic.update(dic2)	# {1: 1, 2: 4, 4: 8, 3: 5}
```

#### 字典的查

1. `dic['key']`：返回字典`key`对应的值，不存在则会报错；
2. `dic.get(key, default=None)`：如果有就返回`key`对应的`value`，找不到就返回`default`的值；
3. `'key' in dic`：存在返回`True`，不存在返回`False`；
4. `dic.keys()`：返回包括`dic`的所有键的列表；
5. `dic.values()`：返回包括`dic`的所有值的列表；
6. `dic.items()`：返回包括`dic`所有键值对（元组的形式：`(key, value)`）的列表。

#### 循环

```python
for i in dic:
    print(i)	# 打印的只是key

# 推荐方法
for i in dic:
    print(i, dic[i])

# 以下效率比较低（用到keys()，items()，values()的都比较慢）
for i in dic.items():
    print(i)
    
for k, v in dic.items():
    print(k, v)
```

## 2.8 细说数据类型-集合

### 2.8.1 集合的作用

和列表一样，存一堆数据，里面的元素不可变，不能存列表、字典等可变数据类型放在集合内，只能存储元组、数字、字符串等不可变数据；集合天生去重，在集合不存在重复元素；集合无序，不能通过索引来查找值。

集合最重要的两个功能：**去重**和**关系运算**（与、并、异或等）

### 2.8.2 集合的增删改查

```python
# 去重
names = ['zm', 'wzw', 'yz', 'zk', 'zm', 'zk']
print(set(names))	# {'wzw', 'zm', 'zk', 'yz'}
print(type(set(names)))	# <class 'set'>

# 增
set_name = set(names)
set_name.add('py')	# {'zm', 'zk', 'yz', 'wzw', 'py'}

# 删
set_name.discard('py')	# 删除py，{'zm', 'zk', 'yz', 'wzw'}
set_name.discard('p2y')	# 删除不存在的值时，就不进行任何操作

set_name.pop()	# 随机删除并返回删除后的集合

set_name.remove('zm')	# 删除zm
set_name.remove('zm2')	# 删除不存在的值时，就会报错

# 查
# 只能in运算
if 'wzw' in set_name:
    print(True)

# 改
# 不能修改！
# 切片也是不能用的
```

### 2.8.3 集合的关系运算

```python
names_181 = ['zm', 'wzw', 'yz', 'zk', 'kyj']
names_182 = ['zm', 'yz', 'py', 'zzw', 'ghd']

print(names_181 & names_182)	# 交集
print(names_181 | names_182)	# 并集
print(names_181 - names_182)	# 差集，only in names_181
print(names_182 - names_181)	# 差集，only in names_182
print(names_181 ^ names_182)	# 对称差集，等于 两个集合的并集 - 两个集合的交集
```

集合的关系一般只有三个：包含、相交、不相交。Python中分别用下面的方法判断：

- `names_181.isdisjoint(names_182)`：判断两个集合是否相交，返回True or False
- `names_181.issubset(names_182)`：判断`name_181`是否被包含于`name_182`中，返回`True` or `False`
- `names_181.issuperset(names_182)`：判断`name_181`是否包含`name_182`，返回`True` or `False`

集合还有其他的方法，这些就不一一赘述了，用到就百度一下就好了。

## 2.9 关于二进制和十六进制

### 2.9.1 二进制

理解数学的十进制到二进制的转换就好了，**二进制逢2进一**。

计算机为什么用二进制？是因为计算机的晶体管只能有高电平和低电平两个状态，先人把低电平和高电平用0和1表示，通过这种方法，用二进制来抽象表示人类生活中的种种信息数据。

Python中将十进制转化成二进制的方法是`bin()`，十进制的值只能从`0-255`，更高的表示方法需要更深学习`bin()`方法的具体表示，我们就可以不用看了，了解二进制的转化即可。

### 2.9.2 十六进制

10进制用`0-9`表示所有数字，2进制用`0, 1`表示所有数字，而16进制用`0-9`以及`A-F`，15个符号表示所有数字，逢16进一。`A-F`分别代表`10-15`。

16进制只是一种表示方法，计算机的底层还是使用2进制的。计算机中16进制多用来表示`HTML/CSS`的颜色表的色号（有`RGB`等，16进制也是一种常用表示方法）、mac地址、字符编码等都用16进制来表示。

为了16进制不与其他进制不混淆，16进制一般开头为`0x`，后面的字符才是可以转化的东西，比如`hex(16)`输出是`0x10`，数学上的计算方法就是：`0* 16*0+1* 16*1=16`，数学方法就不再多介绍了，可以自行百度了解，自己演算的时候很常用。

Python中将十进制转换成十六进制的方法是`hex()`，可以自己多试试。

## 2.10 字符编码

### 2.10.1 文字的显示原理

为了表示字符，我们必须实现zhuming -> 十进制，使他们关联起来。

将一个一个字符与十进制数字对应起来，最常见的有`ASCII`码（基于拉丁字母和特殊字符的一套字符编码表）。然而`ASCII`码一开始只有127个，后来又补充了一些（128后面的字符对应关系称作扩展`ASCII`码），但是没有中文。Python中可以通过`ord()`来查看字符对应的十进制数。

但是每个字符转化的二进制长度都不一样，二进制怎么断句呢？因为ASCI Ⅱ码小于255，所以就规定每8位（`bit`）代表一个字节（`B`，又称`bytes`）。`1024B=1KB`，`1024KB=1MB`，`1024MB=1GB`，`1024GB=1TB` -> `PB` `EB` `ZB`等等。

因为`ASCII`表没有中文，我们就自己研发了一张表，又因为汉字一个`bit`存不下，我们就用了两个`bit`来存储。后来研发成功，名为`GB2312`，总共可有存储6w个汉字，当时只有6763个汉字（日常生活中常用的）

随着电脑在中国的普及，越来越多的字需要被计算机表示，后面升级成了`GBK`编码，表示了2w多个字符（包括汉字、少数民族语言、日语、韩语等），21世纪又进行了升级，表示了2w8k多个字符。

随着发展，问题又来了，人们生活中不光单纯使用中文，英文使用的频率和中文的频率差不多，如果用`GBK`来表示纯英文的文档比用`ASCII`一倍的内存。那么如何兼容呢？

因为`ASCII`高位的字符（大于`127`的特殊字符）比较少用，那么两个连续的高位字符就更少出现了。我们就增加一个判断，如果有两个连续的高位字符，我们就使用`GBK`编码，其他情况就用`ASCII`编码，较好的解决了兼容性问题。

### 2.10.2 编码种类

每个国家可能都会有自己的编码，比如美国是`ASCII`，中国是`GBK`，日本是`shift_JIS`等等等等，每个的字符对应关系都不一样，那不同国家的软件自己拿来就会产生乱码。

最后，出现了`Unicode`编码，2-4字节，俗称万国码，支持所有的语言（13w6k多个），可以与各种语言进行转换（将已经出来的软件不用推倒重做）

但是Unicode用了2-4个字节，比ASCII的一个字节多了很多，在当时的传输和硬件存储水平下，很不适应。

最后针对传输和存储，基于Unicode做出了一个新编码，叫UTF-8（使用1、2、3、4字节表示所有字符，优先使用少的字节）。

> 下面两个编码因为没有解决传输和存储的问题，所以不常使用，只做解。
>
> UTF-16：使用2、4字节表示所有字符
>
> UTF-32：使用4个字节表示所有字符

这里也简单提一下python2和python3的区别。

python2用的是`ASCII`码，python3用的是`utf-8`，所以python2不能显示中文，所以python2在程序的开头一般都要手动声明`# -*- encoding: utf-8 -*-`（官网推荐写法），必须在代码的顶头（第一行）写。

我们**python3呢建议也写上**，防止python3偶尔因为编码文件导致自己的项目代码运行报错，最后画个好几天解决就很伤了。

>  `# -*- encoding: utf-8 -*-`

## 2.11 字典密码——HASH

### 2.11.1 HASH

HASH（又称哈希）是把**任意长度**的输入（又叫做预映射）通过**散列算法**变换成**固定长度**的输出，该输出值就是散列值。这种转换是一种压缩映射，这样我们可以通过更小的值来表示很大的值所表示的东西。

HASH是一种算法，很复杂的运算，它的输入可以是字符创或者数字或者任何文件，经过哈希算法处理后，变成一个固定长度的输出，该输出就是哈希值。哈希算法有一个很大的特点，就是**不能从结果推算出输出是什么，所以成为不可逆的算法**。

哈希多应用于密码学以及区块链等方面。

Python中有`hash()`的方法来将字符串或数字变成哈希值，每次重启Python之后，同样的字符或数字`hash()`的哈希值都不是一致的。注意，`hash()`的参数只能`hash`不可变的值。

#### HASH的特性

1. 刚才也说了，不可逆是HASH的一个重要特性。生活中也有许多不可逆的情况，比如煮熟的鸡蛋变不回生鸡蛋。
2. 计算极快。20G高清电影和5K的文件

#### HASH的用途

1. **密码**。常用的加密算法是`md5`。`md5`就是基于`HASH`做的，使你的密码经过基于`HASH`的算法处理，使你的密码与一个哈希值一一对应，然后存放进数据库中。如果想登陆，就只能知道原来的密码是什么，然后输入，进行算法的处理，将生成的值与数据库内存储的哈希值比较，如果一致才可以登陆成功。
2. **文件完整性校验**。常用的也是`md5`算法。一个文件对应一个哈希值，在传输过程中可能会遇到拦截等恶意攻击，当接收文件之后，再进行md5处理，如果两次得出的哈希值一致，那就说明文件完整，没有残缺或植入了木马等恶意程序。
3. **数字签名**。数字签名是为了防止假情报，效果类似于对暗号，A说天王盖地虎，B回应宝塔镇河妖，那A和B就确定了是自己人，才可以进行通信。数字签名就是在互联网上的暗号应用。A说的天王盖地虎在互联网上称为**私钥**，将发送的原文进行`hash`，生成一段`hash`值（就是摘要信息），然后把原文和摘要信息一同发给B。他回应的宝塔镇河妖被称为**公钥**，将你的摘要信息解密，得到`hash`值。B再对原文件进行`hash`，也得到一个`hash`值，将这个`hash`与a发来的`hash`值进行比较，如果一致就说明这个原文是A本人发送的，而不是别人发送的。
4. **区块链**。电子钱包，加密钱包等应用。
5. 还有很多其他的应用就不一一介绍了。

### 2.11.2 应用HASH的数据结构

Python中有两个数据类型是基于`hash`来做的，一个是`dict`，一个是`set`。

#### 字典快的原因

`dict`有三个显著特点：

- `key`唯一
- `key`不可变
- 查询速度极快，且不受`dict`大小的影响的特点。

第三个特性就是`hash`带来的。下面就进行简单的原理解释（真实的原理不是这样，只是做类似的解说）。

`dict`的每个`key`都会经过`hash`生成一段固定长度的`hash`值，然后这些`hash`值经过大小排序放入一个列表`A`中（`hash`值都是一串数字），需要查询哪个字典的值就通过二分法查找列表`A`，所以只需要31次查询就可以找20亿的数据，计算机查询一次也仅仅只需要几毫秒。

不过，字典的原理还不单单只有这些，这些只是简单地类似原理，真实的字典原理比这还要复杂。

#### 集合为何去重

集合每`add`进一个值，他都会经过`hash`运算出一个`hash`值，然后存放在一个列表A中，如果后面`add`的数据的`hash`值在列表A中，那么这个数据就不会再存进集合里了。

### 2.11.3 判断数据结构是否可变

将这个数据进行`hash`，**如果可以哈希就是不可变的数据，反之则是可变的数据类型。**

## 2.12 文件操作

### 2.12.1 基础操作

日常文件操作的步骤：

1. 找到文件，打开
2. 读、修改
3. 保存、关闭

Python中的文件操作：

1. `open(filename)`：根据路径和文件名打开文件
2. `f.read()`/`f.write()`：读写操作
3. `f.close()`：文件关闭（默认保存）

需要注意的是文件操作的模式只能以一种方式（后面再介绍复杂的多种方式混合的文件操作模式）。python有`r`，`w`，`a`三种基本方法，分别代表**只读模式**、**写入模式**、**追加模式**三种基本方式。（注意，如果`w`的写入模式下会覆盖原文件的旧数据，想在原文件的旧数据后面写新数据的话就要用到`a`的追加模式才可以）

因为是文件的操作，所以存在路径、文件名等差异，每个人都不一样。我们这里就统一规定一下。

以下文件操作的代码都是对名为`test.txt`，路径是所在目录是当前python文件下的路径的文件进行的操作。

```python
# -*- encoding: utf-8 -*-

# 文件的读
f = open(file='test.txt', mode='r')
# 读一行
print(f.readline())
# 读剩下的数据
print(f.read())
f.close()

# 不需要写close()的with语句
with open(file='test.txt', mode='r') as f:
	# 读一行
    print(f.readline())
    # 读剩下的数据
    print(f.read())
print('with代码块执行完之后，with会关闭所有代码块中用到的功能进程，其中就包括f.close()')

# 文件的追加写入
f = open(file='test.txt', mode='a')
# 读一行
f.write('\nzk\t24\t18845516854')
f.close()


# 文件的覆盖写入
f = open(file='test.txt', mode='w')
# 读一行
f.write('zk\t24\t18845516854')
f.close()
```

#### 循环输出

```python
# -*- encoding: utf-8 -*-
f = open(file='test.txt', mode='r')

print('循环输出：')
for line in f:
    print(line.strip())     # strip是去掉每一行末尾的\n
```

```python
# -*- encoding: utf-8 -*-
f = open(file='test.txt', mode='r')
print('输出age大于20的信息')
for line in f:
    line_info = line.strip().split(', ')
    if int(line_info[1]) >= 20:
        print(line.strip())

f.close()
```

```python
# -*- encoding: utf-8 -*-
f = open(file='test.txt', mode='r')
print("全部输出：")
f.readlines()

f.close()
```

### 2.12.2 file类的常用功能

- `seek(num)`：光标的定位，移动到`num`的位置，**`num`是以字节来算而不是字符！**中文占三个字节，所以`seek()`定位的时候可能会定位到一个字符的几个字节之间，导致可能会抛出编码错误（`UnicodeDecodeError`）

  ```python
  # -*- encoding: utf-8 -*-
  with open('test.txt', 'r') as f:
      f.seek(2)	# 从zm后面开始输出
      print(f.readlines())
  ```

- `flush()`：强制刷入硬盘。因为对硬盘的数据进行频繁操作很慢，所以文件操作有个**缓存机制**，`write`的数据**先写到缓存的内存**里，缓存满了才会**刷到硬盘**里。比如我们一直`write`方法写入，但是如果你不`close()`它就不会立即刷到硬盘。如果**写入的数据很重要**，怕运行过程中断电等因素（计算机关闭时只有硬盘的数据不会被清空）影响到关键数据的写入，就可以用`flush()`强制刷入硬盘中。

- `readable()`：判断文件是否可读。

- `seekable()`：判断文件是否可以进行`seek()`，比如`Linux`所有的东西都是文件，所以需要判断这个函数判断，不常用。

- `tell()`：返回当前光标的位置。

- `truncate()`：按指定长度截断文件。指定长度就从文件头开始到指定长度为止；不指定就从当前位置截到文件末尾。**长度也是用字节来算，不是按字符来算！**针对网站访问量大的日志的分析可能会用到。

- `writable()`：判断文件是否可写。

- `writelines()`：传入一个列表数据，然后一个元素一行的写入文件。

### 2.12.3 混合模式下处理文件

文件模式肯定不止前面的基本三种，打开文件还有`w+`、`r+`、`a+`三种混合模式，分别是三种基本文件模式的组合，比如

- `w+`就是创建一个新文件，写一段内容可以再把内容读出，可以理解为`w`和`r`的组合，不常用；
- `r+`就是能读能写，可以理解为`r`和`a`的组合，文件写入是从末尾开始写；读的话，是从开头开始读，不用重新`seek()`，不用为较为常用；
- `a+`就是文件一打开，文件写入是从末尾开始写，读也是从文件末尾开始读。

这三种模式很少使用，`r+`和`a+`偶尔会用到。

#### 混合模式修改文件

我们要修改文件的话就需要用到`r+`的混合模式。比如我们要在`test.txt`的第一行中插入一个`'dd'`。

```python
# -*- encoding: utf-8 -*-
with open('test.txt', 'r+', encoding='utf-8') as f:
    f.seek(2)
    f.write('dd')
```

插入过后打开`test.txt`文件，我们就可以看到，插入的`'dd'`插入是插入成功了，但是`dd`的第二个`d`会把`seek(2)`后面的一个字节（别忘了`seek()`是以字节为单位的）覆盖掉...... 这是我们不想看到的，下面我们就来阐述这个问题的原因以及解决方法。

**在文件中间修改数据的话，就会覆盖后面的数据**，这个**和数据在硬盘上的数据存储方法有关系**。但是像`word`和`vim`这些工具都可以修改文件，那他们到底是怎么实现的呢？

我们就可以先把硬盘的文件数据加载到内存，再对内存的文件数据进行修改，然后再重新刷到硬盘里。如果你打开很大的`word`，你的电脑可能会花费较多的时间加载，就是因为在将文件数据读入内存。

### 2.12.4 其他模式

二进制打开文件的三种模式：`rb`、`wb`、`ab`。

### 2.12.5 不占内存的修改文件

如果像上面讲的那样，我们将数据从硬盘全部读入到内存，然后再对内存的文件数据进行修改的话，如果文件很大的话，那就会对内存造成很大影响。

那么我们可以读取一行数据到内存然后对这行数据进行修改的操作，然后刷入硬盘，周而复始，就完成了对整个文件数据的修改。这种方法被称作边读边写的方法。

将文件中的`zm`都改为`qq`。

```python
# -*- encoding: utf-8 -*-
import os

old_file = 'test.txt'
new_file = 'test_new.txt'
f = open(old_file, "r")
f_new = open(new_file, "w")
old_str = 'zm'
new_str = "qq"

for line in f:
    if "zm" in line:
        line = line.replace(old_str, new_str)
        f_new.write(line)

f.close()
f_new.close()

os.replace(new_file, old_file)
```

## 2.13 关于脚本的说明

Python原来就是一种脚本语言，脚本的数据获取是通过`sys`模块的`argv()`实现的。

前面没讲的是，在Python中导入库或者模块，需要用到`import`语句，并在开头几行写，上面的`import os`就是一个例子。

下面我们给出不占内存修改文件的脚本写法，主要看5到7行的脚本获取输入数据。

```python
import os
import sys

# 脚本获取传入的数据 需要在前面写，中间不能用其它语句
old_str = sys.argv[1]
new_str = sys.argv[2]
file = sys.argv[3]

new_file = f'new_{file}'

f = open(file, 'r', encoding='utf-8')
new_f = open(new_file, 'w', encoding='utf-8')

for line in f.readlines():
    if old_str in line:
        new_line = line.replace(old_str, new_str)
    else:
        new_line = line
    new_f.write(new_line)

f.close()
new_f.close()
os.replace(new_file, file)
```