import time
from datetime import datetime

import requests


def monitor_website(url, interval=60, timeout=5):
    while True:
        try:
            start_time = time.time()
            response = requests.get(url, timeout=timeout)
            elapsed_time = time.time() - start_time

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            status = response.status_code

            print(f"{timestamp} - 状态: {status}, 响应时间: {elapsed_time:.2f}秒")

            if status != 200:
                print(f"警告: 网站返回状态码 {status}!")

        except requests.RequestException as e:
            print(f"错误: {e}")

        time.sleep(interval)


if __name__ == '__main__':
    # 使用示例：每分钟检查一次网站状态
    monitor_website("https://example.com")
