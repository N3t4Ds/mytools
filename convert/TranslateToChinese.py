#!/usr/bin/python3
import os
import sys
from datetime import datetime
from urllib.parse import urlparse
from urllib.request import urlretrieve

import pandas as pd


# 筛选出中国、香港、澳门、台湾的数据
# 读入CSV文件，通过筛选转换成中文通讯录，用于UV-4R数字对讲机使用user.csv'
def extractdata(sourcefilename):
    # 读出CSV文件到数据
    df = pd.read_csv(str(sourcefilename) + ".csv", header=0, index_col="RADIO_ID")
    data = df.query('(COUNTRY=="China")|'
                    '(COUNTRY=="Taiwan")|'
                    '(COUNTRY=="Hong Kong")|'
                    '(COUNTRY=="Macao")').copy()
    return data


# 读取Json文件
def readjsondata():
    # 读入一个json文件的一个节点数据
    return pd.read_json('convert.json')['data']


# 写人Json文件
def writejsondata():
    pass


# 设置个选择项参数 来选择截取的字段
def tochinese(data, df_conv, mode):
    data['STATE'] = data['STATE'].map(df_conv['state'], na_action='ignore')
    data['COUNTRY'] = data['COUNTRY'].map(df_conv['country'])
    # convert.json修改好城市拼音转中文
    # data['CITY'] = data['CITY'].map(df_conv['city'])

    match mode:
        case 1:
            # CITY 由 STATE替换，然后STATE替换为空，COUNTRY,STATE替换成中文。
            data['CITY'] = data['STATE']
            data['STATE'] = None

        case 2:
            # CITY 由 STATE替换，STATE,COUNTRY替换为空。
            data['CITY'] = data['STATE']
            data['STATE'] = None
            data['COUNTRY'] = None

        case 3:
            # COUNTRY,STATE替换成空值，CITY值不变
            data['STATE'] = None
            data['COUNTRY'] = None

        case _:
            # 缺省是保留所有项目数据
            pass
    return data


# 将数据存储csv文件
def writecsvdata(data, targetfilename):
    # 写入数据到CSV文件
    data.to_csv(str(targetfilename) + ".csv")


# 下载user.csv文件到本地
def download_file(url):
    url = pd.read_json('convert.json')['data']['url']
    filename = urlparse(url).path.split('/')[-1]
    urlretrieve(url, filename)  # 是不是在这里增加个判断是否成功
    return str(filename)


# 执行
def go(mode):
    jsondata = readjsondata()
    filename = download_file(jsondata['url'])
    source = filename.split(".")[0]
    sourcedata = extractdata(source)
    now = datetime.now()
    target = source + now.strftime("%Y%m%d")
    writecsvdata(tochinese(sourcedata, jsondata, mode), target)

    os.remove(filename)
    print(str(target) + ".csv处理完成。")


if __name__ == '__main__':
    go(sys.argv[1])
