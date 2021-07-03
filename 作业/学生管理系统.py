dicts = []
tis = 1
person ={
   "names":"xxx",
   "sex": "xxx",
   "id" : "xxx",
   "results" : "xxx"
   }
while True:
   person['names'] = input("请输入姓名")
   person['sex'] = input("请输入%s的性别"%(person['names']))
   person['id'] = input("请输入%s的学号"%(person['names']))
   person['results'] = input("请输入%s的成绩"%(person['names']))
   
   dicts.append(person)
   tis = int(input("是否继续录入:1:继续录入 0：退出录入"))
   if tis == 0:
      break
print(dicts)


