from gensim.summarization import summarize


def generate_summary(text, ratio=0.2):
    # 生成文本摘要
    summary = summarize(text, ratio=ratio)
    return summary


if __name__ == '__main__':
    # 使用示例
    text = """这里是一段很长的文本内容..."""
    summary = generate_summary(text)
    print(f"原文长度: {len(text)}字符")
    print(f"摘要长度: {len(summary)}字符")
    print(f"摘要内容:\n{summary}")
