import sys

while True:
    key = input("请输入指令:")
    match  key :
        case "q" | "quit":
            print("程序已经退出")
            sys.exit()
        case _:
            print("程序还在进行中")
