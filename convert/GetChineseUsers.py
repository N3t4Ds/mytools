#!/usr/bin/python3
import datetime
import os
from dataclasses import dataclass
from urllib.parse import urlparse
from urllib.request import urlretrieve

import pandas as pd


# 设定DMR用户数据类
@dataclass
class DMR_User:
    radio_ID: int
    callsign: str
    first_name: str
    last_name: str
    city: str
    state: str
    country: str


# 读取JSON文件，返回DataFrame数据
def get_convertdata(convert):
    return pd.read_json(str(convert) + ".json")['data']


# 读取CSV文件，返回DataFrame数据
def get_userdata(user):
    return pd.read_csv(str(user) + ".csv", header=0, index_col="RADIO_ID")


# 根据国家筛选返回DATAFRAME数据
def get_query(user, convert):
    return user \
        .query("COUNTRY in" + str(list(convert['country'].keys()))) \
        .copy()


# 写入新文件，成功返回'TRUE',否则'FALSE'
def to_chinese_user_list(data, convert):
    # 替换中文
    data['STATE'] = data['STATE'].map(convert['state'], na_action='ignore')
    data['COUNTRY'] = data['COUNTRY'].map(convert['country'])
    # 通过列索引调整顺序
    # 假设列的顺序是 [2, 0, 1]，即 C -> A -> B
    # df = df.iloc[:, [2, 0, 1]]
    # data = data.iloc[:, [5, 2, 3, 4, 6]]  # 这个索引超界了
    # 将列 'C' 移动到第一列
    col_to_move = data.pop('STATE')  # 删除列 'C' 并获取其数据
    data.insert(1, 'STATE', col_to_move)  # 将列 'C' 插入到索引 0 的位置
    return data


# 写入CSV文件
def to_newcsv(df, filename):
    df.to_csv(filename + ".csv")


# 下载CSV文件
def download_file(url):
    filename = urlparse(url).path.split('/')[-1]
    urlretrieve(url, filename)
    return filename


# 执行入口
def do():
    # 获取配置文件数据
    convert = get_convertdata('convert')
    # 下载的User.csv文件名
    filename = download_file(convert['url'])
    source_filename = filename.split(".")[0]
    # 输出CSV文件名
    target_filename = source_filename + datetime.datetime.now().strftime("%Y%m%d")

    # 读出user.csv文件
    df = get_query(get_userdata(source_filename), convert)
    # 写入新的CSV文件
    to_newcsv(to_chinese_user_list(df, convert), target_filename)
    print(str(target_filename) + ".csv处理完成。")
    # 删除下载的文件
    os.remove(filename)

    # print(Fore.RED + "处理失败！！！" + Style.RESET_ALL)


# 项目入口
if __name__ == '__main__':
    do()
