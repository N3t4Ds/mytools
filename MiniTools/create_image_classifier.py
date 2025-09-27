import os

import numpy as np
from PIL import Image
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def create_image_classifier(data_dir):
    # 加载数据
    X = []  # 图像数据
    y = []  # 标签

    for label in os.listdir(data_dir):
        label_dir = os.path.join(data_dir, label)
        if os.path.isdir(label_dir):
            for image_file in os.listdir(label_dir):
                if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    image_path = os.path.join(label_dir, image_file)
                    try:
                        # 打开并调整图像大小
                        img = Image.open(image_path).convert('RGB').resize((50, 50))
                        # 将图像转换为特征向量
                        features = np.array(img).flatten()
                        X.append(features)
                        y.append(label)
                    except Exception as e:
                        print(f"处理{image_path}时出错: {e}")

    # 转换为numpy数组
    X = np.array(X)
    y = np.array(y)

    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 训练分类器
    classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    classifier.fit(X_train, y_train)

    # 评估模型
    accuracy = classifier.score(X_test, y_test)
    print(f"模型准确率: {accuracy:.2f}")

    return classifier


if __name__ == '__main__':
    # 使用示例（假设有一个包含不同类别图像的数据目录）
    model = create_image_classifier("./image_dataset")
