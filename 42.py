# 打开/etc/目录下的passwd文件
import os
os.chdir('/etc')
print(open('passwd'))
