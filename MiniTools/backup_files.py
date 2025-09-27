import datetime
import os
import shutil


def backup_files(source_dir, backup_dir, create_date_subdir=True):
    # 检查源目录是否存在
    if not os.path.exists(source_dir):
        print(f"错误: 源目录 {source_dir} 不存在")
        return

    # 创建备份目录（如果不存在）
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # 如果需要创建日期子目录
    if create_date_subdir:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        backup_subdir = os.path.join(backup_dir, current_date)
    if not os.path.exists(backup_subdir):
        os.makedirs(backup_subdir)
        target_dir = backup_subdir
    else:
        target_dir = backup_dir

    # 执行备份
    try:
        # 获取源目录中的所有文件和子目录
        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)
            target_item = os.path.join(target_dir, item)

        # 如果是目录，则递归复制
        if os.path.isdir(source_item):
            shutil.copytree(source_item, target_item, dirs_exist_ok=True)
            print(f"已备份目录: {item}")
        # 如果是文件，则直接复制
        else:
            shutil.copy2(source_item, target_item)
            print(f"已备份文件: {item}")

        print(f"备份完成! 所有文件已备份到: {target_dir}")

    except Exception as e:
        print(f"备份过程中出错: {e}")


if __name__ == '__main__':
    # 使用示例：备份当前目录下的documents文件夹到backups目录
    backup_files("./documents", "./backups")
