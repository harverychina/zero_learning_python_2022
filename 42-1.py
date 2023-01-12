# 文件编码
f = open('demo_GBK.txt', mode='w', encoding='GBK')
f.write("人生苦短，我用Python")
f.close()

f = open('demo_GBK.txt', mode='r', encoding='GBK')
data = f.readlines()
print(data)
f.close
