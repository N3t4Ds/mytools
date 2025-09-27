from textblob import TextBlob


def analyze_sentiment(text):
    # 创建TextBlob对象
    blob = TextBlob(text)

    # 获取情感极性（-1到1之间，负值表示负面情感，正值表示正面情感）
    polarity = blob.sentiment.polarity

    # 获取主观性（0到1之间，0表示客观，1表示主观）
    subjectivity = blob.sentiment.subjectivity

    # 情感分类
    if polarity > 0.1:
        sentiment = "正面"
    elif polarity < -0.1:
        sentiment = "负面"
    else:
        sentiment = "中性"

    return {
        "原文": text,
        "情感极性": polarity,
        "主观性": subjectivity,
        "情感分类": sentiment
    }


if __name__ == '__main__':
    # 使用示例
    texts = [
        "我非常喜欢这个产品，它太棒了！",
        "这个服务真的很差，让我很失望。",
        "这只是一个普通的产品，没有特别之处。"
    ]

    for text in texts:
        result = analyze_sentiment(text)
        print(f"文本：{result['原文']}")
        print(f"情感分类：{result['情感分类']}")
        print(f"情感极性：{result['情感极性']:.2f}")
        print(f"主观性：{result['主观性']:.2f}")
        print("-" * 40)
