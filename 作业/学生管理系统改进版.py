student = []
print("欢迎进入学生管理系统\n请输入账号密码进行登录：\n初始账号：admin \n密码：admin")
adm = 'admin'
passWorld = 'admin'
myAdm = input("请输入账号：")
myPassWolrd = input("请输入登录密码：")

if myAdm == adm and myPassWolrd == passWorld:
	while True:
		judge = int(input("请选择方式: \n 1：添加 \n 2：显示 \n 3：删除 \n 4：修改 \n 5：统计 \n -1:退出系统 \n 请做出选择："))
		if judge == -1:
			break


		def studentAdm(judge):
			if judge == 1:

				add()
			elif judge == 2:
				sele(student)
			elif judge == 3:
				dele(student)
			elif judge == 4:
				unda(student)
			elif judge == 5:
				statistical(student)

			else:
				print("输入错误，请重新输入：")


		# 增
		def add():
			cls = {}
			names = input("请输入姓名:")
			age = int(input("请输入%s的年龄" % (names)))
			sex = input("请输入%s的性别" % (names))
			ids = int(input("请输入%s的学号" % (names)))
			result = int(input("请输入%s的成绩" % (names)))
			cls["names"] = names
			cls["age"] = age
			cls["sex"] = sex
			cls["ids"] = ids
			cls["result"] = result
			student.append(cls)
			# 是否继续录入
			num = input("是否继续录入 1：是 \n 2:否 ")
			if num == '1':
				add()
			elif num == '2':
				print('正在退出\n lading.....................')
			else:
				print("输入有误  ,正在退出")


		# 删
		def dele(lists):

			if len(lists):
				# 姓名删除
				num = (input("请选择删除的方式：\n 1：通过姓名删除\n 2：通过学号删除 \n 退出请输入其他值：\n请选择："))
				if num == '1':
					names = input("请输入姓名：")
					for i in student:
						if i["names"] == names:
							student.pop(student.index(i))
							sele(student)
							des = int(input("是否继续删除：\n 1:是 \n 2:否"))
							if des == 1:
								dele(status)
						else:
							print("抱歉并没有找到姓名为：%s的学生" % (names))
							break
				# 学号删除
				elif num == '2':
					ids = int(input("请输入学号："))
					for i in student:
						if i["ids"] == ids:
							student.pop(student.index(i))
							sele(student)
							des = int(input("是否继续删除：\n 1:是 \n 2:否"))
							if des == 1:
								dele(status)
						else:
							print("抱歉并没有找到学号为：%s的学生" % (names))
							break

				else:
					print("输入有误")

			else:
				null()


		# 改
		def unda(lists):
			if len(lists):
				cond = int(input("请选择修改方式 \n 1:通过姓名 \n 2:通过学号  \n 请输入："))
				if cond == 1:
					num = input("请输入姓名：")
					for i in student:
						if i["names"] == num:
							# 获取下标

							#print(student.index(i))
							#sele(student)

							while True:
								tes = int(input(
									"你要修改%s的那一条信息\n 1:姓名 \n 2:年龄 \n 3:性别 \n 4:学号 \n 5:成绩 \n  其他键：退出修改 \n 请输入：" % (num)))
								if tes == 1:
									student[student.index(i)]["names"] = input("请输入")
									continue
								elif tes == 2:
									student[student.index(i)]["age"] = int(input("请输入"))
									continue
								elif tes == 3:
									student[student.index(i)]["sex"] = input("请输入")
									continue
								elif tes == 4:
									student[student.index(i)]["ids"] = int(input("请输入"))
									continue
								elif tes == 5:
									student[student.index(i)]["result"] = int(input("请输入"))
									continue
								else:
									sele(student)
									break
				if cond == 2:
					num = input("请输入学号：")
					for i in student:
						if i["ids"] == num:
							# 获取下标

							

							while True:
								tes = int(input(
									"你要修改%s的那一条信息\n 1:姓名 \n 2:年龄 \n 3:性别 \n 4:学号 \n 5:成绩 \n  其他键：退出修改 \n 请输入：" % (num)))
								if tes == 1:
									student[student.index(i)]["names"] = input("请输入:")
									continue
								elif tes == 2:
									student[student.index(i)]["age"] = int(input("请输入:"))
									continue
								elif tes == 3:
									student[student.index(i)]["sex"] = input("请输入:")
									continue
								elif tes == 4:
									student[student.index(i)]["ids"] = int(input("请输入:"))
									continue
								elif tes == 5:
									student[student.index(i)]["result"] = int(input("请输入:"))
									continue
								else:
									sele(student)
									break
			else:
				null()


		# 查
		def sele(lists):
			if len(lists):
				for i in student:
					print("姓名:%s 年龄:%s 性别:%s 学号:%s 成绩:%s \n"
						  % (i["names"], i["age"], i["sex"], i["ids"], i["result"]))
			else:
				null()


		# 统计
		def statistical(lists):
			if len(lists):
				sums = 0
				maxStudent = 0
				minStudent = 1000
				for i in lists:
					sums += i["result"]
					if maxStudent < i["result"]:
						maxStudent = i["result"]
					if minStudent > i["result"]:
						minStudent = i["result"]

				print("共录入学生%s人，总成绩为%s 平均成绩为%s 其中最高分为%s 最低分为%s"
					  % (len(student), sums, sums / len(student), maxStudent, minStudent))
			else:
				null()


		# 判断数组是否为空
		def null():
			print("你还没有录入任何信息，无法进行此次操作")



		# 主函数调用

		studentAdm(judge)
