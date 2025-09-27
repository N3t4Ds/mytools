import os

from PIL import Image, ImageDraw, ImageFont


def add_watermark(input_dir, output_dir, watermark_text, font_size=50, opacity=50):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 设置字体，使用默认
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"watermarked_{filename}")

            # 打开原始图像
            img = Image.open(input_path).convert("RGBA")

            # 创建水印层
            watermark = Image.new("RGBA", img.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(watermark)

            # 计算水印位置（居中）
            width, height = img.size
            text_width, text_height = draw.textsize(watermark_text, font=font)
            x = (width - text_width) // 2
            y = (height - text_height) // 2

            # 绘制水印
            draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, opacity))

            # 合并原图和水印
            watermarked_img = Image.alpha_composite(img, watermark)
            watermarked_img.convert("RGB").save(output_path)

            print(f"已添加水印: {filename}")

if __name__ == '__main__':
    # 使用示例
    add_watermark("./images", "./watermarked", "© 版权所有")
