import math
import pandas as pd

def convert_to_group(str):
    string_array = str.split()
    numeric_list = [int(x) for x in string_array]
    length = len(numeric_list)
    k = 1 + math.log(length,2)
    print(k)
    max_value = max(numeric_list)
    min_value = min(numeric_list)

def count_by_group(str):
    string_array = str.split()
    numeric_list = [int(x) for x in string_array]
    grouped_data = {}
    for item in numeric_list:
        if item in grouped_data:
            grouped_data[item] += 1
        else:
            grouped_data[item] = 1
    # 将字典转换为DataFrame
    df = pd.DataFrame.from_dict(grouped_data, orient='index', columns=['Count'])

    # 重置索引，使索引成为DataFrame的一列（可选）
    df.reset_index(inplace=True)
    df.columns = ['Item', 'Count']  # 重命名列（可选）

    # 将DataFrame写入Excel文件
    excel_path = './grouped_data.xlsx'
    df.to_excel(excel_path, index=False)  # index=False表示不写入行索引

    print(f"Data has been written to {excel_path}")

s = """57 58 55 56 47 53 48 58 44 52
51 55 46 49 53 57 57 53 49 41
53 52 60 60 49 61 54 51 55 49
52 53 51 40 52 56 54 47 51 47
50 48 51 47 48 45 53 57 50 53
49 43 52 54 46 53 48 44 47 47
49 49 52 53 53 52 47 48 45 46
51 52 44 43 59 46 53 57 50 49
54 47 59 55 57 47 52 46 42 48
45 47 45 49 56 48 57 48 46 50"""
list = count_by_group(s)
