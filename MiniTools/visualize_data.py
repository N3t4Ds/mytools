import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def visualize_data(data_file):
    # 读取数据
    df = pd.read_csv(data_file)

    # 创建可视化目录
    os.makedirs("visualizations", exist_ok=True)

    # 生成多种可视化
    # 1. 折线图
    plt.figure(figsize=(12, 6))
    for column in df.select_dtypes(include=[np.number]).columns[:5]:  # 最多绘制5列
        plt.plot(df.index, df[column], label=column)
    plt.legend()
    plt.title("数据趋势分析")
    plt.savefig("visualizations/trend_analysis.png")

    # 2. 散点图矩阵
    pd.plotting.scatter_matrix(df.select_dtypes(include=[np.number]).iloc[:, :4],
                               figsize=(12, 12))
    plt.savefig("visualizations/scatter_matrix.png")

    # 3. 相关性热图
    plt.figure(figsize=(10, 8))
    corr = df.select_dtypes(include=[np.number]).corr()
    plt.imshow(corr, cmap='coolwarm')
    plt.colorbar()
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.title("相关性分析")
    plt.savefig("visualizations/correlation_heatmap.png")

    print("已生成数据可视化图表，保存在visualizations目录")


if __name__ == '__main__':
    # 使用示例
    visualize_data("sales_data.csv")
