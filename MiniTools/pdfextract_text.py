import PyPDF2


def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
    num_pages = len(reader.pages)
    print(f"PDF共有{num_pages}页")

    for page_num in range(num_pages):
        page = reader.pages[page_num]
        text += page.extract_text()

    return text


if __name__ == '__main__':

    # 使用示例
    pdf_text = extract_text_from_pdf("document.pdf")
    print(f"提取的文本前500个字符：\n{pdf_text[:500]}...")
