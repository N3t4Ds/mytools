import psutil
import time
import datetime

def monitor_system_health(interval=5, duration=60):
  end_time = time.time() + duration

  print("开始监控系统健康...")
  print("按Ctrl+C停止")

  try:
    while time.time() < end_time:
      # 获取当前时间
      current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

      # 获取CPU使用率
      cpu_percent = psutil.cpu_percent(interval=1)

      # 获取内存使用情况
      memory = psutil.virtual_memory()
      memory_percent = memory.percent

      # 获取磁盘使用情况
      disk = psutil.disk_usage('/')
      disk_percent = disk.percent

      # 获取网络信息
      net_io = psutil.net_io_counters()

      # 输出信息
      print(f"时间: {current_time}")
      print(f"CPU使用率: {cpu_percent}%")
      print(f"内存使用率: {memory_percent}%")
      print(f"磁盘使用率: {disk_percent}%")
      print(f"网络发送: {net_io.bytes_sent / 1024 / 1024:.2f} MB")
      print(f"网络接收: {net_io.bytes_recv / 1024 / 1024:.2f} MB")
      print("-" * 40)

      time.sleep(interval)

  except KeyboardInterrupt:
    print("监控已停止")

if __name__ == '__main__':
    # 使用示例：监控系统健康状态，每5秒更新一次，持续60秒
  monitor_system_health()