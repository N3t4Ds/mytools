import random
import string

def generate_password(length=12, include_digits=True, include_special=True):
  # 定义字符集
  chars = string.ascii_letters # 字母
  if include_digits:
    chars += string.digits # 数字
  if include_special:
    chars += string.punctuation # 特殊字符

  # 生成密码
  password = ''.join(random.choice(chars) for _ in range(length))

  # 确保密码至少包含一个大写字母、小写字母、数字和特殊字符
  has_upper = any(c.isupper() for c in password)
  has_lower = any(c.islower() for c in password)
  has_digit = any(c.isdigit() for c in password) if include_digits else True
  has_special = any(c in string.punctuation for c in password) if include_special else True

  # 如果不满足条件，重新生成
  if not (has_upper and has_lower and has_digit and has_special):
    return generate_password(length, include_digits, include_special)

  return password

if __name__ == '__main__':
    # 使用示例
    for _ in range(5):
    pwd = generate_password()
    print(f"随机密码: {pwd}")