import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.io import wavfile
import os

def visualize_music(audio_file, output_dir="./music_viz"):
  # 创建输出目录
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

  # 读取音频文件
  sample_rate, audio_data = wavfile.read(audio_file)

  # 如果是立体声，取平均转为单声道
  if len(audio_data.shape) > 1:
    audio_data = np.mean(audio_data, axis=1)

  # 标准化音频数据
  audio_data = audio_data / (2.0 ** 15)

  # 创建时间数组
  duration = len(audio_data) / sample_rate
  time = np.linspace(0., duration, len(audio_data))

  # 创建图表
  fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

  # 波形图
  ax1.plot(time, audio_data, color='blue')
  ax1.set_title('音频波形')
  ax1.set_xlabel('时间 (秒)')
  ax1.set_ylabel('振幅')

  # 计算频谱
  spec, freqs, t, im = ax2.specgram(audio_data, NFFT=1024, Fs=sample_rate,
                  noverlap=512, cmap='viridis')
  ax2.set_title('频谱图')
  ax2.set_xlabel('时间 (秒)')
  ax2.set_ylabel('频率 (Hz)')

  plt.tight_layout()

  # 保存图像
  output_file = os.path.join(output_dir, os.path.basename(audio_file).replace('.wav', '.png'))
  plt.savefig(output_file)
  print(f"已生成音乐可视化: {output_file}")

  # 显示图像
  plt.show()

if __name__ == '__main__':
  # 使用示例（需要一个WAV格式的音频文件）
  visualize_music("music.wav")