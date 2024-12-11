import requests
import re
from openpyxl import Workbook

# 创建 Excel 工作簿和工作表
wb = Workbook()
ws = wb.active
ws.append(["日期", "天气1", "天气2", "最高温度", "最低温度", "AQI", "风向", "降水量"])

# 获取网页源代码
url = [
    "https://www.tianqi24.com/in_new-delhi/history202301.html",
    "https://www.tianqi24.com/in_new-delhi/history202302.html",
    "https://www.tianqi24.com/in_new-delhi/history202303.html",
    "https://www.tianqi24.com/in_new-delhi/history202304.html",
    "https://www.tianqi24.com/in_new-delhi/history202305.html",
    "https://www.tianqi24.com/in_new-delhi/history202306.html",
    "https://www.tianqi24.com/in_new-delhi/history202307.html",
    "https://www.tianqi24.com/in_new-delhi/history202308.html",
    "https://www.tianqi24.com/in_new-delhi/history202309.html",
    "https://www.tianqi24.com/in_new-delhi/history202310.html",
    "https://www.tianqi24.com/in_new-delhi/history202311.html",
    "https://www.tianqi24.com/in_new-delhi/history202312.html"
]

for i in range(12):
    response = requests.get(url[i])
    html_content = response.text

    # 定义正则表达式模式
    # pattern = r'<div>(\d{2}-\d{2})</div>\s*<div>\s*(.*?)\s*</div>\s*<div class="red">(\d+℃)</div>\s*<div class="green">(\d+℃)</div>\s*<div>(\d+)</div>\s*<div>(.*?)</div>\s*<div>([\d.]+)</div>'
    pattern = r'<div>(\d{2}-\d{2})</div>\s*<div>\s*(.*?)\s*(?:<span>&nbsp;&nbsp;/&nbsp;(.*?)</span>)?\s*</div>\s*<div class="red">(\d+℃)</div>\s*<div class="green">(\d+℃)</div>\s*<div>(\d+)</div>\s*<div>(.*?)</div>\s*<div>([\d.]+)</div>'

    # 匹配天气信息
    weather_data = re.findall(pattern, html_content)

    # 将数据写入 Excel 文件
    for data in weather_data:
        ws.append(data)

# 保存 Excel 文件
wb.save("Delhi_Weather_2023.xlsx")

import pandas as pd

# 读取Excel文件
df = pd.read_excel('Delhi_Weather_2023.xlsx')

# 合并天气数据列
df['天气'] = df['天气1'].fillna('') + df['天气2'].fillna('')

# 将指定形式的天气数据进行合并
df['天气'] = df['天气'].str.replace('<b>', '').str.replace('</b>', '').str.replace('\t', '').str.replace('\n', '').str.replace('\r', '').str.strip()

# 删除原始的天气数据列
df.drop(['天气1', '天气2'], axis=1, inplace=True)

# 保存修改后的Excel文件
df.to_excel('merged_weather_data.xlsx', index=False)
