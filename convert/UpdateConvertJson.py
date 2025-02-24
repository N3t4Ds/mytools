#!/usr/bin/python3
import pandas as pd

# 将数据写入convert.json文件中
def Update(data):
    data.to_json('convert.json', orient='records', lines=True)

# 制作数据
def extractdata(sourcefilename):
    df = pd.read_csv(str(sourcefilename) + ".csv", header=0, index_col="RADIO_ID")
    data = df.query('(COUNTRY=="China")|'
                    '(COUNTRY=="Taiwan")|'
                    '(COUNTRY=="Hong Kong")|'
                    '(COUNTRY=="Macao")').copy()
    return data


def go():
    pass


if __name__ == '__main__':
    go()