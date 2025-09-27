import os

def batch_rename(directory, old_ext, new_ext):
   for filename in os.listdir(directory):
       if filename.endswith(old_ext):
           new_name=filename.replace(old_ext, new_ext)
           os.rename(
               os.path.join(directory, filename),
               os.path.join(directory, new_name)
            )
   print(f"完成：将所有{old_ext}文件重命名为{new_ext}")
if __name__ == '__main__':

    # 使用示例：将目录中所有.txt文件重命名为.md文件
    batch_rename("./documents", ".txt", ".md")