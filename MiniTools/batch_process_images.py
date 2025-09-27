import os

from PIL import Image, ImageEnhance


def batch_process_images(input_dir, output_dir, brightness=1.5, contrast=1.2, size=(800, 600)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"processed_{filename}")

            try:
                # 打开图像
                img = Image.open(input_path)

                # 调整大小
                img = img.resize(size, Image.LANCZOS)

                # 增强亮度
                enhancer = ImageEnhance.Brightness(img)
                img = enhancer.enhance(brightness)

                # 增强对比度
                enhancer = ImageEnhance.Contrast(img)
                img = enhancer.enhance(contrast)

                # 保存处理后的图像
                img.save(output_path)
                print(f"已处理: {filename}")

            except Exception as e:
                print(f"处理{filename}时出错: {e}")


if __name__ == '__main__':
    # 使用示例
    batch_process_images("./images", "./processed_images")
