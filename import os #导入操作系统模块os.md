># os模块
>
>import os #导入操作系统模块
>
>os.getcwd()#访问目前操作环境
>'D:\\python3.9'
>
>os.chdir ("E:\\\")#修改操作环境至\\\E盘
>os.getcwd()
>'E:\\'
>
>os.listdir("E:\\\\")#访问当前操作环境有多少目录
>['$RECYCLE.BIN', '2048游戏', 'GIT', 'github', 'New Folder', 'System Volume Information', 'tppora', '冰川上网客户端', '嗨 录屏大师', '实例', '战网', '百度云下载', '虚幻文件', '迅雷云盘']
>
> os.mkdir("E:\\目录创建练习")#新建单层目录（如果目录存在，抛出异常）
>
>os.makedirs("E:\\\目录创建练习2\\\练习1")#递归创建多层目录，如果目录存在，抛出异常，注意：（E：\\\目录创建练习2\\\练习1跟E：\\\目录创建练习2\\\练习2）并不冲突
>
>os.rmdir("E:\\目录创建练习2")#删除单层目录，注意（删除的目录里面不能有目录和文件）
>Traceback (most recent call last):
>  File "<pyshell#11>", line 1, in <module>
>
>​    os.rmdir("E:\\目录创建练习2")
>OSError: [WinError 145] 目录不是空的。: 'E:\\目录创建练习2'
>
>
>
> os.remove ("E:\\目录创建练习2\\练习1\\test.txt")#删除目录里面的文件
>
>os.rmdir("E:\\目录创建练习2\\练习1")#正确方法（删除目录里面的子目录及文件）
>
>os.removedirs("E:\\目录创建练习2\\子目录")#递归删除目录，从子目录到父目录尝试逐一删除（遇到非空目录则抛出异常）
>
><img src="C:\Users\PAN\AppData\Roaming\Typora\typora-user-images\image-20210321150117527.png" alt="image-20210321150117527" style="zoom:50%;" />
>
>os.rename("E:\\目录创建练习","E:\\目录创建练习nex")#将文件old重新命名为new
>
>
>
>os.system("cmd")#运行系统的shell命令
>
>![image-20210321151047505](C:\Users\PAN\AppData\Roaming\Typora\typora-user-images\image-20210321151047505.png)
>
>以下是支持路径操作的一些常用定义，支持所有平台
>
>```python
>os.curdir#指定当前目录（"."）
>```
>
>os.listdir(os.curdir)
>['$RECYCLE.BIN', '2048游戏', 'GIT', 'github', 'New Folder', 'System Volume Information', 'tppora', '冰川上网客户端', '嗨 录屏大师', '实例', '战网', '百度云下载', '目录创建练习nex', '虚幻文件', '迅雷云盘']
>
>```python
>os.pardir#指定上一级目录（".."）
>```
>
>
>
>```python
>os.sep#输出操作系统特定的路径分隔符（win下为"\\",linux下为"/"）
>```
>
>```python
>os.linesep#当前平台使用的行终止符（win下为"\r\n",linux下为"\n"）
>```
>
>```python
>os.name#格式当前使用的操作系统（包括:posix,nt,mac,os2,ce,java）
>```
>
># os.path模块

```
basename(path)#去掉目录路径，单独返回文件名
```

###### os.path.basename("E:\\a\\c\\temes.ex")

'temes.ex'

```
dirname(path)#去掉文件名，单独返回目录路径
```

###### os.path.dirname("E:\\a\\c\\temes.ex")

'E:\\a\\c'

```
join(path1[,],path2[,...])#将path1，path2各部分组成一个路径
```

###### os.path.join('a','b','c')

'a\\b\\c'

###### os.path.join('E:\\','a','b','c')

'E:\\a\\b\\c'

```
split(path)#分割文件名与路径，返回（f_path,f_name）元组。如果完全使用目录，它也会将最后一个目录作为文件分离，且不会判断文件或者目录是否存在
```

###### os.path.split("E:\\a\\temes.exe")#将目录与文件名分开

('E:\\a', 'temes.exe')

###### os.path.split("E:\\a\\c")#将最后一个目录当作文件名分开了

('E:\\a', 'c')

```
splitext(path)#分离文件名与拓展名，返回（f_nema,f_extension）元组
```

###### os.path.splitext("E:\\a\\temes.exe")

('E:\\a\\temes', '.exe')

```
getsize(flie)#返回文件的尺寸，单位是字节
```

###### os.path.getsize("E:\\迅雷云盘\\Thunder\\UninstallXLWFP.exe")

45375

```
gettime(file)#返回指定文件最近的访问时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）
```

###### os.path.getatime("E:\\迅雷云盘\\Thunder\\UninstallXLWFP.exe")

1616135777.6643395

>> ### import time#导入time模块 #gmtime（）英国时间，localtime（）中国时间，东八区时间

>> time.gmtime(os.path.getatime("E:\\迅雷云盘\\Thunder\\UninstallXLWFP.exe"))
>> time.struct_time( m_year=2021, tm_mon=3, tm_mday=19, tm_hour=6, tm_min=36, tm_sec=17, tm_wday=4, tm_yday=78, tm_isdst=0)



```
getctime(file)#返回指定文件的创建时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）
```

###### time.gmtime(os.path.getctime("E:\\迅雷云盘\\Thunder\\UninstallXLWFP.exe"))

time.struct_time(tm_year=2021, tm_mon=3, tm_mday=19, tm_hour=6, tm_min=36, tm_sec=11, tm_wday=4, tm_yday=78, tm_isdst=0)

```
getmtime(file)#返回指定文件最新修改时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）
```

###### time.gmtime(os.path.getmtime("E:\\迅雷云盘\\Thunder\\UninstallXLWFP.exe"))

time.struct_time(tm_year=2021, tm_mon=3, tm_mday=19, tm_hour=6, tm_min=36, tm_sec=11, tm_wday=4, tm_yday=78, tm_isdst=0)

### 以下函数返回True或False

```
exists(path)#判断指定路径（目录或文件）是否存在
```

os.path.exists("E:\\PAN")
False

>>> os.path.exists("E:\\实例")
>>> True

```
isabs(path)#判断指定路径是否为绝对路径,相对路径a\\b\\a.exe,绝对路径E:\\a\\b\\a.exe
eg：访问E：\\下面的dell.exe文件,相对路径..\\a\\dell.exe，绝对路径：E:\\dell.exe
```

os.path.isabs("E:\\实例")
True
>>> os.path.isabs("E:\\实例\\潘尚国.txt")
>>> True

```
isdir(path)#判断指定路径是否存在且是一个目录
```

 os.path.isdir("E:\\实例\\潘尚国.txt")
False

>>> os.path.isabs("E:\\目录创建练习nex")
>>> True

```
isfile(path)#判断指定路径是否存在且是一个文件
```

>>> os.path.isfile("E:\\目录创建练习nex")
>>> False
>>>
>>> >>> os.path.isfile("E:\\实例\\潘尚国.txt")
>>> >>> True

```
islink(path)#判断指定路径是否存在且是一个符号链接#快捷方式
```



```
ismouth(path)#判断指定路径是否存在且是一个挂载点# A盘，E盘这些就是挂载点
```



```
samefile(path1,path2)#判断path1和path2两个路径是否指向同一个文件path2
```

os.path.samefile("E:\\目录创建练习nex\\新建文本文档.txt","E:\\目录创建练习nex\\潘尚国.txt")
False

>>> os.path.samefile("目录创建练习nex\\潘尚国.txt","E:\\目录创建练习nex\\潘尚国.txt")
>>> True

采用两种路径，相对路径和绝对路径



# pickle模块

pickling:存放

pickle.dump()

```
>>> import pickle #导入模块

>>> my_list = [123,"潘尚国",["panshangguo"]]#创建一个列表
>>> pickle_file = open ("E:\\目录创建练习nex\\my_list.pkl","wb")打开文件，并指定位置
>>> pickle.dump(my_list,pickle_file)#引入pickle模块，导入方法
>>> pickle_file.close()关闭文件
```

![image-20210321173530735](C:\Users\PAN\AppData\Roaming\Typora\typora-user-images\image-20210321173530735.png)

unpickling:读取

pickle.load()

```

```

