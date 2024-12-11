import pandas as pd

# 读取 Excel 文件
df = pd.read_excel('original_data.xlsx')

# 添加前导零到日期列中的单个数字的月份和日期
df['Date_of_Journey'] = df['Date_of_Journey'].apply(lambda x: '-'.join([f'{int(i):02d}' for i in x.split('-')]))

# 保存修改后的数据到新的 Excel 文件
df.to_excel('original_data.xlsx', index=False)

print("数据已修改并保存到 modified_data.xlsx 文件中。")
