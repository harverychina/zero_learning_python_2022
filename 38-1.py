import argparse
# 执行方式 python3 6-1arg-1.py -number 100
parser = argparse.ArgumentParser(description="这个程序用来演示参数处理")
parser.add_argument( "number", help="输入一个数字")
args = parser.parse_args()
print(f"你输入的number参数是 {args.number} ")