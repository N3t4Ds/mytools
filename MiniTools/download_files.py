import os

import requests


def download_files(urls, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for url in urls:
        filename = url.split("/")[-1]
        filepath = os.path.join(destination_folder, filename)

        print(f"正在下载: {url}")
        response = requests.get(url, stream=True)

        with open(filepath, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

        print(f"已下载: {filename}")


if __name__ == '__main__':
    # 使用示例
    urls = [
        "https://example.com/file1.pdf",
        "https://example.com/file2.pdf",
        "https://example.com/file3.pdf"
    ]

    download_files(urls, "./downloads")
