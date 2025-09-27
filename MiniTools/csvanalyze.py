import matplotlib.pyplot as plt
import pandas as pd


def analyze_csv(file_path):
    # 读取CSV
    df = pd.read_csv(file_path)

    # 基本统计信息
    print("数据概览:")
    print(df.describe())

    # 数据可视化
    for column in df.select_dtypes(include=['number']).columns:
        plt.figure(figsize=(10, 6))
        plt.hist(df[column], bins=20)
        plt.title(f"{column}分布")
        plt.savefig(f"{column}_distribution.png")
        print(f"已生成{column}数据分布图")

    return df


if __name__ == '__main__':
    # 使用示例
    data = analyze_csv("sales_data.csv")
