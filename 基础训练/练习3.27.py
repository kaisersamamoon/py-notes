'''
set1 = {1,2,3,3,2}
print(set1)
print('Length = ',len(set1))
set2 = set(range(1,10))
set3 = set((1,2,3,3,2,1))
print(set2,set3)

set4 = {num for num in range(1,100) if num %3 == 0 or num % 5 ==0}
print(set4)
set1.add(4)#添加单个元素
print(set1)
set2.update([11,12])#类似于列表中的exend（）可以添加多个元素
print(set2)
set2.discard(5)#删除指定位置的元素
print(set2)
if 4 in set2:
   set2.remove(4)
print(set2)
'''
'''
set1 = {1,2,3,3,2}
set2 = set(range(1,10))
set3 = set((1,2,3,3,2,1))
set4 = {num for num in range(1,100) if num %3 == 0 or num % 5 ==0}
set5 = {num for num in range(1,100) if num %3 == 1 or num % 5 ==1}
print(set1 & set2)#交集

print(set1 | set2)#并集
print(set1 - set2)#差集
print(set1 ^ set2)#对称差
print(set2 <= set1)#False
print(set3 <= set1)#True
print(set1 <= set3)
print(set3 <= set2)
print(set4 not in set5)
'''

'''
scores = {'罗浩':95,'百元方':78,'狄仁杰':82}
print(scores)
items1 = dict(one = 1,two = 2,there = 3,four = 4)
print(items1)
items2 = dict(zip(['a','b','c'],'123'))
print(items2)
items3 = {num:num **2 for num in range(1,10)}
print(items3)
print(scores['罗浩'])
print(scores['狄仁杰'])
for key in scores:
   print(f'{key}:{scores[key]}')
scores['百元方'] = 40
scores ['诸葛孔明'] = 77
scores.update(冷面 = 67,方天画戟 = 85)
print(scores)
if '武则天' in scores:
   print(scores('武则天'))
print(scores.get('武则天'))
print(scores.get('武则天',60))
print(scores)
print(scores.popitem())
print(scores)
print(scores.popitem())
print(scores)
print(scores.pop('罗浩',95))
print(scores)
scores.clear()
print(secores)

'''
'''
import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()


'''

'''
import random


def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code
print(generate_code())

''''

import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin :
        
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'


if __name__ == '__main__':
    main()
