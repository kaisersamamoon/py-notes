print ("四则计算".center(40),)
print ("计算开始".center(40),)
while True:
    num1 =float (input ( " 请输入第一个数字:" ))
    calculate = input ( " 请输入运算符号:" )
    num2 = float (input ( " 请输入第二个数字: " ))
    temes = int (input ("你选择保留几位小数："))
    n = temes
    if calculate == "+":
        flyme = num1 + num2
    elif calculate == "-":
        flyme = num1 - num2
    elif calculate == "*":
        flyme = num1 * num2
    elif calculate == "/":
        if num2 ==0:
            print ( "数字一，二不能为零" )
            continue
        else:
            flyme =num1 / num2
    elif calculate != ['+','-','*','/' ]:
        print ("运算符号输入错误，请重试：")
        continue
    print("保留",n,"位小数后结果为;", round(flyme,n))
        
        
        
