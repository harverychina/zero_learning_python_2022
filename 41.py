import time

date_str = "2022-05-20 13:40:40"

date = time.strptime(date_str, "%Y-%m-%d %H:%M:%S")
# print(date)
new_date = time.strftime("%Y年%m月%d日 %H时%M分%S秒", date)
# print(new_date)
print(f"当前时间是：{new_date}")

print(
    f"当前时间是：{date_str[:4]}年{date_str[5:7]}月{date_str[8:10]}日 {date_str[11:13]}时{date_str[14:16]}分{date_str[17:19]}秒"
)
