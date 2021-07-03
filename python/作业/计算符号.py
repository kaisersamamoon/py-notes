print ("计算开始")
betes = 1
while betes < 1000:
    num1 =float (input ( " 请输入第一个数字:" ))
    calculate = input ( " 请输入运算符号:" )
    num2 = float (input ( " 请输入第二个数字: " ))
    if calculate == "+":
        temes = num1 + num2
    elif calculate == "-":
        temes = num1 - num2
    elif calculate == "*":
        temes = num1 * num2
    elif calculate == "/":
        if num2 ==0:
            print ( "数字一，二不能为零" )
        else:
            temes =num1 / num2
    elif calculate != ['+','-','*','/' ]:
        print ("运算符号输入错误，请重试：")
    print ( temes )        
        
