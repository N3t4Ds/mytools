import time

import schedule


def job():
    print("执行定时任务...")
    # 在这里添加你想要执行的代码


def setup_scheduler():
    # 每天上午10点执行
    schedule.every().day.at("10:00").do(job)

    # 每小时执行一次
    schedule.every().hour.do(job)

    # 每周一执行
    schedule.every().monday.do(job)

    print("定时任务已设置，等待执行...")
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    # 开始定时任务
    setup_scheduler()
