# 需要先安装pynput包
# pip3 install pynput
# 飞机大战
from pynput.keyboard import Key, Listener, KeyCode
import random
import sys
# 生命值
number = 100   # 初始化为100，超过100不再增加，少于0，则游戏结束


# 移动
background = [[0,0,0],
              [0,"x",0],
              [0,0,0]]
print(background[0])
print(background[1])
print(background[2])


def on_press(key):
    global number
    if key == KeyCode.from_char('+'):
        number = number + int(random.randint(1,100))
        if number >= 100:
            number = 100
            print(f"已经到最大生命值{number}, 游戏继续")
        else:
            print(f"生命值已增加，现在生命值：{number}, 游戏继续")
    
    if key == KeyCode.from_char('-'):
        number = number - int(random.randint(1,100))
        if number <= 0:
            number = 0
            print("生命值已耗尽，游戏结束")
            sys.exit()
        else:
            print(f"生命值已减弱，现在生命值：{number}, 游戏继续")

    if key == KeyCode.from_char('w') :
        # print("你按下了 上 键")
        for i in 0,1,2:
            for j in 0,1,2:
                if background[i][j] == "x" and i > 0:
                    background[i][j] = "0"
                    background[i-1][j] = "x"
                    break

    elif key == KeyCode.from_char('s'):
        # print("你按下了 下 键")
        for i in 2, 1, 0:
            for j in 0, 1, 2:
                if background[i][j] == "x" and i < 2:
                    background[i][j] = "0"
                    background[i + 1][j] = "x"
                    break

    elif key == KeyCode.from_char('a'):
        # print("你按下了 左 键")
        for i in 0,1,2:
            for j in 0,1,2:
                if background[i][j] == "x" and j > 0:
                    background[i][j] = "0"
                    background[i][j - 1] = "x"
                    break

    elif key == KeyCode.from_char('d'):
        # print("你按下了 右 键")+
        for i in 0,1,2:
            for j in 0,1,2:
                if background[i][j] == "x" and j < 2:
                    background[i][j] = "0"
                    background[i][j + 1] = "x"
                    break

    print()
    print(background[0])
    print(background[1])
    print(background[2])

with Listener(on_press=on_press) as listener:
    listener.join()